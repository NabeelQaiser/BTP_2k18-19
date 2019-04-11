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


class SePathsInfoForMc():
    def __init__(self):
        pass

    def execute(self, data, spec):
        # data = "gen/data/" + argv[1]
        # spec = "specification/" + argv[2]
        processor = PreProcessor(spec, data)
        tableInfo, assume, assrt, resultString = processor.start()

        file = open('upper_input.sql', "w")
        file.write(resultString)
        file.close()

        input = FileStream('upper_input.sql')
        lexer = PlSqlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PlSqlParser(stream)
        tree = parser.sql_script()

        cfg = MyCFG()
        helper = MyHelper(parser)
        utility = MyUtility(helper)
        v = MyVisitor(parser, cfg, utility)
        v.visit(tree)

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

        utility.dfs(cfg.nodes[0].id, cfg)

        for nodeId in cfg.nodes:
            last_node = cfg.nodes[nodeId].id

        list_of_path = list(utility.dfs_path(cfg.nodes[0].id, last_node, cfg))


        vcs = SymbolicVcGeneration(cfg, parser)
        z3fr = z3formulaofvcs(cfg, parser)

        listOfPaths = []
        listOfSatisfiability = []
        for path in list_of_path:
            vc = vcs.SymbolicVc(path)
            variableset = z3fr.z3VariableDeclarationSet(path)
            z3fr.z3FormulaForEachPath(vc)

            f = open("tempSatInfo.txt", "w")
            f.close()
            os.system('python3 z3formula.py >> tempSatInfo.txt')
            listOfPaths.append(path)
            f = open("tempSatInfo.txt", "r")
            lines = f.readlines()
            listOfSatisfiability.append(lines[0].strip())

        return listOfPaths, listOfSatisfiability
