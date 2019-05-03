import sys
import os
import datetime
from antlr4 import *
from SeAPI.MyCFG import MyCFG
from SeAPI.MyHelper import MyHelper
from SeAPI.MyUtility import MyUtility
from SeAPI.MyVisitor import MyVisitor
from SeAPI.PreProcessor import PreProcessor
from SeAPI.gen.PlSqlLexer import PlSqlLexer
from SeAPI.gen.PlSqlParser import PlSqlParser
from SeAPI.MyRawCfgToGraph import MyRawCfgToGraph
from SeAPI.gen.MySsaStringGenerator import MySsaStringGenerator
from SeAPI.gen.SymbolicVcGeneration import SymbolicVcGeneration
from SeAPI.gen.z3formulaofvcs import z3formulaofvcs

# SeApi Debugging Class, it is used from "simulator_se_api.py"


class TesterClassForSeApi():
    def __init__(self):
        pass

    def execute(self, data, spec, pwd):
        data = pwd + "SeAPI/gen/data/" + data
        spec = pwd + "SeAPI/specification/" + spec

        f = open(data, 'r')
        linesOfCode = len(f.readlines())
        f.close()

        processor = PreProcessor(spec, data)
        tableInfo, assume, assrt, resultString = processor.start()

        file = open(pwd + 'SeAPI/upper_input.sql', "w")
        file.write(resultString)
        file.close()

        input = FileStream(pwd + 'SeAPI/upper_input.sql')
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

        print("\nRaw CFG :", v.rawCFG)

        res = MyRawCfgToGraph(v.rawCFG, cfg)
        res.execute()
        utility.generateDomSet(cfg)
        utility.generateSDomSet(cfg)
        utility.generatIDom(cfg)
        utility.generateDFSet(cfg)
        utility.insertPhiNode(cfg)

        utility.initialiseVersinosedPhiNode(cfg)
        utility.versioniseVariable(cfg)
        utility.phiDestruction(cfg)

        ssaString = MySsaStringGenerator(cfg, parser)
        ssaString.execute()

        # for nodeId in cfg.nodes:
        #     cfg.nodes[nodeId].printPretty()

        # cfg.dotToPng(cfg.dotGraph, pwd + "SeAPI/" + "raw_graph.dot")

        # hello1 = utility.generateBeforeVersioningDotFile(cfg)
        # cfg.dotToPng(hello1, pwd + "SeAPI/" + "before_versioning_graph.dot")

        # hello4 = utility.generateDestructedPhiNodeWalaDotFile(cfg)
        # cfg.dotToPng(hello4, pwd + "SeAPI/" + "destructed_phi_node_wala_graph.dot")


        utility.dfs(cfg.nodes[0].id, cfg)

        for nodeId in cfg.nodes:
            last_node = cfg.nodes[nodeId].id

        list_of_path = list(utility.dfs_path(cfg.nodes[0].id, last_node, cfg))


        vcs = SymbolicVcGeneration(cfg, parser)
        z3fr = z3formulaofvcs(cfg, parser)

        # listOfPaths = []
        # listOfSatisfiability = []

        print("////// Paths & VCs...")
        for i in range(len(list_of_path)):
            vc = vcs.SymbolicVc(list_of_path[i])
            variableset = z3fr.z3VariableDeclarationSet(list_of_path[i])
            z3fr.z3FormulaForEachPath(vc, pwd)

            f = open(pwd + "SeAPI/tempSatInfo.txt", "w")
            f.close()

            tempStr = 'python3 ' + pwd + 'SeAPI/z3formula.py >> ' + pwd + 'SeAPI/tempSatInfo.txt'
            os.system(tempStr)

            # listOfPaths.append(list_of_path[i])

            f = open(pwd + "SeAPI/tempSatInfo.txt", "r")
            lines = f.readlines()
            f.close()


            print("Path", i+1, ":", list_of_path[i])
            print("VC"+str(i+1)+" :", vc)
            if len(lines) > 0:
                if lines[0].strip() == "looksgood":
                    print("Satisfiability :\tsat")
                elif lines[0].strip() == "cannotsay":
                    print("Satisfiability :\tviolation")
            else:
                print("No Z3Output Given For the VC of This Path by SeApi!!!")
            print("")


            # if len(lines) > 0:
            #     listOfSatisfiability.append(lines[0].strip())
            # else:
            #     listOfSatisfiability.append("NoZ3OutputGivenForThisPath")
            #     # print("\t!!!!!!! Problem in SE API, No Z3 Output Given For This SE Path :", path)
        # clearing this file
        f = open(pwd + "SeAPI/tempSatInfo.txt", "w")
        f.close()

        # return listOfPaths, listOfSatisfiability
        return linesOfCode, len(list_of_path)