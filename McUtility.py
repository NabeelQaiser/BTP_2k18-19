from z3 import *

from McNode import McNode
from WpcStringConverter import WpcStringConverter


class McUtility():

    def __init__(self, cfg, wpcGenerator, predicateVarSet):
        self.cfg = cfg
        self.helper = wpcGenerator.helper
        self.wpcGenerator = wpcGenerator
        self.variablesForZ3 = set()
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
        self.allVar = self.allVar.union(self.variablesForZ3)

    def wpcStringForANode(self, nodeId, predicate, predicateIndex):
        # notImportant = self.wpcGenerator.updateWpcStringByReplacing(predicate, self.cfg.nodes[nodeId]).strip()
        temp = self.mcUpdateWpcStringByReplacing(predicate, self.cfg.nodes[nodeId]).strip()
        self.cfg.nodes[nodeId].wpcString[predicateIndex] = temp

    def generateBooleanVariableForAPredicate(self, predicate, predicateIndex):
        for nodeId in self.cfg.nodes:
            self.booleanVariableForANode(nodeId, predicate, predicateIndex)

    def generateBooleanVariableForAPath(self, predicates, path):
        for i in range(len(predicates)):
            for nodeId in path:
                self.wpcStringForANode(nodeId, predicates[i], i)
            for nodeId in path:
                self.booleanVariableForANode(nodeId, predicates[i], i)


    def booleanVariableForANode(self, nodeId, predicate, predicateIndex):
        # ruleName = self.helper.getRuleName(self.cfg.nodes[nodeId].ctx).strip()
        wpcString = self.cfg.nodes[nodeId].wpcString[predicateIndex]
        if predicateIndex in self.cfg.nodes[nodeId].booleans.keys() and self.cfg.nodes[nodeId].booleans[predicateIndex][0] == "True":
            pass
        elif self.cfg.nodes[nodeId].ctx is None:
            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["skip"]
        elif len(self.cfg.nodes[nodeId].next) > 1:
            if self.wpcGenerator.nullInCondition(self.cfg.nodes[nodeId].ctx):
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["skip"]
            else:
                condStr = self.wpcGenerator.getConditionalString(self.cfg.nodes[nodeId].ctx).strip()
                brackettedString = "( ( " + condStr + " ) ==> ( " + predicate + " ) )"
                brackettedString = brackettedString.replace("  ", " ")
                brackettedString = brackettedString.replace(" = ", " == ")
                z3StringConvertorObj = WpcStringConverter(brackettedString)
                z3StringConvertorObj.execute()
                result = self.z3SolverVaribleDeclaration(z3StringConvertorObj)

                if result == "looksgood":
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["True"]
                elif result == "cannotsay":
                    self.cfg.nodes[nodeId].booleans[predicateIndex] = ["skip"]
        elif predicate == wpcString:
            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["skip"]
        else:
            brackettedString = "( ( " + wpcString + " ) ==> ( " + predicate + " ) )"
            brackettedString = brackettedString.replace("  ", " ")
            brackettedString = brackettedString.replace(" = ", " == ")
            z3StringConvertorObj = WpcStringConverter(brackettedString)
            z3StringConvertorObj.execute()
            result = self.z3SolverVaribleDeclaration(z3StringConvertorObj)

            # brackettedString2 = "( ( " + wpcString + " ) ==> ( ! ( " + predicate + " ) ) )"
            # brackettedString2 = brackettedString2.replace("  ", " ")
            # brackettedString2 = brackettedString2.replace(" = ", " == ")
            # z3StringConvertorObj2 = WpcStringConverter(brackettedString2)
            # z3StringConvertorObj2.execute()
            # result2 = self.z3SolverVaribleDeclaration(z3StringConvertorObj2)

            if result == "looksgood":
                self.cfg.nodes[nodeId].booleans[predicateIndex] = ["True"]
            # elif result2 == "looksgood":
            #     self.cfg.nodes[nodeId].booleans[predicateIndex] = ["False"]
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
                            # whereCondition = self.wpcGenerator.getConditionalString(currentNode.ctx.children[i].children[1])
                            whereCondition = self.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[i].children[1]).strip()
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
                            conditionInFromClause = self.extractRawConditionsInFromClause(tempNode.children[i].children[1]).strip()
                            # conditionInFromClause = self.wpcGenerator.ssaString.getTerminal(tempNode.children[i].children[1]).strip()
                            # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                            isWherePresent = True
                            if self.wpcGenerator.nullInCondition(tempNode.children[i].children[1]):
                                isNullPresentInWhere = True
                            else:
                                # whereCondition = self.wpcGenerator.getConditionalString(tempNode.children[i].children[1])
                                whereCondition = self.wpcGenerator.ssaString.getTerminal(tempNode.children[i].children[1]).strip()
                                # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                        else:
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = conditionInFromClause + " AND " + whereCondition
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
                                conditionInFromClause = self.extractRawConditionsInFromClause(tempCtx.children[j].children[1]).strip()
                                # conditionInFromClause = self.wpcGenerator.ssaString.getTerminal(tempCtx.children[j].children[1]).strip()
                                # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                            elif self.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                                isWherePresent = True
                                if self.wpcGenerator.nullInCondition(tempCtx.children[j].children[1]):
                                    isNullPresentInWhere = True
                                else:
                                    # whereCondition = self.wpcGenerator.getConditionalString(tempCtx.children[j].children[1])
                                    whereCondition = self.wpcGenerator.ssaString.getTerminal(tempCtx.children[j].children[1]).strip()
                                    # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                if isWherePresent:
                    if isNullPresentInWhere:
                        if conditionInFromClause == "":
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                        else:
                            self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]
                    else:
                        if not conditionInFromClause == "":
                            whereCondition = conditionInFromClause + " AND " + whereCondition
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [whereCondition, "*", "True"]
                else:
                    if conditionInFromClause == "":
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = ["*"]
                    else:
                        self.cfg.nodes[nodeId].booleans[predicateIndex] = [conditionInFromClause, "*", "True"]



    # Recursive method to extract raw Conditions In From_Clause (SELECT, SELECT-IN-CURSOR)
    def extractRawConditionsInFromClause(self, ctx):  # ctx ~ from_clause.children[1]
        if self.helper.getRuleName(ctx) == "table_ref":
            if ctx.getChildCount() == 2:
                leftCondition = self.extractRawConditionsInFromClause(ctx.children[0])
                rightCondition = self.extractRawConditionsInFromClause(ctx.children[1])
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
                    condition = self.wpcGenerator.ssaString.getTerminal(ctx.children[i].children[1].children[0]).strip()
            return condition


    # -------------------------------------------------------------------------
    def mcUpdateWpcStringByReplacing(self, wpcString, currentNode):
        wpcString = wpcString.replace("  ", " ").strip()
        if len(currentNode.variableLHS) > 0:
            if self.helper.getRuleName(currentNode.ctx) == "assignment_statement":  # strictly assignment_statement
                for i in currentNode.variableLHS:
                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                    # DON'T expect more... do same for UPDATE, INSERT rhs...
                    varString = self.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[2]).strip()
                    varString = varString.replace("( )", "")
                    varString = varString.replace("  ", " ").strip()
                    replacedBy = "( " + varString + " )"
                    wpcString = wpcString.replace(" "+i.strip()+" ", " "+replacedBy+" ")
                # also add RHS vars to variablesForZ3 set
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
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
                    tempWpcString = wpcString
                    updateSetCtx = currentNode.ctx.children[whereClausePosition-1]
                    didOldWpcChanged = False
                    for i in range(updateSetCtx.getChildCount()):       # finding "column_based_update_set_clause"...
                        if updateSetCtx.children[i].getChildCount() > 1 and self.helper.getRuleName(updateSetCtx.children[i]) == "column_based_update_set_clause":
                            toBeReplaced = " " + updateSetCtx.children[i].children[0].getText().strip() + " "
                            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                            # DON'T expect more...
                            varString = self.wpcGenerator.ssaString.getTerminal(updateSetCtx.children[i].children[2]).strip()
                            varString = varString.replace("( )", "")
                            varString = varString.replace("  ", " ").strip()
                            replacedBy = " ( " + varString + " ) "
                            tempWpcString = tempWpcString.replace(toBeReplaced, replacedBy)
                            if not tempWpcString.strip() == wpcString.strip():
                                didOldWpcChanged = True
                    # now join 'true' and 'false' like 'if' block...
                    if didOldWpcChanged:
                        if self.wpcGenerator.nullInCondition(currentNode.ctx.children[whereClausePosition].children[1]):  # NULL +nt in condition
                            wpcString = "( " + tempWpcString + " v " + wpcString + " )"
                        else:  # NULL not +nt in condition
                            wpcString = "( ( " + whereCondition + " ^ " + tempWpcString + " ) v ( ( ! " + whereCondition + " ) ^ " + wpcString + " ) )"
                else:       # whereCondition does not exist...so, no merging like 'if' block...
                    for i in range(currentNode.ctx.getChildCount()):        # finding "update_set_clause"...
                        if currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "update_set_clause":
                            updateSetCtx = currentNode.ctx.children[i]
                            for j in range(updateSetCtx.getChildCount()):       # finding "column_based_update_set_clause"...
                                if updateSetCtx.children[j].getChildCount() > 1 and self.helper.getRuleName(updateSetCtx.children[j]) == "column_based_update_set_clause":
                                    toBeReplaced = " " + updateSetCtx.children[j].children[0].getText().strip() + " "
                                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                                    # DON'T expect more...
                                    varString = self.wpcGenerator.ssaString.getTerminal(updateSetCtx.children[j].children[2]).strip()
                                    varString = varString.replace("( )", "")
                                    varString = varString.replace("  ", " ").strip()
                                    replacedBy = " ( " + varString + " ) "
                                    wpcString = wpcString.replace(toBeReplaced, replacedBy)
                            break
                # also add RHS vars to variablesForZ3 set
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
            elif self.helper.getRuleName(currentNode.ctx) == "select_statement":  # Database SELECT statement
                # Note: we will not enter here if currentNode.variableLHS set is empty. See outer if condition.
                tempNode = currentNode.ctx.children[0].children[0]
                myRHS = []
                myLHS = []
                didOldWpcChanged = False
                conditionInFromClause = ""
                # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
                trueWpcString = ""
                into_flag = -1
                whereHandled_flag = False
                for i in range(tempNode.getChildCount()):
                    if tempNode.children[i].getChildCount() > 0:
                        if self.helper.getRuleName(tempNode.children[i]) == "selected_element":
                            varString = self.wpcGenerator.ssaString.getTerminal(tempNode.children[i]).strip()
                            myRHS.append(self.wpcGenerator.getVariableForAggregateFunctionInSelect(varString))                # <--- RHS
                        elif self.helper.getRuleName(tempNode.children[i]) == "into_clause":
                            into_flag = i
                            intoNode = tempNode.children[i]
                            for x in range(intoNode.getChildCount()):
                                if intoNode.children[x].getChildCount() > 0 and self.helper.getRuleName(intoNode.children[x]) == "variable_name":
                                    myLHS.append(intoNode.children[x].getText().strip())        # <--- LHS
                        elif self.helper.getRuleName(tempNode.children[i]) == "from_clause":
                            conditionInFromClause = self.wpcGenerator.extractConditionsInFromClause(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                            # myLHS & myRHS & conditionInFromClause will be already filled here if they should be
                            whereCondition = self.wpcGenerator.getConditionalString(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                            if not conditionInFromClause == "":     # merging condition from WHERE and FROM_CLAUSE
                                whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                            whereHandled_flag = True
                            if into_flag > -1:
                                # update wpcString for true part of where Condition
                                trueWpcString = wpcString
                                for j in range(len(myLHS)):
                                    trueWpcString = trueWpcString.replace(" " + myLHS[j] + " ", " " + myRHS[j] + " ")
                                    if not trueWpcString.strip() == wpcString.strip():
                                        didOldWpcChanged = True
                                    # also add RHS vars to variablesForZ3 set
                                    self.variablesForZ3.add(myRHS[j])  # <<<-----------<<<---------------<<<-------------
                                # now join 'true' and 'false' like 'if' block...
                                if didOldWpcChanged:
                                    if self.wpcGenerator.nullInCondition(tempNode.children[i].children[1]):   # NULL +nt in condition
                                        if conditionInFromClause == "":
                                            wpcString = "( " + trueWpcString + " v " + wpcString + " )"
                                        else:       # if FROM_CLAUSE is not empty, we have to treat it as condition
                                            wpcString = "( ( " + conditionInFromClause + " ^ " + trueWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
                                    else:   # NULL not +nt in condition
                                        wpcString = "( ( " + whereCondition + " ^ " + trueWpcString + " ) v ( ( ! " + whereCondition + " ) ^ " + wpcString + " ) )"
                if whereHandled_flag is False and into_flag > -1:
                    # do update in wpcString here becoz whereCondition do not exist in SELECT
                    for i in range(len(myLHS)):
                        wpcString = wpcString.replace(" " + myLHS[i] + " ", " " + myRHS[i] + " ")
                        if not trueWpcString.strip() == wpcString.strip():
                            didOldWpcChanged = True
                        # also add RHS vars to variablesForZ3 set
                        self.variablesForZ3.add(myRHS[i])       # <<<-----------<<<---------------<<<-------------
                    # BUT, don't relax, condition from FROM_CLAUSE may not be empty!!!
                    if not conditionInFromClause == "" and didOldWpcChanged:
                        wpcString = "( ( " + conditionInFromClause + " ^ " + trueWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
                # also add every RHS var to variablesForZ3 set, be tension free...
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
            elif self.helper.getRuleName(currentNode.ctx) == "insert_statement":  # Database INSERT statement
                tempNode = currentNode.ctx.children[1]      # single_table_insert
                myLHS = []
                myRHS = []
                count = tempNode.children[0].getChildCount()    # inset_into_clause
                if count > 2:
                    i = 2
                    while i < count:
                        if tempNode.children[0].children[i].getChildCount() > 0:
                            myLHS.append(tempNode.children[0].children[i].getText().strip())
                        i = i+1
                count = tempNode.children[1].children[1].getChildCount()    # expression_list
                i = 0
                while i < count:
                    node = tempNode.children[1].children[1].children[i]
                    if node.getChildCount() > 0:
                        myRHS.append(self.wpcGenerator.ssaString.getTerminal(node).strip())
                    i = i+1
                # do replacing in wpcString now...
                if len(myLHS) > 0:
                    for i in range(len(myLHS)):
                        # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                        # DON'T expect more...
                        varString = myRHS[i]
                        varString = varString.replace("( )", "")
                        varString = varString.replace("  ", " ").strip()
                        replacedBy = "( " + varString + " )"
                        wpcString = wpcString.replace(" " + myLHS[i] + " ", " " + replacedBy + " ")
                # else:
                #     # get LHS vars from tableDict of MyHelper
                #     # BUT, for that table attributes must be stored in order
                #     # so, tableDict must be modified to Dictionary of List...
                #     # this is a TODO
                # also add RHS vars to variablesForZ3 set
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
            elif self.helper.getRuleName(currentNode.ctx) == "fetch_statement":    # Database FETCH statement
                for i in currentNode.variableLHS:
                    replacedBy = "( " + self.wpcGenerator.ssaString.getTerminal(currentNode.ctx.children[1]).strip() + " )"      # see FETCH stmt structure for reference
                    wpcString = wpcString.replace(" "+i.strip()+" ", " "+replacedBy+" ")
                # also add RHS vars to variablesForZ3 set
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
            elif self.helper.getRuleName(currentNode.ctx) == "cursor_declaration":  # Database CURSOR statement
                lhsVar = ""
                rhsVar = ""
                whereCondition = ""
                conditionInFromClause = ""
                isWherePresent = False
                isNullPresentInWhere = False
                for i in range(currentNode.ctx.getChildCount()):
                    if self.helper.getRuleName(currentNode.ctx.children[i]) == "cursor_name":
                        lhsVar = currentNode.ctx.children[i].getText().strip()
                    elif self.helper.getRuleName(currentNode.ctx.children[i]) == "select_statement":
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
                        # BUT what to do if there are multiple SELECTION attributes here???...as per datasets assuming single attribute...
                        varString = self.wpcGenerator.ssaString.getTerminal(tempCtx.children[1]).strip()
                        rhsVar = self.wpcGenerator.getVariableForAggregateFunctionInSelect(varString)
                if not(lhsVar == "") and not(rhsVar == ""):
                    didOldWpcChanged = False
                    newWpcString = wpcString
                    newWpcString = newWpcString.replace(" " + lhsVar + " ", " " + rhsVar + " ")
                    if not newWpcString.strip() == wpcString.strip():
                        didOldWpcChanged = True
                    if didOldWpcChanged:
                        if isWherePresent:
                            if isNullPresentInWhere:
                                if conditionInFromClause == "":
                                    wpcString = "( " + newWpcString + " v " + wpcString + " )"
                                else:
                                    wpcString = "( ( " + conditionInFromClause + " ^ " + newWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
                            else:
                                if not conditionInFromClause == "":
                                    whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                                wpcString = "( ( " + whereCondition + " ^ " + newWpcString + " ) v ( ( ! " + whereCondition + " ) ^ " + wpcString + " ) )"
                        else:
                            if conditionInFromClause == "":
                                wpcString = newWpcString
                            else:
                                wpcString = "( ( " + conditionInFromClause + " ^ " + newWpcString + " ) v ( ( ! " + conditionInFromClause + " ) ^ " + wpcString + " ) )"
                # also add every RHS var to variablesForZ3 set
                self.variablesForZ3.add(rhsVar)  # <<<-----------<<<---------------<<<-------------
                self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)       # <<<-----------<<<---------------<<<-------------
        return wpcString