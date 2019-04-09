from z3 import *

from McNode import McNode
from WpcStringConverter import WpcStringConverter


class McUtility():

    def __init__(self, cfg, wpcGenerator, predicateVarSet):
        self.cfg = cfg
        self.helper = wpcGenerator.helper
        self.wpcGenerator = wpcGenerator
        self.allVar = predicateVarSet


    def execute(self, predicateList):
        self.preExecute()
        for i in range(len(predicateList)):
            self.generateWpcStringForAPredicate(predicateList[i], i)
        for i in range(len(predicateList)):
            self.generateBooleanVariableForAPredicate(predicateList[i], i)



    def preExecute(self):
        for nodeId in self.cfg.nodes:
            self.allVar = self.allVar.union(self.cfg.nodes[nodeId].variableSet)

    def generateWpcStringForAPredicate(self, predicate, predicateIndex):
        for nodeId in self.cfg.nodes:
            self.wpcStringForANode(nodeId, predicate, predicateIndex)
        self.allVar = self.allVar.union(self.wpcGenerator.variablesForZ3)

    def wpcStringForANode(self, nodeId, predicate, predicateIndex):
        temp = self.wpcGenerator.updateWpcStringByReplacing(predicate, self.cfg.nodes[nodeId]).strip()
        self.cfg.nodes[nodeId].wpcString[predicateIndex] = temp

    def generateBooleanVariableForAPredicate(self, predicate, predicateIndex):
        for nodeId in self.cfg.nodes:
            self.booleanVariableForANode(nodeId, predicate, predicateIndex)

    def booleanVariableForANode(self, nodeId, predicate, predicateIndex):
        wpcString = self.cfg.nodes[nodeId].wpcString[predicateIndex]
        if predicate == wpcString:
            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["skip"]
        else:
            brackettedString = "( ( " + wpcString + " ) ==> ( " + predicate + " ) )"
            brackettedString = brackettedString.replace("  ", " ")
            brackettedString = brackettedString.replace(" = ", " == ")
            z3StringConvertorObj = WpcStringConverter(brackettedString)
            z3StringConvertorObj.execute()
            result = self.z3SolverVaribleDeclaration(z3StringConvertorObj)

            brackettedString2 = "( ( " + wpcString + " ) ==> ( ! ( " + predicate + " ) ) )"
            brackettedString2 = brackettedString2.replace("  ", " ")
            brackettedString2 = brackettedString2.replace(" = ", " == ")
            z3StringConvertorObj2 = WpcStringConverter(brackettedString2)
            z3StringConvertorObj2.execute()
            result2 = self.z3SolverVaribleDeclaration(z3StringConvertorObj2)

            if result == "looksgood":
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["True"]
            elif result2 == "looksgood":
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["False"]
            elif result == "cannotsay":
                self.statementWiseBooleanVariableForANode(nodeId, predicateIndex)


    def z3SolverVaribleDeclaration(self, z3StringConvertorObj):
        for i in self.allVar:
            exec("%s=%s" % (i, "Real(\'" + i + "\')"))
        z3SolverObj = Solver()
        if len(z3StringConvertorObj.implies_p) > 0:
            for i in range(len(z3StringConvertorObj.implies_p)):
                exec("%s" % ("z3SolverObj.add(" + z3StringConvertorObj.implies_p[i] + ")"))
                if not z3StringConvertorObj.convertedWpc == z3StringConvertorObj.implies_p_q[i]:
                    exec("%s" % ("z3SolverObj.add(" + z3StringConvertorObj.implies_p_q[i] + ")"))
        exec("%s" % ("z3SolverObj.add( Not(" + z3StringConvertorObj.convertedWpc + ") )"))
        satisfiability = str(z3SolverObj.check())
        if satisfiability == "unsat":
            return "looksgood"
        elif satisfiability == "sat":
            return "cannotsay"



    def statementWiseBooleanVariableForANode(self, nodeId, predicateIndex):
        currentNode = self.cfg.nodes[nodeId]
        if len(currentNode.variableLHS) > 0:
            if self.helper.getRuleName(currentNode.ctx) == "assignment_statement":  # strictly assignment_statement
                for i in currentNode.variableLHS:
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "update_statement":    # Database UPDATE statement
                isWherePresent = False
                isNullPresentInWhere = False
                whereCondition = ""
                for i in range(currentNode.ctx.getChildCount()):        # finding "where_clause"...
                    if currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "where_clause":
                        isWherePresent = True
                        if self.wpcGenerator.nullInCondition(currentNode.ctx.children[i].children[1]):
                            isNullPresentInWhere = True
                        else:
                            whereCondition = self.wpcGenerator.getConditionalString(currentNode.ctx.children[i].children[1])
                            # print("@@@@@@@ update_statement whereCondition :", whereCondition)
                        break
                if isWherePresent:
                    if isNullPresentInWhere:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                    else:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
                else:
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "select_statement":  # Database SELECT statement
                # Note: we will not enter here if currentNode.variableLHS set is empty. See outer if condition.
                tempNode = currentNode.ctx.children[0].children[0]
                # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
                whereCondition = ""
                conditionInFromClause = ""
                isWherePresent = False
                isNullPresentInWhere = False
                for i in range(tempNode.getChildCount()):
                    if tempNode.children[i].getChildCount() > 0:
                        if self.helper.getRuleName(tempNode.children[i]) == "from_clause":
                            conditionInFromClause = self.wpcGenerator.extractConditionsInFromClause(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                            isWherePresent = True
                            if self.wpcGenerator.nullInCondition(tempNode.children[i].children[1]):
                                isNullPresentInWhere = True
                            else:
                                whereCondition = self.wpcGenerator.getConditionalString(tempNode.children[i].children[1])
                                # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                        else:
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
                else:
                    if conditionInFromClause == "":
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                    else:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
            elif self.helper.getRuleName(currentNode.ctx) == "insert_statement":  # Database INSERT statement
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "fetch_statement":    # Database FETCH statement
                for i in currentNode.variableLHS:
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "cursor_declaration":  # Database CURSOR statement
                whereCondition = ""
                conditionInFromClause = ""
                isWherePresent = False
                isNullPresentInWhere = False
                for i in range(currentNode.ctx.getChildCount()):
                    if self.helper.getRuleName(currentNode.ctx.children[i]) == "select_statement":
                        tempCtx = currentNode.ctx.children[i].children[0].children[0]
                        for j in range(tempCtx.getChildCount()):
                            if self.helper.getRuleName(tempCtx.children[j]) == "from_clause":
                                conditionInFromClause = self.wpcGenerator.extractConditionsInFromClause(tempCtx.children[j].children[1])
                                # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                            elif self.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                                isWherePresent = True
                                if self.wpcGenerator.nullInCondition(tempCtx.children[j].children[1]):
                                    isNullPresentInWhere = True
                                else:
                                    whereCondition = self.wpcGenerator.getConditionalString(tempCtx.children[j].children[1])
                                    # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                        else:
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
                else:
                    if conditionInFromClause == "":
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                    else:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
