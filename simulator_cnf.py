import datetime
import os
import sys
from importlib import reload

from antlr4 import *

from CnfUtility import CnfUtility
from CnfVcGenerator import CnfVcGenerator
from MyCFG import MyCFG
from MyHelper import MyHelper
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from PreProcessor import PreProcessor
from WpcStringConverter import WpcStringConverter
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser

from MyRawCfgToGraph import MyRawCfgToGraph


def executeSinglePlSqlFile(data, spec):
    f = open(data, 'r')
    linesOfCode = len(f.readlines())
    f.close()

    processor = PreProcessor(spec, data)
    tableInfo, assumeConstraint, assertConstraint, resultString = processor.start()

    file = open('cnf/upper_input.sql', "w")
    file.write(resultString)
    file.close()

    # recording startTime
    startTime = datetime.datetime.now()

    input = FileStream('cnf/upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()
    # ast = tree.toStringTree(recog=parser)
    # print(str(MyPlSqlVisitor(parser).getRuleName(tree)))
    # print("\n\n", signature(tree.toStringTree), "\n")

    cfg = MyCFG()
    helper = MyHelper(parser)
    helper.updateTableDict(tableInfo)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)

    print(v.rawCFG)

    for key in v.cfg.nodes:
        if v.cfg.nodes[key].ctx != None:
            print(key, " --> ", v.cfg.nodes[key].ctx.getText())

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    cfg.dotToPng(cfg.dotGraph, "cnf/raw_graph")  # TODO: make dot file in cnf form
    utility.generateDomSet(cfg)
    print("Dominator set ended----------->\n\n")
    utility.generateSDomSet(cfg)
    print("Strictly Dominator set ended ----------->\n\n")
    utility.generatIDom(cfg)
    print("Immediate Dominator ended ----------->\n\n")
    utility.generateDFSet(cfg)
    utility.insertPhiNode(cfg)

    utility.initialiseVersinosedPhiNode(cfg)
    utility.versioniseVariable(cfg)
    utility.phiDestruction(cfg)

    ssaString = MySsaStringGenerator(cfg, parser)
    ssaString.execute()

    # utility.generateFinalDotGraph(cfg)
    # for nodeId in cfg.nodes:
    #     cfg.nodes[nodeId].printPretty()

    cnfUtility = CnfUtility(helper)
    iCnfCfg = cnfUtility.copyCfg(cfg)
    reverseCnfCfg = cnfUtility.topologicalSort(iCnfCfg)
    cnfUtility.unvisit(iCnfCfg)
    cnfUtility.setParentBranching(iCnfCfg)

    cnfCfg = cnfUtility.reverseDictOrder(reverseCnfCfg)
    cnfUtility.copyParentBranching(cnfCfg, iCnfCfg)
    print("\n\n\n\n\n\t\t\tThe intermediate CNF form is ------------------------------>\n\n\n\n")

    # for nodeId in iCnfCfg.nodes:
    #     iCnfCfg.nodes[nodeId].printPretty()

    print("\n\n\n\n\n\t\t\tThe CNF form is ------------------------------>\n\n\n\n")

    cnfVcGenerator = CnfVcGenerator(cnfCfg, parser)

    cnfPath = []

    for nodeId in cnfCfg.nodes:
        cnfPath.append(nodeId)

    cnfVcGenerator.generateCnfVc(cnfPath)

    # print("\n\n\n\n\t\t\tThe CNF VCs are : ------------------------------->\n\n\n")
    # print(cnfVcs)

    # for nodeId in cnfCfg.nodes:
    #     cnfCfg.nodes[nodeId].printPretty()

    # cnfVc = cnfUtility.cnfVc(cnfCfg)
    #
    # print("\n\n\t\tThe CNF VCs are ----------------->\n\n\n")
    #
    # for str in cnfVc:
    #     print(str)

    varSet, z3Str = cnfUtility.iZ3format(cnfCfg)

    print("\n\n*******************\n\n", z3Str, "\n\n--------------\n\n")
    print(varSet)

    print("\n\n")
    z3Str = z3Str.replace("  ", " ")
    z3Str = z3Str.replace(" == ", " = ")
    z3Str = z3Str.replace(" = ", " == ")
    z3StringConvertor = WpcStringConverter(z3Str)
    z3StringConvertor.execute()
    print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")

    z3FileString = "# This file was generated at runtime on " + str(datetime.datetime.now()) + "\n"
    z3FileString = z3FileString + "from z3 import *\n\n"
    z3FileString = z3FileString + "class Z3RuntimeCnfFile():\n"
    z3FileString = z3FileString + "\t" + "def __init__(self):\n"
    z3FileString = z3FileString + "\t\t" + "self.finalFormula = \"\"\n"
    z3FileString = z3FileString + "\t\t" + "self.satisfiability = \"\"\n"
    z3FileString = z3FileString + "\t\t" + "self.modelForViolation = \"\"\n\n"

    z3FileString = z3FileString + "\t" + "def execute(self):\n"
    for i in varSet:
        z3FileString = z3FileString + "\t\t" + i + " = Real(\'" + i + "\')\n"
    z3FileString = z3FileString + "\n\t\ts = Solver()\n"

    if len(z3StringConvertor.implies_p) > 0:
        for i in range(len(z3StringConvertor.implies_p)):
            z3FileString = z3FileString + "\t\t" + "s.add(" + z3StringConvertor.implies_p[i] + ")\n"
            if not z3StringConvertor.convertedWpc == z3StringConvertor.implies_p_q[i]:
                z3FileString = z3FileString + "\t\t" + "s.add(" + z3StringConvertor.implies_p_q[i] + ")\n"
    #     if z3StringConvertor.convertedWpc not in z3StringConvertor.implies_p_q:
    #         z3FileString = z3FileString + "\t\t" + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    # else:
    #     z3FileString = z3FileString + "\t\t" + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    z3FileString = z3FileString + "\t\t" + "s.add( Not( " + z3StringConvertor.convertedWpc + " ) )\n"

    z3FileString = z3FileString + "\n\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t" + "print(\"%%%%%%%%%% Aggregate Formula %%%%%%%%%%\\n\", s)"
    z3FileString = z3FileString + "\n\t\t" + "self.finalFormula = str(s)"
    z3FileString = z3FileString + "\n\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t" + "print(\"%%%%%%%%%% Satisfiability %%%%%%%%%%\")\n"
    z3FileString = z3FileString + "\n\t\t" + "self.satisfiability = str(s.check())"

    z3FileString = z3FileString + "\n\t\t" + "if self.satisfiability == \"sat\":"
    z3FileString = z3FileString + "\n\t\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t\t" + "print(\"-------->> Violation Occurred...\")"
    z3FileString = z3FileString + "\n\t\t\t" + "self.satisfiability = \"Unsatisfiable\""
    z3FileString = z3FileString + "\n\t\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t\t" + "print(\"%%%%%%%%%% An Instance for which Violation Occurred %%%%%%%%%%\\n\", s.model())"
    z3FileString = z3FileString + "\n\t\t\t" + "self.modelForViolation = str(s.model())"

    z3FileString = z3FileString + "\n\t\t" + "elif self.satisfiability == \"unsat\":"
    z3FileString = z3FileString + "\n\t\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t\t" + "print(\"-------->> NO Violation Detected so far...\")"
    z3FileString = z3FileString + "\n\t\t\t" + "self.satisfiability = \"Satisfiable\""
    z3FileString = z3FileString + "\n\t\t\t" + "print()"
    z3FileString = z3FileString + "\n\t\t" + "print()\n"

    file = open('cnf/Z3RuntimeCnfFile.py', "w")
    file.write(z3FileString)
    file.close()

    import cnf.Z3RuntimeCnfFile
    from cnf.Z3RuntimeCnfFile import Z3RuntimeCnfFile
    # Reload after module's creation to avoid old module remain imported from disk...VVI...
    cnf.Z3RuntimeCnfFile = reload(cnf.Z3RuntimeCnfFile)

    z3Runtime = Z3RuntimeCnfFile()
    z3Runtime.execute()

    finishTime = datetime.datetime.now()
    timeDifference = (finishTime - startTime).total_seconds()

    return linesOfCode, timeDifference, z3StringConvertor.convertedWpc, z3Runtime.satisfiability, z3Runtime.modelForViolation



