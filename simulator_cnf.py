import sys

from antlr4 import *

from CnfUtility import CnfUtility
from MyCFG import MyCFG
from MyHelper import MyHelper
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser

from MyRawCfgToGraph import MyRawCfgToGraph


def main(argv):
    name = "cnf/data/"+argv[1]
    file = open(name, "r")
    content = file.read().upper()
    file.close()
    file = open('cnf/upper_input.sql', "w")
    file.write(content)
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
    for nodeId in cfg.nodes:
        cfg.nodes[nodeId].printPretty()

    cnfUtility = CnfUtility(helper)
    iCnfCfg = cnfUtility.copyCfg(cfg)
    reverseCnfCfg = cnfUtility.topologicalSort(iCnfCfg)
    cnfUtility.unvisit(iCnfCfg)
    cnfUtility.setParentBranching(iCnfCfg)

    cnfCfg = cnfUtility.reverseDictOrder(reverseCnfCfg)
    cnfUtility.copyParentBranching(cnfCfg, iCnfCfg)
    print("\n\n\n\n\n\t\t\tThe intermediate CNF form is ------------------------------>\n\n\n\n")

    for nodeId in iCnfCfg.nodes:
        iCnfCfg.nodes[nodeId].printPretty()

    print("\n\n\n\n\n\t\t\tThe CNF form is ------------------------------>\n\n\n\n")

    for nodeId in cnfCfg.nodes:
        cnfCfg.nodes[nodeId].printPretty()

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