import sys

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyRawCfgToGraph import MyRawCfgToGraph
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from WpcGenerator import WpcGenerator
from WpcStringConverter import WpcStringConverter
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
    # print("\n\n", algo.finalWpcString.replace(" ", ""), "\n")

    z3StringConvertor = WpcStringConverter(algo.finalWpcString)
    z3StringConvertor.execute()
    print("\n**** WPC String in Z3 Format:\n", z3StringConvertor.convertedWpc, "\n")




if __name__ == '__main__':
    main(sys.argv)


# TODO notes:
