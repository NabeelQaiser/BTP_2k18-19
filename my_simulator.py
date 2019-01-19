import sys

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser

from MyRawCfgToGraph import MyRawCfgToGraph


def main(argv):
    name = "gen/data/"+argv[1]
    file = open(name, "r")
    content = file.read().upper()
    file.close()
    file = open('upper_input.sql', "w")
    file.write(content)
    file.close()

    input = FileStream('upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()
    # ast = tree.toStringTree(recog=parser)
    # print(str(MyPlSqlVisitor(parser).getRuleName(tree)))
    # print("\n\n", signature(tree.toStringTree), "\n")

    cfg = MyCFG()
    helper = MyHelper(parser)
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
    cfg.dotToPng(cfg.dotGraph, "raw_graph.dot")
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
    for nodeId in cfg.nodes:
        cfg.nodes[nodeId].printPretty()
    #
    # hello = utility.generateFinalDotGraph(cfg)
    # print(hello)
    # cfg.dotToPng(hello, "versioned_graph.dot")

    hello2 = utility.generateVersionedDotFile(cfg)
    #print(hello2)
    cfg.dotToPng(hello2, "versioned_graph.dot")

    hello3 = utility.generateVersionedPhiNodeWalaDotFile(cfg)
    #print(hello3)
    cfg.dotToPng(hello3, "versioned_phi_node_wala_graph.dot")

    hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
    #print(hello4)
    cfg.dotToPng(hello4, "destructed_phi_node_wala_graph.dot")
    #just comment


if __name__ == '__main__':
    main(sys.argv)