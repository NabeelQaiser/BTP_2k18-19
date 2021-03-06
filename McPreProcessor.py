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


class McPreProcessor:

    def __init__(self, fileSpec, fileData):
        self.fileSpec = fileSpec
        self.fileData = fileData

    def getSpec(self):
        with open(self.fileSpec, 'r') as f:
            lines = f.readlines()
            tableInfo = dict()      # format : {'tableName': [(attr, nullity), (attr, nullity), ...]}
            predicates = []        # list of strings
            isEnd = False
            for line in lines:
                if not isEnd:
                    line = line.upper()
                    line = line.strip()
                    tokens = line.split('::')
                    tokens[0] = tokens[0].strip()
                    if len(tokens[0]) > 0:
                        if tokens[0] == 'PREDICATES':
                            isEnd = True
                            predicates = tokens[1].strip().split(',')
                            for i in range(len(predicates)):
                                predicates[i] = predicates[i].strip()
                                predicates[i] = predicates[i].strip('(')
                                predicates[i] = predicates[i].strip(')')
                        else:
                            temp = []
                            attr = tokens[1].strip().split(',')
                            for i in range(len(attr)):
                                pair = (attr[i].split(':')[0].strip(), attr[i].split(':')[1].strip())
                                temp.append(pair)
                            tableInfo[tokens[0].strip()] = temp
                else:
                    break
            return tableInfo, predicates



    def start(self):
        tableInfo, predicates = self.getSpec()

        magicString = "CREATE OR REPLACE PROCEDURE TEST(X IN VARCHAR)\nIS\nBEGIN\n"
        for predicate in predicates:
            magicString = magicString + "\tASSUME " + predicate + ";\n"
        magicString = magicString + "\nEND;"
        file = open('mc/magic_file.sql', "w")
        file.write(magicString)
        file.close()

        input = FileStream('mc/magic_file.sql')
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

        res = MyRawCfgToGraph(v.rawCFG, cfg)
        res.execute()
        utility.generateVariableSet(cfg)

        ssaStringObj = MySsaStringGenerator(cfg, parser)
        wpcGeneratorObj = WpcGenerator(cfg, helper, ssaStringObj)

        newPredicates = []
        predicateVarSet = set()
        for nodeId in cfg.nodes:
            if helper.getRuleName(cfg.nodes[nodeId].ctx) == "assume_statement":
                assumeCondition = wpcGeneratorObj.getConditionalString(cfg.nodes[nodeId].ctx.children[1])
                assumeCondition = assumeCondition.replace("  ", " ").strip()
                newPredicates.append(assumeCondition)
                predicateVarSet = predicateVarSet.union(cfg.nodes[nodeId].variableSet)

        f = open(self.fileData, "r")
        content = f.read().upper()
        f.close()
        assumeConstraintString = "TO_CORRECT_PROBLEMS_IN_SE_API > 0"
        assertConstraintString = "TO_CORRECT_PROBLEMS_IN_SE_API > 0"
        temp = content.strip().split("BEGIN")
        result = ""
        result = result + temp[0] + "BEGIN\n\t" + "ASSUME " + assumeConstraintString + " ;\n" + temp[1]
        for i in range(2, len(temp)):
            result = result + "BEGIN" + temp[i]

        temp = result.strip().split("END")
        result = temp[0]
        for i in range(1, len(temp) - 1):
            result = result + "END" + temp[i]
        result = result + "ASSERT " + assertConstraintString + " ;\n\t" + "END" + temp[len(temp) - 1]

        return tableInfo, newPredicates, predicates, predicateVarSet, result        # newPredicates : in wpc format ; predicate : in plsql format
