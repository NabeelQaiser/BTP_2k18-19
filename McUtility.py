from z3 import *

from WpcStringConverter import WpcStringConverter


class McUtility():

    def __init__(self, cfg, wpcGenerator, predicateVarSet):
        self.cfg = cfg
        self.helper = wpcGenerator.helper
        self.wpcGenerator = wpcGenerator
        self.allVar = predicateVarSet

    def execute(self):
        self.preExecute()



    def preExecute(self):
        for nodeId in self.cfg.nodes:
            self.allVar = self.allVar.union(self.cfg.nodes[nodeId].variableSet)

    def generateWpcStringForAPredicate(self, predicate, predicateIndex):
        for nodeId in self.cfg.nodes:
            self.wpcStringForANode(nodeId, predicate, predicateIndex)

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
                z3SolverObj.add(z3StringConvertorObj.implies_p[i])
                if not z3StringConvertorObj.convertedWpc == z3StringConvertorObj.implies_p_q[i]:
                    z3SolverObj.add(z3StringConvertorObj.implies_p_q[i])
        z3SolverObj.add(Not(z3StringConvertorObj.convertedWpc))
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
                whereClausePosition = -1
                whereCondition = ""
                for i in range(currentNode.ctx.getChildCount()):        # finding "where_clause"...
                    if currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "where_clause":
                        whereClausePosition = i
                        whereCondition = self.wpcGenerator.getConditionalString(currentNode.ctx.children[i].children[1])
                        # print("@@@@@@@ update_statement whereCondition :", whereCondition)
                        break
                if not whereClausePosition == -1:   # whereCondition exists
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
                else:       # whereCondition does not exist...so, no merging like 'if' block...
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "select_statement":  # Database SELECT statement
                # Note: we will not enter here if currentNode.variableLHS set is empty. See outer if condition.
                tempNode = currentNode.ctx.children[0].children[0]
                conditionInFromClause = ""
                # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
                trueWpcString = ""
                into_flag = -1
                whereHandled_flag = False
                for i in range(tempNode.getChildCount()):
                    if tempNode.children[i].getChildCount() > 0:
                        if self.helper.getRuleName(tempNode.children[i]) == "from_clause":
                            conditionInFromClause = self.wpcGenerator.extractConditionsInFromClause(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                            whereCondition = self.wpcGenerator.getConditionalString(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                            if not conditionInFromClause == "":     # merging condition from WHERE and FROM_CLAUSE
                                whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                            whereHandled_flag = True
                if whereHandled_flag is False and into_flag > -1:
                    # BUT, don't relax, condition from FROM_CLAUSE may not be empty!!!
                    if not conditionInFromClause == "":
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
                    else:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                elif whereHandled_flag is True and into_flag > -1:
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
            elif self.helper.getRuleName(currentNode.ctx) == "insert_statement":  # Database INSERT statement
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "fetch_statement":    # Database FETCH statement
                for i in currentNode.variableLHS:
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
            elif self.helper.getRuleName(currentNode.ctx) == "cursor_declaration":  # Database CURSOR statement
                lhsVar = ""
                rhsVar = ""
                # whereCondition = ""
                # conditionInFromClause = ""
                # isWherePresent = False
                # isNullPresentInWhere = False
                # for i in range(currentNode.ctx.getChildCount()):
                #     if self.helper.getRuleName(currentNode.ctx.children[i]) == "cursor_name":
                #         lhsVar = currentNode.ctx.children[i].getText().strip()
                #     elif self.helper.getRuleName(currentNode.ctx.children[i]) == "select_statement":
                #         tempCtx = currentNode.ctx.children[i].children[0].children[0]
                #         for j in range(tempCtx.getChildCount()):
                #             if self.helper.getRuleName(tempCtx.children[j]) == "from_clause":
                #                 conditionInFromClause = self.extractConditionsInFromClause(tempCtx.children[j].children[1])
                #                 # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                #             elif self.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                #                 isWherePresent = True
                #                 if self.nullInCondition(tempCtx.children[j].children[1]):
                #                     isNullPresentInWhere = True
                #                 else:
                #                     whereCondition = self.getConditionalString(tempCtx.children[j].children[1])
                #                     # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                #         # BUT what to do if there are multiple SELECTION attributes here???...as per datasets assuming single attribute...
                #         varString = self.ssaString.getTerminal(tempCtx.children[1]).strip()
                #         rhsVar = self.getVariableForAggregateFunctionInSelect(varString)
                # if not(lhsVar == "") and not(rhsVar == ""):
                #     newWpcString = wpcString
                #     newWpcString = newWpcString.replace(" " + lhsVar + " ", " " + rhsVar + " ")
                #     if isWherePresent:
                #         if isNullPresentInWhere:
                #             if conditionInFromClause == "":
                #                 wpcString = "( " + newWpcString + " v " + wpcString + " )"
                #             else:
                #                 wpcString = "( ( " + conditionInFromClause + " ^ " + newWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
                #         else:
                #             if not conditionInFromClause == "":
                #                 whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                #             wpcString = "( ( " + whereCondition + " ^ " + newWpcString + " ) v ( ( ! " + whereCondition + " ) ^ " + wpcString + " ) )"
                #     else:
                #         if conditionInFromClause == "":
                #             wpcString = newWpcString
                #         else:
                #             wpcString = "( ( " + conditionInFromClause + " ^ " + newWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
        return ""

