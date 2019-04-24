import sys

from antlr4 import *

from MyCFG import MyCFG
from MyHelper import MyHelper
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from PreProcessor import PreProcessor
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser

from MyRawCfgToGraph import MyRawCfgToGraph


def main(argv):
    datafile = "se/data/"+argv[1]
    specfile = "se/spec/"+argv[2]

    file = open(datafile, "r")
    content = file.read().upper()
    file.close()

    processor = PreProcessor(specfile, datafile)
    tableInfo, assumeConstraintList, assertConstraintList, resultString = processor.start()

    file = open('se/upper_input.sql', "w")
    file.write(content)
    file.close()

    input = FileStream('se/upper_input.sql')
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

    print("\n\t", v.rawCFG, "\n")

    for key in v.cfg.nodes:
        if v.cfg.nodes[key].ctx != None:
            print(key, " --> ", v.cfg.nodes[key].ctx.getText())


    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    cfg.dotToPng(cfg.dotGraph, "se/raw_graph")
    utility.generateDomSet(cfg)
    # print("Dominator set ended----------->\n\n")
    utility.generateSDomSet(cfg)
    # print("Strictly Dominator set ended ----------->\n\n")
    utility.generatIDom(cfg)
    # print("Immediate Dominator ended ----------->\n\n")
    utility.generateDFSet(cfg)
    utility.insertPhiNode(cfg)


    utility.initialiseVersinosedPhiNode(cfg)
    utility.versioniseVariable(cfg)
    utility.phiDestruction(cfg)


    ssaString = MySsaStringGenerator(cfg, parser)
    ssaString.execute()


    for nodeId in cfg.nodes:
        cfg.nodes[nodeId].printPretty()


    hello2 = utility.generateVersionedDotFile(cfg)
    #print(hello2)
    cfg.dotToPng(hello2, "se/versioned_graph")

    hello3 = utility.generateVersionedPhiNodeWalaDotFile(cfg)
    #print(hello3)
    cfg.dotToPng(hello3, "se/versioned_phi_node_wala_graph")

    hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
    #print(hello4)
    cfg.dotToPng(hello4, "se/destructed_phi_node_wala_graph")



if __name__ == '__main__':
    main(sys.argv)