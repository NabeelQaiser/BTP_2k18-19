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

class McSsaForBooleanVc():

    def __init__(self):
        self.helper = None
        self.cfg = None
        self.variablesForZ3 = set()

    # returns versionizedPredicateList, versionizedVarSet, versionizedConsequentList
    def execute(self, toVersionizeList, rawPredicateContentDict, sqlTableInfo, originalRawPredList):
        smartList = list()      # analogous to toVersionizeList, format : [ [x], ..., [y, y+1], ..., [z, z+1] ]
        sqlFileStr = self.generateBooleanVcPlsqlFileString(toVersionizeList, rawPredicateContentDict, originalRawPredList, smartList)

        file = open('mc/boolean_vc_plsql_file.sql', "w")
        file.write(sqlFileStr)
        file.close()

        input = FileStream('mc/boolean_vc_plsql_file.sql')
        lexer = PlSqlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = PlSqlParser(stream)
        tree = parser.sql_script()

        cfg = MyCFG()
        self.cfg = cfg
        helper = MyHelper(parser)
        self.helper = helper

        self.helper.updateTableDict(sqlTableInfo)
        utility = MyUtility(self.helper)
        v = MyVisitor(parser, self.cfg, utility)
        v.visit(tree)

        res = MyRawCfgToGraph(v.rawCFG, self.cfg)
        res.execute()
        utility.generateDomSet(self.cfg)
        utility.generateSDomSet(self.cfg)
        utility.generatIDom(self.cfg)
        utility.generateDFSet(self.cfg)
        utility.insertPhiNode(self.cfg)

        utility.initialiseVersinosedPhiNode(self.cfg)
        utility.versioniseVariable(self.cfg)
        utility.phiDestruction(self.cfg)

        ssaStringObj = MySsaStringGenerator(self.cfg, parser)
        ssaStringObj.execute()

        # print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')
        # for nodeId in self.cfg.nodes:
        #     self.cfg.nodes[nodeId].printPretty()
        # print('{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{')

        versionizedPredicateList = self.processSmartList(smartList, rawPredicateContentDict, toVersionizeList)
        # last element of smartList will be versionized ConsequentList node ids
        nodeList = smartList[len(smartList)-1]
        versionizedConsequentList = list()
        for i in nodeList:
            tempCond = self.getEquivalentPredicateForANode(i).strip()
            versionizedConsequentList.append(tempCond)
        return versionizedPredicateList, self.variablesForZ3, versionizedConsequentList


    def processSmartList(self, smartList, rawPredicateContentDict, toVersionizeList):
        versionizedPredicateList = list()
        for i in range(len(smartList)-1):
            equivalentCondition = ""
            tempList = rawPredicateContentDict[toVersionizeList[i]]
            nodeList = smartList[i]
            if len(tempList) == 2:
                equivalentCondition = self.getEquivalentPredicateForANode(nodeList[0]).strip()
            elif len(tempList) == 3:
                phi = self.getEquivalentPredicateForANode(nodeList[0]).strip()
                bool = self.getEquivalentPredicateForANode(nodeList[1]).strip()
                equivalentCondition = "( ( ( " + phi + " ) ^ ( " + bool + " ) ) v ( ( " + phi + " ) ^ ( ! ( " + bool + " ) ) ) v ( ( ! ( " + phi + " ) ) ^ ( " + bool + " ) ) )"
            versionizedPredicateList.append(equivalentCondition)
        return versionizedPredicateList



    def generateBooleanVcPlsqlFileString(self, toVersionizeList, rawPredicateContentDict, originalRawPredList, smartList):
        sqlFileStr = "CREATE OR REPLACE PROCEDURE TEST(STAY_AWAY_FROM_IT IN VARCHAR)\nIS\nBEGIN\n\n"
        counter = 2
        for predIndex in toVersionizeList:
            tempList = rawPredicateContentDict[predIndex]
            flagList = list()
            if len(tempList) == 2:
                if tempList[1] == "cond":
                    sqlFileStr = sqlFileStr + "\tASSUME " + tempList[0].strip() + ";\n\n"
                    flagList.append(counter)
                    counter = counter + 1
                elif tempList[1] == "ass":
                    sqlFileStr = sqlFileStr + "\t" + self.cursorToSelectStmt(tempList[0].strip()) + ";\n\n"
                    flagList.append(counter)
                    counter = counter + 1
            elif len(tempList) == 3:
                if tempList[1] == "cond":
                    sqlFileStr = sqlFileStr + "\tASSUME " + tempList[2].strip() + ";\n"
                    flagList.append(counter)
                    counter = counter + 1
                    sqlFileStr = sqlFileStr + "\tASSUME " + tempList[0].strip() + ";\n\n"
                    flagList.append(counter)
                    counter = counter + 1
                elif tempList[1] == "ass":
                    sqlFileStr = sqlFileStr + "\tASSUME " + tempList[2].strip() + ";\n"
                    flagList.append(counter)
                    counter = counter + 1
                    sqlFileStr = sqlFileStr + "\t" + self.cursorToSelectStmt(tempList[0].strip()) + ";\n\n"
                    flagList.append(counter)
                    counter = counter + 1
            smartList.append(flagList)
        flagList = list()
        for pred in originalRawPredList:
            sqlFileStr = sqlFileStr + "\tASSERT " + pred.strip() + ";\n"
            flagList.append(counter)
            counter = counter + 1
        smartList.append(flagList)
        sqlFileStr = sqlFileStr + "\nEND;"
        return sqlFileStr


    def cursorToSelectStmt(self, cStr):
        tokens = cStr.split(" ")
        if tokens[0] == "CURSOR":
            fromIndexCursor = -1
            for i in range(len(tokens)):
                if tokens[i] == "SELECT":
                    fromIndexCursor = i
                    break
            selectStr = ""
            for i in range(fromIndexCursor, len(tokens)-1):
                if tokens[i] == "FROM":
                    selectStr = selectStr + "INTO " + tokens[1] + " FROM "
                else:
                    selectStr = selectStr + tokens[i] + " "
            return selectStr.strip()
        else:
            return cStr


    def getEquivalentPredicateForANode(self, nodeId):
        currentNode = self.cfg.nodes[nodeId]
        ruleName = self.helper.getRuleName(currentNode.ctx).strip()
        equivalentCondition = ""
        if ruleName == "assignment_statement":
            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
            # DON'T expect more...
            varString = self.getVersionedTerminalRHS(nodeId, currentNode.ctx.children[2], self.cfg).strip()
            varString = varString.replace("( )", "")
            varString = varString.replace("  ", " ").strip()
            rhsVar = "( " + varString + " )"
            if not varString == "":
                equivalentCondition = "( " + self.getVersionedTerminalLHS(nodeId, currentNode.ctx.children[0], self.cfg).strip() + " == " + rhsVar + " )"
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "update_statement":
            for i in range(currentNode.ctx.getChildCount()):
                # finding "update_set_clause"...
                if currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "update_set_clause":
                    updateSetCtx = currentNode.ctx.children[i]
                    for j in range(updateSetCtx.getChildCount()):
                        # finding "column_based_update_set_clause"...
                        if updateSetCtx.children[j].getChildCount() > 1 and self.helper.getRuleName(updateSetCtx.children[j]) == "column_based_update_set_clause":
                            lhsVar = self.getVersionedTerminalLHS(nodeId, updateSetCtx.children[j].children[0], self.cfg).strip()
                            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                            # DON'T expect more...
                            varString = self.getVersionedTerminalRHS(nodeId, updateSetCtx.children[j].children[2], self.cfg).strip()
                            varString = varString.replace("( )", "")
                            varString = varString.replace("  ", " ").strip()
                            rhsVar = " ( " + varString + " ) "
                            if not varString == "":
                                if equivalentCondition == "":
                                    equivalentCondition = "( " + lhsVar + " == " + rhsVar + " )"
                                else:
                                    equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                # finding "where_clause"...
                elif currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "where_clause":
                    if not self.nullInCondition(currentNode.ctx.children[i].children[1]):
                        whereCondition = self.getConditionalString(nodeId, currentNode.ctx.children[i].children[1]).strip()
                        equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + whereCondition + " ) )"
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "insert_statement":  # assuming Attributes in which data is to be inserted is mentioned with Tablename
            tempNode = currentNode.ctx.children[1]  # single_table_insert
            myLHS = []
            myRHS = []
            count = tempNode.children[0].getChildCount()  # inset_into_clause
            if count > 2:
                i = 2
                while i < count:
                    if tempNode.children[0].children[i].getChildCount() > 0:
                        myLHS.append(self.getVersionedTerminalLHS(nodeId, tempNode.children[0].children[i], self.cfg).strip())
                    i = i + 1
            count = tempNode.children[1].children[1].getChildCount()  # expression_list
            i = 0
            while i < count:
                node = tempNode.children[1].children[1].children[i]
                if node.getChildCount() > 0:
                    myRHS.append(self.getVersionedTerminalRHS(nodeId, node, self.cfg).strip())
                i = i + 1
            if len(myLHS) > 0:
                for i in range(len(myLHS)):
                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                    # DON'T expect more...
                    varString = myRHS[i]
                    varString = varString.replace("( )", "")
                    varString = varString.replace("  ", " ").strip()
                    rhsVar = "( " + varString + " )"
                    if not varString == "":
                        if equivalentCondition == "":
                            equivalentCondition = "( " + myLHS[i] + " == " + rhsVar + " )"
                        else:
                            equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + myLHS[i] + " == " + rhsVar + " ) )"
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "select_statement":
            tempNode = currentNode.ctx.children[0].children[0]
            myRHS = []
            myLHS = []
            conditionInFromClause = ""
            # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
            into_flag = -1
            whereHandled_flag = False
            for i in range(tempNode.getChildCount()):
                if tempNode.children[i].getChildCount() > 0:
                    if self.helper.getRuleName(tempNode.children[i]) == "selected_element":
                        varString = self.getVersionedTerminalRHS(nodeId, tempNode.children[i], self.cfg).strip()
                        myRHS.append(self.getVariableForAggregateFunctionInSelect(varString))  # <--- RHS
                    elif self.helper.getRuleName(tempNode.children[i]) == "into_clause":
                        into_flag = i
                        intoNode = tempNode.children[i]
                        for x in range(intoNode.getChildCount()):
                            if intoNode.children[x].getChildCount() > 0 and self.helper.getRuleName(
                                    intoNode.children[x]) == "variable_name":
                                myLHS.append(self.getVersionedTerminalLHS(nodeId, intoNode.children[x], self.cfg).strip())  # <--- LHS
                    elif self.helper.getRuleName(tempNode.children[i]) == "from_clause":
                        conditionInFromClause = self.extractConditionsInFromClause(nodeId, tempNode.children[i].children[1])
                        # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                    elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                        # myLHS & myRHS & conditionInFromClause will be already filled here if they should be
                        whereCondition = self.getConditionalString(nodeId, tempNode.children[i].children[1])
                        # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                        if not conditionInFromClause == "":  # merging condition from WHERE and FROM_CLAUSE
                            whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                        whereHandled_flag = True
                        if into_flag > -1:
                            for j in range(len(myLHS)):
                                if equivalentCondition == "":
                                    equivalentCondition = "( " + myLHS[j] + " == " + myRHS[j] + " )"
                                else:
                                    equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + myLHS[j] + " == " + myRHS[j] + " ) )"
                                # also add RHS vars to variablesForZ3 set
                                self.variablesForZ3.add(myRHS[j])  # <<<-----------<<<---------------<<<-------------
                            if self.nullInCondition(tempNode.children[i].children[1]):  # NULL +nt in where_condition
                                if not conditionInFromClause == "":
                                    equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + conditionInFromClause + " ) )"
                            else:  # NULL not +nt in where_condition
                                equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + whereCondition + " ) )"
            if whereHandled_flag is False and into_flag > -1:
                # whereCondition do not exist in SELECT
                for i in range(len(myLHS)):
                    if equivalentCondition == "":
                        equivalentCondition = "( " + myLHS[i] + " == " + myRHS[i] + " )"
                    else:
                        equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + myLHS[i] + " == " + myRHS[i] + " ) )"
                    # also add RHS vars to variablesForZ3 set
                    self.variablesForZ3.add(myRHS[i])  # <<<-----------<<<---------------<<<-------------
                # BUT, don't relax, condition from FROM_CLAUSE may not be empty!!!
                if not conditionInFromClause == "":
                    equivalentCondition = "( ( " + equivalentCondition + " ) ^ ( " + conditionInFromClause + " ) )"
            # also add every versioned var to variablesForZ3 set, be tension free...
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "cursor_declaration":
            lhsVar = ""
            rhsVar = ""
            whereCondition = ""
            conditionInFromClause = ""
            isWherePresent = False
            isNullPresentInWhere = False
            for i in range(currentNode.ctx.getChildCount()):
                if self.helper.getRuleName(currentNode.ctx.children[i]) == "cursor_name":
                    lhsVar = self.getVersionedTerminalLHS(nodeId, currentNode.ctx.children[i], self.cfg).strip()
                elif self.helper.getRuleName(currentNode.ctx.children[i]) == "select_statement":
                    tempCtx = currentNode.ctx.children[i].children[0].children[0]
                    for j in range(tempCtx.getChildCount()):
                        if self.helper.getRuleName(tempCtx.children[j]) == "from_clause":
                            conditionInFromClause = self.extractConditionsInFromClause(nodeId, tempCtx.children[j].children[1])
                            # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                            isWherePresent = True
                            if self.nullInCondition(tempCtx.children[j].children[1]):
                                isNullPresentInWhere = True
                            else:
                                whereCondition = self.getConditionalString(nodeId, tempCtx.children[j].children[1])
                                # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                    # BUT what to do if there are multiple SELECTION attributes here???...as per datasets assuming single attribute...
                    varString = self.getVersionedTerminalRHS(nodeId, tempCtx.children[1], self.cfg).strip()
                    rhsVar = self.getVariableForAggregateFunctionInSelect(varString)
            if not (lhsVar == "") and not (rhsVar == ""):
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            equivalentCondition = "( " + lhsVar + " == " + rhsVar + " )"
                        else:
                            equivalentCondition = "( ( " + conditionInFromClause + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = "( ( " + conditionInFromClause + " ) ^ ( " + whereCondition + " ) )"
                        equivalentCondition = "( ( " + whereCondition + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                else:
                    if not conditionInFromClause == "":
                        equivalentCondition = "( ( " + conditionInFromClause + " ) ^ ( " + lhsVar + " == " + rhsVar + " ) )"
                    else:
                        equivalentCondition = "( " + lhsVar + " == " + rhsVar + " )"
            # also add every RHS var to variablesForZ3 set
            self.variablesForZ3.add(rhsVar)  # <<<-----------<<<---------------<<<-------------
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "fetch_statement":
            equivalentCondition = "( ( " + self.getVersionedTerminalLHS(nodeId, currentNode.ctx.children[3], self.cfg).strip() + " ) == ( " + self.getVersionedTerminalRHS(nodeId, currentNode.ctx.children[1], self.cfg).strip() + " ) )"
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "assume_statement":
            equivalentCondition = self.getConditionalString(nodeId, currentNode.ctx.children[1])
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))
        elif ruleName == "assert_statement":
            equivalentCondition = self.getConditionalString(nodeId, currentNode.ctx.children[1])
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedLHS.values()))
            self.variablesForZ3 = self.variablesForZ3.union(set(currentNode.versionedRHS.values()))

        equivalentCondition = equivalentCondition.replace("  ", " ")
        equivalentCondition = equivalentCondition.replace(" = ", " == ").strip()
        return equivalentCondition



    def getVersionedTerminalRHS(self, nodeId, ctx, cfg):
        c = ctx.getChildCount()
        if c == 0:
            if ctx.getText() in cfg.nodes[nodeId].versionedRHS.keys():
                return cfg.nodes[nodeId].versionedRHS[ctx.getText()] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[i], cfg)
            return res

    def getVersionedTerminalLHS(self, nodeId, ctx, cfg):
        c = ctx.getChildCount()
        if c == 0:
            if str(ctx) in cfg.nodes[nodeId].versionedLHS.keys():
                return cfg.nodes[nodeId].versionedLHS[str(ctx)] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[i], cfg)
            return res


    def getVariableForAggregateFunctionInSelect(self, varString):
        varString = varString.replace("(", "")
        varString = varString.replace(")", "")
        varString = varString.replace(",", "")
        varString = varString.strip()
        varString = varString.replace("  ", " ")
        varString = varString.replace(" ", "_")
        varString = varString.replace("*", "STAR")
        return varString

    # it will yeild versioned condition
    def getConditionalString(self, nodeId, ctx):   # considering only AND, OR, NOT as 'word' separator
        if ctx.getChildCount() == 1:
            return self.getConditionalString(nodeId, ctx.children[0])
        elif ctx.getChildCount() == 2:      # strictly for "NOT"
            if ctx.children[0].getText().strip() == "NOT":
                return "( ! " + self.getConditionalString(nodeId, ctx.children[1]) + " )"
        elif ctx.getChildCount() == 3:
            operators = ['=', '>', '<', '>=', '<=', '!=', '<>', '^=', '~=']
            if ctx.children[1].getText().strip() == "AND":  # conditions separated by "AND"
                return "( " + self.getConditionalString(nodeId, ctx.children[0]) + " ^ " + self.getConditionalString(nodeId, ctx.children[2]) + " )"
            elif ctx.children[1].getText().strip() == "OR":  # conditions separated by "OR"
                return "( " + self.getConditionalString(nodeId, ctx.children[0]) + " v " + self.getConditionalString(nodeId, ctx.children[2]) + " )"
            elif ctx.children[1].getText().strip() in operators:
                return "( " + self.getVersionedTerminalRHS(nodeId, ctx, self.cfg).strip() + " )"
            else:
                return self.getConditionalString(nodeId, ctx.children[1])
        elif ctx.getChildCount() == 5:  # For "XX BETWEEN 10 AND 50"
            if self.getVersionedTerminalRHS(nodeId, ctx.children[1], self.cfg).strip() == "BETWEEN":
                referenceVar = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[0], self.cfg).strip() + " )"
                leftBoundary = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[2], self.cfg).strip() + " )"
                rightBoundary = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[4], self.cfg).strip() + " )"
                return "( ( " + referenceVar + " > " + leftBoundary + " ) ^ ( " + referenceVar + " < " + rightBoundary + " ) )"
            elif self.getVersionedTerminalRHS(nodeId, ctx.children[1], self.cfg).strip() == "IN":  # For "XX IN ( select_subquery )"
                leftVar = self.getVersionedTerminalRHS(nodeId, ctx.children[0], self.cfg).strip()
                selectQueryCtx = ctx.children[3].children[0]
                rightVar = self.getVersionedTerminalRHS(nodeId, selectQueryCtx.children[1], self.cfg).strip()
                isWhereCondition = False
                isNullInCondition = False
                condition = ""
                for m in range(selectQueryCtx.getChildCount()):
                    if self.helper.getRuleName(selectQueryCtx.children[m]) == "where_clause":
                        isWhereCondition = True
                        if self.nullInCondition(selectQueryCtx.children[m].children[1]):
                            isNullInCondition = True
                        else:
                            condition = self.getConditionalString(nodeId, selectQueryCtx.children[m].children[1])
                if isWhereCondition:
                    if isNullInCondition:
                        return "( " + leftVar + " = " + rightVar + " )"
                    else:
                        return "( ( " + leftVar + " = " + rightVar + " ) ^ ( " + condition + " ) )"
                else:
                    return "( " + leftVar + " = " + rightVar + " )"
            return ""
        elif ctx.getChildCount() == 6:  # For "XX NOT BETWEEN 10 AND 50"
            if self.getVersionedTerminalRHS(nodeId, ctx.children[2], self.cfg).strip() == "BETWEEN":
                referenceVar = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[0], self.cfg).strip() + " )"
                leftBoundary = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[3], self.cfg).strip() + " )"
                rightBoundary = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[5], self.cfg).strip() + " )"
                return "( ( " + referenceVar + " < " + leftBoundary + " ) v ( " + referenceVar + " > " + rightBoundary + " ) )"
            elif self.getVersionedTerminalRHS(nodeId, ctx.children[2], self.cfg).strip() == "IN":  # For "XX NOT IN ( select_subquery )"
                leftVar = self.getVersionedTerminalRHS(nodeId, ctx.children[0], self.cfg).strip()
                selectQueryCtx = ctx.children[4].children[0]
                rightVar = self.getVersionedTerminalRHS(nodeId, selectQueryCtx.children[1], self.cfg).strip()
                isWhereCondition = False
                isNullInCondition = False
                condition = ""
                for m in range(selectQueryCtx.getChildCount()):
                    if self.helper.getRuleName(selectQueryCtx.children[m]) == "where_clause":
                        isWhereCondition = True
                        if self.nullInCondition(selectQueryCtx.children[m].children[1]):
                            isNullInCondition = True
                        else:
                            condition = self.getConditionalString(nodeId, selectQueryCtx.children[m].children[1])
                if isWhereCondition:
                    if isNullInCondition:
                        return "( ! ( " + leftVar + " = " + rightVar + " ) )"
                    else:
                        return "( ( ! ( " + leftVar + " = " + rightVar + " ) ) ^ ( " + condition + " ) )"
                else:
                    return "( ! ( " + leftVar + " = " + rightVar + " ) )"
            return ""
        elif ctx.getChildCount() == 0:      # for stmts like "UPDATE --blah blah-- WHERE SingleWord;"
            return "( " + self.getVersionedTerminalRHS(nodeId, ctx, self.cfg).strip() + " )"


    # it will yeild versioned condition
    def extractConditionsInFromClause(self, nodeId, ctx):       # ctx ~ from_clause.children[1]
        if self.helper.getRuleName(ctx) == "table_ref":
            if ctx.getChildCount() == 2:
                leftCondition = self.extractConditionsInFromClause(nodeId, ctx.children[0])
                rightCondition = self.extractConditionsInFromClause(nodeId, ctx.children[1])
                if leftCondition == "" and rightCondition == "":
                    return ""
                elif leftCondition == "":
                    return rightCondition
                elif rightCondition == "":
                    return leftCondition
                else:
                    return "( " + leftCondition + " ^ " + rightCondition + " )"
            elif ctx.getChildCount() == 1:
                # one can get Table Name from here...
                notImportant = "notImportant"
                return ""
        elif self.helper.getRuleName(ctx) == "join_clause":
            condition = ""
            for i in range(ctx.getChildCount()):
                if self.helper.getRuleName(ctx.children[i]) == "table_ref":
                    # one can get Table Name from here...
                    notImportant = "notImportant"
                elif self.helper.getRuleName(ctx.children[i]) == "join_on_part":
                    condition = self.getConditionalString(nodeId, ctx.children[i].children[1].children[0])
            return condition


    def nullInCondition(self, conditionalCtx):
        condition = self.getTerminal(conditionalCtx).strip()
        tokens = condition.split(" ")   # tokens will be a list
        if "NULL" in tokens:
            return True
        return False


    def getTerminal(self, ctx):
        if ctx==None:
            return ""
        c = ctx.getChildCount()
        if c==0:
            return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getTerminal(ctx.children[i])
            return res
