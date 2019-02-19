import sys

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


def main(argv):
    data = "cnf/data/" + argv[1]
    spec = "cnf/spec/" + argv[2]
    processor = PreProcessor(spec, data)
    tableInfo, constraints, resultString = processor.start()

    file = open('cnf/upper_input.sql', "w")
    file.write(resultString)
    file.close()

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
    cfg.dotToPng(cfg.dotGraph, "cnf/raw_graph")  #TODO: make dot file in cnf form
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

    #utility.generateFinalDotGraph(cfg)
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
    #
    # print("\n\n\n\n\n\t\t\tThe CNF form is ------------------------------>\n\n\n\n")



    cnfVcGenerator = CnfVcGenerator(cnfCfg, parser)

    cnfPath = []

    for nodeId in cnfCfg.nodes:
        cnfPath.append(nodeId)

    cnfVcGenerator.generateCnfVc(cnfPath)

    # print("\n\n\n\n\t\t\tThe CNF VCs are : ------------------------------->\n\n\n")
    # print(cnfVcs)

    for nodeId in cnfCfg.nodes:
        cnfCfg.nodes[nodeId].printPretty()

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

    z3StringConvertor = WpcStringConverter(z3Str)
    z3StringConvertor.execute()
    print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")

    z3FileString = "# This file was generated at runtime " + "\n"
    z3FileString = z3FileString + "from z3 import *\n\n"
    for i in varSet:
        z3FileString = z3FileString + i + " = Real(\'" + i + "\')\n"
    z3FileString = z3FileString + "\ns = Solver()\n"

    if len(z3StringConvertor.implies_p) > 0:
        for i in range(len(z3StringConvertor.implies_p)):
            z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p[i] + ")\n"
            if not z3StringConvertor.convertedWpc == z3StringConvertor.implies_p_q[i]:
                z3FileString = z3FileString + "s.add(" + z3StringConvertor.implies_p_q[i] + ")\n"
    #     if z3StringConvertor.convertedWpc not in z3StringConvertor.implies_p_q:
    #         z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    # else:
    #     z3FileString = z3FileString + "s.add(" + z3StringConvertor.convertedWpc + ")\n"
    z3FileString = z3FileString + "s.add( Not( " + z3StringConvertor.convertedWpc + " ) )\n"

    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "\nprint(\"------------------------------------------------------------------\\nRunning script in /wpc/z3FormatWpcFile.py ....\\n\")\n"
    z3FileString = z3FileString + "\nprint(\"%%%%%%%%%% Aggregate Formula %%%%%%%%%%\\n\", s)\n"
    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiability %%%%%%%%%%\\n\", s.check())\n"
    z3FileString = z3FileString + "\nprint()\n"
    z3FileString = z3FileString + "print(\"%%%%%%%%%% Satisfiable Model %%%%%%%%%%\\n\", s.model())\n"
    z3FileString = z3FileString + "\nprint()\n"

    file = open('cnf/z3FormatCnfFile.py', "w")
    file.write(z3FileString)
    file.close()

    # call(["python3", "wpc/z3FormatWpcFile.py"])

    #
    # hello = utility.generateFinalDotGraph(cfg)
    # print(hello)
    # cfg.dotToPng(hello, "versioned_graph")

    #hello2 = utility.generateVersionedDotFile(cfg)
    #print(hello2)
    #cfg.dotToPng(hello2, "se/versioned_graph")

    #hello3 = utility.generateVersionedPhiNodeWalaDotFile(cfg)
    #print(hello3)
    #cfg.dotToPng(hello3, "se/versioned_phi_node_wala_graph")

    #hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
    #print(hello4)
    #cfg.dotToPng(hello4, "se/destructed_phi_node_wala_graph")



if __name__ == '__main__':
    main(sys.argv)