def main(argv):
    if len(argv) < 3:
        print("Not Enough Arguments. Exiting...")
    elif len(argv) == 3:
        data = "cnf/data/" + argv[1]
        spec = "cnf/spec/" + argv[2]
        executeSinglePlSqlFile(data, spec)
    elif len(argv) == 4:
        if argv[1] == "-dataset":
            dataList = os.listdir(argv[2])
            specList = os.listdir(argv[3])
            # print(dataList)
            # print(specList)
            mat = []
            counter = 0
            for dataFile in dataList:
                specFile = dataFile.split(".")[0].strip() + ".spec"
                print("~~~~~~~~~~~~~~~~ For PlSQL FileName => " + dataFile + " ~~~~~~~~~~~~~~~~")
                if specFile in specList:
                    linesOfCode, executionTime, vcGenerated, satisfiability, modelForViolation = executeSinglePlSqlFile(
                        argv[2] + "/" + dataFile, argv[3] + "/" + specFile)
                    temp = []
                    temp.append(dataFile)
                    temp.append(linesOfCode)
                    temp.append(executionTime)
                    # temp.append(vcGenerated)
                    temp.append(satisfiability)
                    temp.append(modelForViolation)
                    mat.append(temp)
                    file = open('wpc/Z3RuntimeWpcFile.py', "w")
                    file.write("# Cleared content of this File...\n\nclass Z3RuntimeWpcFile():\n\tdef __init__(self):\n\t\tself.finalFormula = \"\"\n\t\tself.satisfiability = \"\"\n\t\tself.modelForViolation = \"\"\n\n\tdef execute(self):\n\t\tprint('+++++++++++++++++++++++++++++%%%%%^^^^^^^^####')\n")
                    file.close()
                else:
                    print(specFile + " do not exist!!!")
                counter = counter + 1
                print("Counter =", counter)


            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Filename\t\tLinesOfCode\t\tExecutionTime\t\tSatisfiability\t\tViolatingInstance\n")
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    print(mat[i][j], end="\t\t")
                print()













    # data = "cnf/data/" + argv[1]
    # spec = "cnf/spec/" + argv[2]
    # processor = PreProcessor(spec, data)
    # tableInfo, assumeConstraint, assertConstraint, resultString = processor.start()
    #
    # file = open('cnf/upper_input.sql', "w")
    # file.write(resultString)
    # file.close()
    #
    # input = FileStream('cnf/upper_input.sql')
    # lexer = PlSqlLexer(input)
    # stream = CommonTokenStream(lexer)
    # parser = PlSqlParser(stream)
    # tree = parser.sql_script()
    # # ast = tree.toStringTree(recog=parser)
    # # print(str(MyPlSqlVisitor(parser).getRuleName(tree)))
    # # print("\n\n", signature(tree.toStringTree), "\n")
    #
    # cfg = MyCFG()
    # helper = MyHelper(parser)
    # helper.updateTableDict(tableInfo)
    # utility = MyUtility(helper)
    # v = MyVisitor(parser, cfg, utility)
    # v.visit(tree)
    #
    #
    #
    # print(v.rawCFG)
    #
    # for key in v.cfg.nodes:
    #     if v.cfg.nodes[key].ctx != None:
    #         print(key, " --> ", v.cfg.nodes[key].ctx.getText())
    #
    #
    # res = MyRawCfgToGraph(v.rawCFG, cfg)
    # res.execute()
    # cfg.printPretty()
    # cfg.dotToPng(cfg.dotGraph, "cnf/raw_graph")  #TODO: make dot file in cnf form
    # utility.generateDomSet(cfg)
    # print("Dominator set ended----------->\n\n")
    # utility.generateSDomSet(cfg)
    # print("Strictly Dominator set ended ----------->\n\n")
    # utility.generatIDom(cfg)
    # print("Immediate Dominator ended ----------->\n\n")
    # utility.generateDFSet(cfg)
    # utility.insertPhiNode(cfg)
    #
    #
    # utility.initialiseVersinosedPhiNode(cfg)
    # utility.versioniseVariable(cfg)
    # utility.phiDestruction(cfg)
    #
    #
    # ssaString = MySsaStringGenerator(cfg, parser)
    # ssaString.execute()
    #
    # #utility.generateFinalDotGraph(cfg)
    # # for nodeId in cfg.nodes:
    # #     cfg.nodes[nodeId].printPretty()
    #
    # cnfUtility = CnfUtility(helper)
    # iCnfCfg = cnfUtility.copyCfg(cfg)
    # reverseCnfCfg = cnfUtility.topologicalSort(iCnfCfg)
    # cnfUtility.unvisit(iCnfCfg)
    # cnfUtility.setParentBranching(iCnfCfg)
    #
    # cnfCfg = cnfUtility.reverseDictOrder(reverseCnfCfg)
    # cnfUtility.copyParentBranching(cnfCfg, iCnfCfg)
    # print("\n\n\n\n\n\t\t\tThe intermediate CNF form is ------------------------------>\n\n\n\n")
    #
    # for nodeId in iCnfCfg.nodes:
    #     iCnfCfg.nodes[nodeId].printPretty()
    #
    # print("\n\n\n\n\n\t\t\tThe CNF form is ------------------------------>\n\n\n\n")
    #
    #
    #
    # cnfVcGenerator = CnfVcGenerator(cnfCfg, parser)
    #
    # cnfPath = []
    #
    # for nodeId in cnfCfg.nodes:
    #     cnfPath.append(nodeId)
    #
    # cnfVcGenerator.generateCnfVc(cnfPath)
    #
    # # print("\n\n\n\n\t\t\tThe CNF VCs are : ------------------------------->\n\n\n")
    # # print(cnfVcs)
    #
    # for nodeId in cnfCfg.nodes:
    #     cnfCfg.nodes[nodeId].printPretty()
    #
    # # cnfVc = cnfUtility.cnfVc(cnfCfg)
    # #
    # # print("\n\n\t\tThe CNF VCs are ----------------->\n\n\n")
    # #
    # # for str in cnfVc:
    # #     print(str)
    #
    # varSet, z3Str = cnfUtility.iZ3format(cnfCfg)
    #
    # print("\n\n*******************\n\n", z3Str, "\n\n--------------\n\n")
    # print(varSet)
    #
    # print("\n\n")
    # z3Str = z3Str.replace("  ", " ")
    # z3Str = z3Str.replace(" == ", " = ")
    # z3Str = z3Str.replace(" = ", " == ")
    # z3StringConvertor = WpcStringConverter(z3Str)
    # z3StringConvertor.execute()
    # print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")
    #
    # z3FileString = "# This file was generated at runtime " + "\n"
    # z3FileString = z3FileString + "from z3 import *\n\n"
    # for i in varSet:
    #     z3FileString = z3FileString + i + " = Real(\'" + i + "\')\n"
    # z3FileString = z3FileString + "\ns = Solver()\n"
    #
    # if len(z3StringConvertor.implies_p) > 0:
    #     for i in range(len(z3StringConvertor.implies_p)):
    #         z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p[i] + ")\n"
    #         if not z3StringConvertor.convertedWpc == z3StringConvertor.implies_p_q[i]:
    #             z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p_q[i] + ")\n"
    # #     if z3StringConvertor.convertedWpc not in z3StringConvertor.implies_p_q:
    # #         z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    # # else:
    # #     z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    # z3FileString = z3FileString + "s.add( Not( " + z3StringConvertor.convertedWpc + " ) )\n"
    #
    # z3FileString = z3FileString + "\nprint()\n"
    # z3FileString = z3FileString + "\nprint(\"------------------------------------------------------------------\\nRunning script in /wpc/z3FormatWpcFile.py ....\\n\")\n"
    # z3FileString = z3FileString + "\nprint(\"%%%%%%%%%% Aggregate Formula %%%%%%%%%%\\n\", s)\n"
    # z3FileString = z3FileString + "\nprint()\n"
    # z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiability %%%%%%%%%%\\n\", s.check())\n"
    # z3FileString = z3FileString + "\nprint()\n"
    # z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiable Model %%%%%%%%%%\\n\", s.model())\n"
    # z3FileString = z3FileString + "\nprint()\n"
    #
    # file = open('cnf/z3FormatCnfFile.py', "w")
    # file.write(z3FileString)
    # file.close()
    #
    # # call(["python3", "cnf/z3FormatWpcFile.py"])
    #
    # #
    # # hello = utility.generateFinalDotGraph(cfg)
    # # print(hello)
    # # cfg.dotToPng(hello, "versioned_graph")
    #
    # #hello2 = utility.generateVersionedDotFile(cfg)
    # #print(hello2)
    # #cfg.dotToPng(hello2, "se/versioned_graph")
    #
    # #hello3 = utility.generateVersionedPhiNodeWalaDotFile(cfg)
    # #print(hello3)
    # #cfg.dotToPng(hello3, "se/versioned_phi_node_wala_graph")
    #
    # #hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
    # #print(hello4)
    # #cfg.dotToPng(hello4, "se/destructed_phi_node_wala_graph")



if __name__ == '__main__':
    main(sys.argv)