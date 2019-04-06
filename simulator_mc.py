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
    tableInfo, predicates, predicateVarSet, resultString = processor.start()

    file = open('mc/upper_input.sql', "w")
    file.write(resultString)
    file.close()

    # recording startTime
    startTime = datetime.datetime.now()

    input = FileStream('mc/upper_input.sql')
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

    # print(v.rawCFG, "\n")

    # for key in v.cfg.nodes:
    #     if v.cfg.nodes[key].ctx != None:
    #         print(key, " --> ", v.cfg.nodes[key].ctx.getText())
    # print("\n")

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    # cfg.printPretty()
    # print("\n")

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

    # print("\n**** Final WPC String:\n", algo.finalWpcString, "\n")

    # print(algo.variablesForZ3)

    # algo.finalWpcString = "( ( z ) ^ ( ( ! ( y ) ) ==> ( ( ( 2 ) v ( x ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( ( ( true ) ) ==> ( y - 2 ) ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( z ) ==> ( u ) ) ^ ( ( ! ( y ) ) ==> ( true ) ) ^ ( ( a ) ==> ( b ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ==> ( true ) ) )"       # for testing! Don't UNCOMMENT...
    # algo.finalWpcString = "( ( ( ! ( y ) ) ^ ( true ) v ( g ) ) )"       # for testing! Don't UNCOMMENT...
    z3StringConvertor = WpcStringConverter(algo.finalWpcString)
    z3StringConvertor.execute()
    # z3StringConvertor.convertedWpc is the FINAL VC Generated...
    # print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")

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
    elif len(argv) == 3:        # python3 simulator_wpc.py <data-file-name> <spec-file-name>
        data = "mc/data/" + argv[1]    # given data-file must be +nt in "wpc/data/"
        spec = "mc/spec/" + argv[2]    # given spec-file must be +nt in "wpc/spec/"
        linesOfCode, executionTime, vcGenerated, satisfiability, modelForViolation = executeSinglePlSqlFile(data, spec)
        print("executionTime :", executionTime)
        print("vcGenerated :", vcGenerated)
        print("satisfiability :", satisfiability)
        print("modelForViolation :", modelForViolation)
    elif len(argv) == 6:        # see dataset_runner_wpc.py
        if argv[1] == "-datafilename" and argv[3] == "-data_spec_filepaths":
            linesOfCode, executionTime, vcGenerated, satisfiability, modelForViolation = executeSinglePlSqlFile(argv[4], argv[5])
            print(" "+argv[2], end="\t\t\t")
            print(linesOfCode, end="\t\t")
            print(executionTime, end="\t")
            print("1", end="\t")
            print(satisfiability, end="\t\t")
            print(modelForViolation.replace("\n", " "), end="")
            print()


if __name__ == '__main__':
    main(sys.argv)

