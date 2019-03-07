import os
import sys
import datetime
import time
from importlib import reload
from subprocess import call

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyRawCfgToGraph import MyRawCfgToGraph
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from PreProcessor import PreProcessor
from WpcGenerator import WpcGenerator
from WpcStringConverter import WpcStringConverter
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser



def executeSinglePlSqlFile(data, spec):
    f = open(data, 'r')
    linesOfCode = len(f.readlines())
    f.close()

    processor = PreProcessor(spec, data)
    tableInfo, assumeConstraintList, assertConstraintList, resultString = processor.start()

    file = open('wpc/upper_input.sql', "w")
    file.write(resultString)
    file.close()

    # recording startTime
    startTime = datetime.datetime.now()

    input = FileStream('wpc/upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()

    cfg = MyCFG()
    helper = MyHelper(parser)
    helper.updateTableDict(tableInfo)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)

    print(v.rawCFG, "\n")

    # for key in v.cfg.nodes:
    #     if v.cfg.nodes[key].ctx != None:
    #         print(key, " --> ", v.cfg.nodes[key].ctx.getText())
    # print("\n")

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    print("\n")

    # cfg.dotToPng(cfg.dotGraph, "wpc/raw_graph")
    utility.generateVariableSet(cfg)

    # all properties of each node
    # for nodeId in cfg.nodes:
    #     cfg.nodes[nodeId].printPretty()


    ssaString = MySsaStringGenerator(cfg, parser)
    # ssaString.execute()


    algo = WpcGenerator(cfg, helper, ssaString)
    algo.execute()
    algo.finalWpcString = algo.finalWpcString.replace("  ", " ")
    # done: replace " = " with " == " in algo.finalWpcString
    algo.finalWpcString = algo.finalWpcString.replace(" = ", " == ")

    print("\n**** Final WPC String:\n", algo.finalWpcString, "\n")

    # print(algo.variablesForZ3)

    # algo.finalWpcString = "( ( z ) ^ ( ( ! ( y ) ) ==> ( ( ( 2 ) v ( x ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( ( ( true ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( true ) ) ^ ( ( a ) ==> ( b ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ==> ( true ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ^ ( true ) v ( g ) ) )"       # for testing! Don't UNCOMMENT...
    z3StringConvertor = WpcStringConverter(algo.finalWpcString)
    z3StringConvertor.execute()
    # z3StringConvertor.convertedWpc is the FINAL VC Generated...
    print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")

    z3FileString = "# This file was generated at runtime on " + str(datetime.datetime.now()) + "\n"
    z3FileString = z3FileString + "from z3 import *\n\n"
    z3FileString = z3FileString + "class Z3RuntimeWpcFile():\n"
    z3FileString = z3FileString + "\t" + "def __init__(self):\n"
    z3FileString = z3FileString + "\t\t" + "self.finalFormula = \"\"\n"
    z3FileString = z3FileString + "\t\t" + "self.satisfiability = \"\"\n"
    z3FileString = z3FileString + "\t\t" + "self.modelForViolation = \"\"\n\n"

    z3FileString = z3FileString + "\t" + "def execute(self):\n"
    for i in algo.variablesForZ3:
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

    file = open('wpc/Z3RuntimeWpcFile.py', "w")
    file.write(z3FileString)
    file.close()

    # import file created on Runtime...
    import wpc.Z3RuntimeWpcFile
    from wpc.Z3RuntimeWpcFile import Z3RuntimeWpcFile
    # Reload after module's creation to avoid old module remain imported from disk...VVI...
    wpc.Z3RuntimeWpcFile = reload(wpc.Z3RuntimeWpcFile)

    z3Runtime = Z3RuntimeWpcFile()
    z3Runtime.execute()
    # print(z3Runtime.finalFormula)
    # print(z3Runtime.satisfiability)
    # print(z3Runtime.modelForViolation)

    # recording finishTime
    finishTime = datetime.datetime.now()
    timeDifference = (finishTime-startTime).total_seconds()

    return linesOfCode, timeDifference, z3StringConvertor.convertedWpc, z3Runtime.satisfiability, z3Runtime.modelForViolation



def main(argv):
    if len(argv) < 3:
        print("Not Enough Arguments. Exiting...")
    elif len(argv) == 3:
        data = "wpc/data/" + argv[1]
        spec = "wpc/spec/" + argv[2]
        linesOfCode, executionTime, vcGenerated, satisfiability, modelForViolation = executeSinglePlSqlFile(data, spec)
        print(satisfiability)
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
                print("~~~~~~~~~~~~~~~~ For PlSQL FileName => "+ dataFile +" ~~~~~~~~~~~~~~~~")
                if specFile in specList:
                    linesOfCode, executionTime, vcGenerated, satisfiability, modelForViolation = executeSinglePlSqlFile(argv[2]+"/"+dataFile, argv[3]+"/"+specFile)
                    temp = []
                    temp.append(dataFile)
                    temp.append(linesOfCode)
                    temp.append(executionTime)
                    # temp.append(vcGenerated)
                    temp.append(satisfiability)
                    temp.append(modelForViolation)
                    mat.append(temp)
                else:
                    print(specFile + " do not exist!!!")
                counter = counter + 1
                print("Counter =", counter)
            # file = open('wpc/Z3RuntimeWpcFile.py', "w")
            # file.write("# Cleared content of this File...\n\nclass Z3RuntimeWpcFile():\n\tdef __init__(self):\n\t\tself.finalFormula = \"\"\n\t\tself.satisfiability = \"\"\n\t\tself.modelForViolation = \"\"\n\n\tdef execute(self):\n\t\tpass\n")
            # file.close()

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Filename\t\tLinesOfCode\t\tExecutionTime\t\tSatisfiability\t\tViolatingInstance\n")
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    print(mat[i][j], end="\t\t")
                print()


if __name__ == '__main__':
    main(sys.argv)


# TODO notes:
