import sys

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyRawCfgToGraph import MyRawCfgToGraph
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from WpcGenerator import WpcGenerator
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser


def main(argv):
    name = "wpc/data/" + argv[1]
    file = open(name, "r")
    content = file.read().upper()
    file.close()
    file = open('wpc/upper_input.sql', "w")
    file.write(content)
    file.close()

    input = FileStream('wpc/upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()

    cfg = MyCFG()
    helper = MyHelper(parser)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)

    print(v.rawCFG, "\n")

    for key in v.cfg.nodes:
        if v.cfg.nodes[key].ctx != None:
            print(key, " --> ", v.cfg.nodes[key].ctx.getText())
    print("\n")

    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    print("\n")

    cfg.dotToPng(cfg.dotGraph, "wpc/raw_graph")
    utility.generateVariableSet(cfg)

    ssaString = MySsaStringGenerator(cfg, parser)
    # ssaString.execute()

    ### approach for generating wpcString without any Conditional Node... too Naive to use...

    # totalNodes = len(cfg.nodes.keys())
    # totalNodes = totalNodes-1
    # # print(totalNodes)
    # assertString = ""
    # while(totalNodes > 0):
    #     if len(cfg.nodes[totalNodes].parent) < 1:
    #         break
    #     if helper.getRuleName(cfg.nodes[totalNodes].ctx) == "assert_statement":
    #         # print("got it", totalNodes, ssaString.getTerminal(cfg.nodes[totalNodes].ctx.children[1]))
    #         assertString = ssaString.getTerminal(cfg.nodes[totalNodes].ctx.children[1])
    #     elif not assertString=="":
    #         assertString = assertString.replace("  ", " ")
    #         assertString = assertString.strip()
    #         tokens = assertString.split(" ")
    #         if len(cfg.nodes[totalNodes].variableLHS) > 0:
    #             for i in cfg.nodes[totalNodes].variableLHS:
    #                 # print(i)
    #                 for j in range(len(tokens)):
    #                     # print(tokens[j])
    #                     if i==tokens[j] and helper.getRuleName(cfg.nodes[totalNodes].ctx) == "assignment_statement":
    #                         tokens[j] = "( " + ssaString.getTerminal(cfg.nodes[totalNodes].ctx.children[2]) + " )"    # strictly assignment_statement
    #         print(tokens)
    #         assertString = ""
    #         for j in range(len(tokens)):
    #             assertString = assertString + tokens[j] + " "
    #         print(assertString)
    #     totalNodes = totalNodes - 1
    #
    # print("\n\n\t", assertString, "\n")


    algo = WpcGenerator(cfg)
    algo.execute()
    print("\n\n", algo.finalWpcString, "\n")


    # #all properties of each node
    # for nodeId in cfg.nodes:
    #     cfg.nodes[nodeId].printPretty()


if __name__ == '__main__':
    main(sys.argv)


# TODO notes:
#   1. if there is no 'else' after 'elsif' then *last elsif* not coming in RAW-CFG, BUT, if there is no 'else' after 'if' then *empty else block* coming in RAW-CFG & that's OK.