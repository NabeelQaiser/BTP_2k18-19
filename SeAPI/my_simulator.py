import sys
import os
import datetime
from antlr4 import *
from MyCFG import MyCFG
from MyHelper import MyHelper
from MyUtility import MyUtility
from MyVisitor import MyVisitor
from PreProcessor import PreProcessor
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser
from MyRawCfgToGraph import MyRawCfgToGraph
from gen.MySsaStringGenerator import MySsaStringGenerator
from gen.SymbolicVcGeneration import SymbolicVcGeneration
from gen.z3formulaofvcs import z3formulaofvcs
from subprocess import call

def main(argv):
    data = "gen/data/" + argv[1]
    spec = "specification/" + argv[2]
    processor = PreProcessor(spec, data)
    tableInfo, assume, assrt, resultString = processor.start()

    file = open('upper_input.sql', "w")
    file.write(resultString)
    file.close()

    #input = FileStream('upper_input.sql')
    #name = "gen/data/"+argv[1]
    #file = open(name, "r")
    #content = file.read().upper()
    #file.close()
    #TODO: Processing of specification file and append constraint into plsql code.
    #file = open('upper_input.sql', "w")
    #file.write(content)
    #file.close()
    startTime = datetime.datetime.now()
    input = FileStream('upper_input.sql')
    lexer = PlSqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PlSqlParser(stream)
    tree = parser.sql_script()
    #ast = tree.toStringTree(recog=parser)
    #print(ast)
    # print(str(MyPlSqlVisitor(parser).getRuleName(tree)))
    # print("\n\n", signature(tree.toStringTree), "\n")

    cfg = MyCFG()
    #print(cfg)
    helper = MyHelper(parser)
    utility = MyUtility(helper)
    v = MyVisitor(parser, cfg, utility)
    v.visit(tree)


    print(v.rawCFG)

    for key in v.cfg.nodes:
        if v.cfg.nodes[key].ctx != None:
            pass
            #print(key, " --> ", v.cfg.nodes[key].ctx.getText())


    res = MyRawCfgToGraph(v.rawCFG, cfg)
    res.execute()
    cfg.printPretty()
    #cfg.dotToPng(cfg.dotGraph, "raw_graph.dot")
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
    
    #vcs = SymbolicVeGeneration(cfg, parser)
    #vcs.SymbolicVcCalculation()
    
    
    utility.dfs(cfg.nodes[0].id, cfg)
    
    #start = cfg.nodes[0].id
    
    for nodeId in cfg.nodes:
        last_node = cfg.nodes[nodeId].id


    
    list_of_path = list(utility.dfs_path(cfg.nodes[0].id, last_node, cfg))
    #print(list_of_path)
    #print(start)
    #print(last_node)
    
    vcs = SymbolicVcGeneration(cfg, parser)
    z3fr = z3formulaofvcs(cfg, parser)
    #vcs.SymbolicVcCalculation(cfg, start, last_node)
    
    list_of_vcs = []
    for path in list_of_path:
        print("\n Path %d --->", path)
        vc =vcs.SymbolicVc(path)
        print(vc)
        #print(varaibleset)
        variableset = z3fr.z3VariableDeclarationSet(path)
        z3fr.z3FormulaForEachPath(vc)
        call(['python', 'z3formula.py'])

    finishTime = datetime.datetime.now()
    timeDifference = (finishTime - startTime).total_seconds()
    print(timeDifference*60)



        
    #file = open("dbvcs.txt","w")
    #for ele in list_of_vcs:
       # file.write("%s\n" % ele)
        #print (ele+"\n")
    #file.close()
            
    
    #for path in list_of_path:
        
    
    
    #print(list_of_path)
    
    #for path in list_of_path:
        #print(path)
    
    
    #print(cfg.nodes[0].id)

    # utility.generateFinalDotGraph(cfg)   
   
    #for nodeId in cfg.nodes:
        #cfg.nodes[nodeId].printPretty()

    #
    #hello = utility.generateFinalDotGraph(cfg)
    #print(hello)
    #cfg.dotToPng(hello, "versioned_graph.dot")

    #hello2 = utility.generateVersionedDotFile(cfg)
    #print(hello2)
    #cfg.dotToPng(hello2, "versioned_graph.dot")

    #hello3 = utility.generateVersionedPhiNodeWalaDotFile(cfg)
    #print(hello3)
    #cfg.dotToPng(hello3, "versioned_phi_node_wala_graph.dot")
    
    #hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
    #print(hello4)
    #cfg.dotToPng(hello4, "destructed_phi_node_wala_graph.dot")

    #utility.accumulate(cfg)
    
    #se = VC_Generation(cfg, utility)
    #se.SeVc(cfg, utility)
    #ast = tree.toStringTree(recog=parser)
    #print(ast)

    


if __name__ == '__main__':
    main(sys.argv)
