
class WpcGenerator():

    def __init__(self, cfg, helper, ssaString):
        self.cfg = cfg
        self.helper = helper
        self.ssaString = ssaString
        self.variablesForZ3 = set()

        self.finalWpcString = ""
        self.totalNodeCount = -1
        self.cfgVisited = []


    def execute(self):
        self.totalNodeCount = len(self.cfg.nodes.keys())
        self.cfgVisited = [0] * self.totalNodeCount     # initialize visited list
        currentNodeId = self.totalNodeCount - 1
        # self.runner(currentNodeId)        # 1st approach
        # self.goodAlgo(currentNodeId, "")    # 2nd approach
        self.wpcStringMakerAlgo(currentNodeId, "")      # modified 2nd approach


    ### modifying 2nd approach...

    def wpcStringMakerAlgo(self, currentNodeId, wpcString):
        if self.cfgVisited[currentNodeId] == 1:
            return
        currentNode = self.cfg.nodes[currentNodeId]
        if len(currentNode.next) > 1:       # it's a conditional Node! Yo!!!
            listOfNext = list(currentNode.next)
            if self.cfgVisited[listOfNext[0]]==1 and self.cfgVisited[listOfNext[1]]==1:
                # Beware! first enrich wpcMakerHelper dict()
                self.enrich_wpcMakerHelper(currentNodeId, wpcString)
                # merge true and false part
                # print("----", str(currentNodeId), "---", currentNode.wpcMakerHelper)
                if self.nullInCondition(currentNode.ctx):   # NULL +nt in condition
                    wpcString = self.mergeConditionalWpcStringsIfConditionContainsNULL(currentNode)
                    # no need to add anything to variablesForZ3 set
                else:   # NULL not +nt in condition
                    conditionalString = self.getConditionalString(currentNode.ctx)
                    # print("&&&&&&&&&&&&&& if_condition:", conditionalString)
                    wpcString = self.mergeConditionalWpcStrings(currentNode, conditionalString)
                    # also add RHS vars of CONDITION to variablesForZ3 set
                    self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
            elif self.cfgVisited[listOfNext[0]]==1:
                self.addWpcString(currentNodeId, listOfNext[0], wpcString)
                return
            elif self.cfgVisited[listOfNext[1]]==1:
                self.addWpcString(currentNodeId, listOfNext[1], wpcString)
                return
        self.cfgVisited[currentNodeId] = 1  # visit the node
        # print(str(currentNodeId), "visited, wpc :", wpcString)
        if len(currentNode.next) <= 1:      # avoid conditional node for wpcString here
            if not currentNode.ctx == None:     # check if ctx is None
                if self.helper.getRuleName(currentNode.ctx) == "assert_statement":
                    wpcString = self.getConditionalString(currentNode.ctx.children[1])         # start wpcString here
                    # also add RHS vars to variablesForZ3 set
                    self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
                elif self.helper.getRuleName(currentNode.ctx) == "assume_statement":
                    assumeCondition = self.getConditionalString(currentNode.ctx.children[1])
                    wpcString = "( " + assumeCondition + " ==> " + wpcString + " )"
                    # also add RHS vars to variablesForZ3 set
                    self.variablesForZ3 = self.variablesForZ3.union(currentNode.variableRHS)  # <<<-----------<<<---------------<<<-------------
                    # one may want to finalize and return here...   # TODO: decide later, what to do here for ASSUME,
                    # self.finalWpcString = wpcString               # But nothing pre topmost ASSUME will be reflected in "Z3RuntimeWpcFile.py", so our work is done!
                    # return
                elif not wpcString == "":
                    wpcString = self.updateWpcStringByReplacing(wpcString, currentNode)
                    # print(wpcString)
        # go to parents...
        if len(currentNode.parent) < 1:
            self.finalWpcString = wpcString
            return
        elif len(currentNode.parent) == 1:
            parent = set(currentNode.parent)
            self.wpcStringMakerAlgo(parent.pop(), wpcString)
        elif len(currentNode.parent) > 1:
            setOfParents = set(currentNode.parent)
            while len(setOfParents) >= 1:
                tempNodeId = setOfParents.pop()
                self.wpcStringMakerAlgo(tempNodeId, wpcString)


    def mergeConditionalWpcStrings(self, currentNode, conditionalString):
        tempString1 = ""
        tempString2 = ""
        if not currentNode.wpcMakerHelper['true'] == "":
            tempString1 = "( " + conditionalString + " ^ " + currentNode.wpcMakerHelper['true'] + " )"
        if not currentNode.wpcMakerHelper['false'] == "":
            tempString2 = "( ( ! " + conditionalString + " ) ^ " + currentNode.wpcMakerHelper['false'] + " )"
        wpcString = ""
        if tempString1 == "":
            wpcString = tempString2
        elif tempString2 == "":
            wpcString = tempString1
        else:
            wpcString = "( " + tempString1 + " v " + tempString2 + " )"
        return wpcString

    def mergeConditionalWpcStringsIfConditionContainsNULL(self, currentNode):
        tempString1 = ""
        tempString2 = ""
        if not currentNode.wpcMakerHelper['true'] == "":
            tempString1 = currentNode.wpcMakerHelper['true']
        if not currentNode.wpcMakerHelper['false'] == "":
            tempString2 = currentNode.wpcMakerHelper['false']
        wpcString = ""
        if tempString1 == "":
            wpcString = tempString2
        elif tempString2 == "":
            wpcString = tempString1
        else:
            wpcString = "( " + tempString1 + " v " + tempString2 + " )"
        return wpcString


    # def updateWpcStringByReplacing(self, wpcString, currentNode):   # this is better than "updateWpcStringBySplitting" method
    #     wpcString = wpcString.replace("  ", " ").strip()
    #     if len(currentNode.variableLHS) > 0:
    #         for i in currentNode.variableLHS:
    #             if self.helper.getRuleName(currentNode.ctx) == "assignment_statement":  # strictly assignment_statement
    #                 replacedBy = "( " + self.ssaString.getTerminal(currentNode.ctx.children[2]) + " )"
    #                 wpcString = wpcString.replace(" "+i.strip()+" ", " "+replacedBy+" ")
    #     return wpcString

    def updateWpcStringByReplacing(self, wpcString, currentNode):   # this is better than "updateWpcStringBySplitting" method
        wpcString = wpcString.replace("  ", " ").strip()
        if len(currentNode.variableLHS) > 0:
            if self.helper.getRuleName(currentNode.ctx) == "assignment_statement":  # strictly assignment_statement
                for i in currentNode.variableLHS:
                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                    # DON'T expect more... do same for UPDATE, INSERT rhs...
                    varString = self.ssaString.getTerminal(currentNode.ctx.children[2]).strip()
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
                        whereCondition = self.getConditionalString(currentNode.ctx.children[i].children[1])
                        # print("@@@@@@@ update_statement whereCondition :", whereCondition)
                        break
                if not whereClausePosition == -1:   # whereCondition exists
                    tempWpcString = wpcString
                    updateSetCtx = currentNode.ctx.children[whereClausePosition-1]
                    for i in range(updateSetCtx.getChildCount()):       # finding "column_based_update_set_clause"...
                        if updateSetCtx.children[i].getChildCount() > 1 and self.helper.getRuleName(
                                updateSetCtx.children[i]) == "column_based_update_set_clause":
                            toBeReplaced = " " + updateSetCtx.children[i].children[0].getText().strip() + " "
                            # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                            # DON'T expect more...
                            varString = self.ssaString.getTerminal(updateSetCtx.children[i].children[2]).strip()
                            varString = varString.replace("( )", "")
                            varString = varString.replace("  ", " ").strip()
                            replacedBy = " ( " + varString + " ) "
                            tempWpcString = tempWpcString.replace(toBeReplaced, replacedBy)
                    # now join 'true' and 'false' like 'if' block...
                    if self.nullInCondition(currentNode.ctx.children[whereClausePosition].children[1]):  # NULL +nt in condition
                        wpcString = "( " + tempWpcString + " v " + wpcString + " )"
                    else:  # NULL not +nt in condition
                        wpcString = "( ( " + whereCondition + " ^ " + tempWpcString + " ) v ( ( ! " + whereCondition + " ) ^ " + wpcString + " ) )"
                else:       # whereCondition does not exist...so, no merging like 'if' block...
                    for i in range(currentNode.ctx.getChildCount()):        # finding "update_set_clause"...
                        if currentNode.ctx.children[i].getChildCount() > 1 and self.helper.getRuleName(currentNode.ctx.children[i]) == "update_set_clause":
                            updateSetCtx = currentNode.ctx.children[i]
                            for j in range(updateSetCtx.getChildCount()):       # finding "column_based_update_set_clause"...
                                if updateSetCtx.children[j].getChildCount() > 1 and self.helper.getRuleName(
                                        updateSetCtx.children[j]) == "column_based_update_set_clause":
                                    toBeReplaced = " " + updateSetCtx.children[j].children[0].getText().strip() + " "
                                    # converting functions like "xyx_ab_jhk()" in RHS to equivalent variable "xyx_ab_jhk", however nested RHS is
                                    # DON'T expect more...
                                    varString = self.ssaString.getTerminal(updateSetCtx.children[j].children[2]).strip()
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
                conditionInFromClause = ""
                # SELECT A, B, C2 INTO K, L, M   FROM T JOIN T2 ON B=B2 JOIN T3 ON A2=A3   WHERE A2=X+3;
                trueWpcString = ""
                into_flag = -1
                whereHandled_flag = False
                for i in range(tempNode.getChildCount()):
                    if tempNode.children[i].getChildCount() > 0:
                        if self.helper.getRuleName(tempNode.children[i]) == "selected_element":
                            varString = self.ssaString.getTerminal(tempNode.children[i]).strip()
                            myRHS.append(self.getVariableForAggregateFunctionInSelect(varString))                # <--- RHS
                        elif self.helper.getRuleName(tempNode.children[i]) == "into_clause":
                            into_flag = i
                            intoNode = tempNode.children[i]
                            for x in range(intoNode.getChildCount()):
                                if intoNode.children[x].getChildCount() > 0 and self.helper.getRuleName(intoNode.children[x]) == "variable_name":
                                    myLHS.append(intoNode.children[x].getText().strip())        # <--- LHS
                        elif self.helper.getRuleName(tempNode.children[i]) == "from_clause":
                            conditionInFromClause = self.extractConditionsInFromClause(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement conditionInFromClause :", conditionInFromClause)
                        elif self.helper.getRuleName(tempNode.children[i]) == "where_clause":
                            # myLHS & myRHS & conditionInFromClause will be already filled here if they should be
                            whereCondition = self.getConditionalString(tempNode.children[i].children[1])
                            # print("@@@@@@@ select_statement whereCondition :", whereCondition)
                            if not conditionInFromClause == "":     # merging condition from WHERE and FROM_CLAUSE
                                whereCondition = "( " + conditionInFromClause + " ^ " + whereCondition + " )"
                            whereHandled_flag = True
                            if into_flag > -1:
                                # update wpcString for true part of where Condition
                                trueWpcString = wpcString
                                for j in range(len(myLHS)):
                                    trueWpcString = trueWpcString.replace(" " + myLHS[j] + " ", " " + myRHS[j] + " ")
                                    # also add RHS vars to variablesForZ3 set
                                    self.variablesForZ3.add(myRHS[j])  # <<<-----------<<<---------------<<<-------------
                                # now join 'true' and 'false' like 'if' block...
                                if self.nullInCondition(tempNode.children[i].children[1]):   # NULL +nt in condition
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
                        # also add RHS vars to variablesForZ3 set
                        self.variablesForZ3.add(myRHS[i])       # <<<-----------<<<---------------<<<-------------
                    # BUT, don't relax, condition from FROM_CLAUSE may not be empty!!!
                    if not conditionInFromClause == "":
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
                        myRHS.append(self.ssaString.getTerminal(node).strip())
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
                    replacedBy = "( " + self.ssaString.getTerminal(currentNode.ctx.children[1]).strip() + " )"      # see FETCH stmt structure for reference
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
                                conditionInFromClause = self.extractConditionsInFromClause(tempCtx.children[j].children[1])
                                # print("@@@@@@@ cursor_statement conditionInFromClause :", conditionInFromClause)
                            elif self.helper.getRuleName(tempCtx.children[j]) == "where_clause":
                                isWherePresent = True
                                if self.nullInCondition(tempCtx.children[j].children[1]):
                                    isNullPresentInWhere = True
                                else:
                                    whereCondition = self.getConditionalString(tempCtx.children[j].children[1])
                                    # print("@@@@@@@ cursor_statement whereCondition :", whereCondition)
                        # BUT what to do if there are multiple SELECTION attributes here???...as per datasets assuming single attribute...
                        varString = self.ssaString.getTerminal(tempCtx.children[1]).strip()
                        rhsVar = self.getVariableForAggregateFunctionInSelect(varString)
                if not(lhsVar == "") and not(rhsVar == ""):
                    newWpcString = wpcString
                    newWpcString = newWpcString.replace(" " + lhsVar + " ", " " + rhsVar + " ")
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


    # Recursive method to extract Conditions In From_Clause (SELECT, SELECT-IN-CURSOR)
    def extractConditionsInFromClause(self, ctx):       # ctx ~ from_clause.children[1]
        if self.helper.getRuleName(ctx) == "table_ref":
            if ctx.getChildCount() == 2:
                leftCondition = self.extractConditionsInFromClause(ctx.children[0])
                rightCondition = self.extractConditionsInFromClause(ctx.children[1])
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
                    condition = self.getConditionalString(ctx.children[i].children[1].children[0])
            return condition


    # TODO: condition not proper for conditions like "NAME LIKE 'RYAN'" or "NAME IS VAR_NAME", avoid datasets having keywords IS, LIKE etc.
    def getConditionalString(self, ctx):   # considering only AND, OR, NOT, IN, BETWEEN as 'word' separator
        if ctx.getChildCount() == 1:
            return self.getConditionalString(ctx.children[0])
        elif ctx.getChildCount() == 2:      # strictly for "NOT"
            if ctx.children[0].getText().strip() == "NOT":
                return "( ! " + self.getConditionalString(ctx.children[1]) + " )"
        elif ctx.getChildCount() == 3:
            operators = ['=', '>', '<', '>=', '<=', '!=', '<>', '^=', '~=']
            if ctx.children[1].getText().strip() == "AND":  # conditions separated by "AND"
                return "( " + self.getConditionalString(ctx.children[0]) + " ^ " + self.getConditionalString(ctx.children[2]) + " )"
            elif ctx.children[1].getText().strip() == "OR":  # conditions separated by "OR"
                return "( " + self.getConditionalString(ctx.children[0]) + " v " + self.getConditionalString(ctx.children[2]) + " )"
            elif ctx.children[1].getText().strip() in operators:
                return "( " + self.ssaString.getTerminal(ctx).strip() + " )"
            else:
                return self.getConditionalString(ctx.children[1])
        elif ctx.getChildCount() == 5:
            if self.ssaString.getTerminal(ctx.children[1]).strip() == "BETWEEN":  # For "XX BETWEEN 10 AND 50"
                referenceVar = "( " + self.ssaString.getTerminal(ctx.children[0]).strip() + " )"
                leftBoundary = "( " + self.ssaString.getTerminal(ctx.children[2]).strip() + " )"
                rightBoundary = "( " + self.ssaString.getTerminal(ctx.children[4]).strip() + " )"
                return "( ( " + referenceVar + " > " + leftBoundary + " ) ^ ( " + referenceVar + " < " + rightBoundary + " ) )"
            elif self.ssaString.getTerminal(ctx.children[1]).strip() == "IN":  # For "XX IN ( select_subquery )"
                leftVar = self.ssaString.getTerminal(ctx.children[0]).strip()
                selectQueryCtx = ctx.children[3].children[0]
                rightVar = self.ssaString.getTerminal(selectQueryCtx.children[1]).strip()
                isWhereCondition = False
                isNullInCondition = False
                condition = ""
                for m in range(selectQueryCtx.getChildCount()):
                    if self.helper.getRuleName(selectQueryCtx.children[m]) == "where_clause":
                        isWhereCondition = True
                        if self.nullInCondition(selectQueryCtx.children[m].children[1]):
                            isNullInCondition = True
                        else:
                            condition = self.getConditionalString(selectQueryCtx.children[m].children[1])
                if isWhereCondition:
                    if isNullInCondition:
                        return "( " + leftVar + " = " + rightVar + " )"
                    else:
                        return "( ( " + leftVar + " = " + rightVar + " ) ^ ( " + condition + " ) )"
                else:
                    return "( " + leftVar + " = " + rightVar + " )"
            return ""
        elif ctx.getChildCount() == 6:  # For "XX NOT BETWEEN 10 AND 50"
            if self.ssaString.getTerminal(ctx.children[2]).strip() == "BETWEEN":
                referenceVar = "( " + self.ssaString.getTerminal(ctx.children[0]).strip() + " )"
                leftBoundary = "( " + self.ssaString.getTerminal(ctx.children[3]).strip() + " )"
                rightBoundary = "( " + self.ssaString.getTerminal(ctx.children[5]).strip() + " )"
                return "( ( " + referenceVar + " < " + leftBoundary +" ) v ( " + referenceVar + " > " + rightBoundary +" ) )"
            elif self.ssaString.getTerminal(ctx.children[2]).strip() == "IN":  # For "XX NOT IN ( select_subquery )"
                leftVar = self.ssaString.getTerminal(ctx.children[0]).strip()
                selectQueryCtx = ctx.children[4].children[0]
                rightVar = self.ssaString.getTerminal(selectQueryCtx.children[1]).strip()
                isWhereCondition = False
                isNullInCondition = False
                condition = ""
                for m in range(selectQueryCtx.getChildCount()):
                    if self.helper.getRuleName(selectQueryCtx.children[m]) == "where_clause":
                        isWhereCondition = True
                        if self.nullInCondition(selectQueryCtx.children[m].children[1]):
                            isNullInCondition = True
                        else:
                            condition = self.getConditionalString(selectQueryCtx.children[m].children[1])
                if isWhereCondition:
                    if isNullInCondition:
                        return "( ! ( " + leftVar + " = " + rightVar + " ) )"
                    else:
                        return "( ( ! ( " + leftVar + " = " + rightVar + " ) ) ^ ( " + condition + " ) )"
                else:
                    return "( ! ( " + leftVar + " = " + rightVar + " ) )"
            return ""
        elif ctx.getChildCount() == 0:      # for stmts like "UPDATE --blah blah-- WHERE SingleWord;"
            return "( " + self.ssaString.getTerminal(ctx).strip() + " )"


    # Returns True if NULL is found in conditional String
    def nullInCondition(self, conditionalCtx):
        condition = self.ssaString.getTerminal(conditionalCtx).strip()
        tokens = condition.split(" ")   # tokens will be a list
        if "NULL" in tokens:
            return True
        return False

    def getVariableForAggregateFunctionInSelect(self, varString):
        varString = varString.replace("(", "")
        varString = varString.replace(")", "")
        varString = varString.replace(",", "")
        varString = varString.strip()
        varString = varString.replace("  ", " ")
        varString = varString.replace(" ", "_")
        varString = varString.replace("*", "STAR")
        return varString


    def addWpcString(self, currentNodeId, myVisitedChildId, wpcString):
        if self.cfg.nodes[currentNodeId].branching['true'] == myVisitedChildId:
            self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString    # fool! don't just edit the copy!
        elif self.cfg.nodes[currentNodeId].branching['false'] == myVisitedChildId:
            self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString

    def enrich_wpcMakerHelper(self, currentNodeId, wpcString):
        if len(self.cfg.nodes[currentNodeId].wpcMakerHelper) < 2:
            if self.cfg.nodes[currentNodeId].wpcMakerHelper.get('true') == None:
                self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
            elif self.cfg.nodes[currentNodeId].wpcMakerHelper.get('false') == None:
                self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString




    ### 2nd approach... better complexity than 1st one

    # def goodAlgo(self, currentNodeId, wpcString):
    #     if self.cfgVisited[currentNodeId] == 1:
    #         return
    #
    #     currentNode = self.cfg.nodes[currentNodeId]
    #     if len(currentNode.next) > 1:       # it's a condition! Yo!!!
    #         listOfNext = list(currentNode.next)
    #         if self.cfgVisited[listOfNext[0]]==1 and self.cfgVisited[listOfNext[1]]==1:
    #             # Beware! first enrich wpcMakerHelper dict()
    #             self.enrich_wpcMakerHelper(currentNodeId, wpcString)
    #             # if len(currentNode.wpcMakerHelper) < 2:
    #             #     if currentNode.wpcMakerHelper.get('true') == None:
    #             #         self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
    #             #     elif currentNode.wpcMakerHelper.get('false') == None:
    #             #         self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
    #
    #             # merge true and false part
    #             print(listOfNext)
    #             print("-------", currentNode.wpcMakerHelper)
    #             wpcString = "( ( " + str(currentNodeId) + " ^ " + currentNode.wpcMakerHelper['true'] + " ) v ( ( ! " + str(currentNodeId) + " ) ^ " + currentNode.wpcMakerHelper['false'] + " ) )"
    #         elif self.cfgVisited[listOfNext[0]]==1:
    #             print("first")
    #             self.addWpcString(currentNodeId, listOfNext[0], wpcString)
    #             # if currentNode.branching['true']==listOfNext[0]:
    #             #     self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString    # fool! don't just edit the copy!
    #             # elif currentNode.branching['false']==listOfNext[0]:
    #             #     self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
    #             return
    #         elif self.cfgVisited[listOfNext[1]]==1:
    #             print("second")
    #             self.addWpcString(currentNodeId, listOfNext[1], wpcString)
    #             # if currentNode.branching['true']==listOfNext[1]:
    #             #     self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
    #             # elif currentNode.branching['false']==listOfNext[1]:
    #             #     self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
    #             return
    #
    #     self.cfgVisited[currentNodeId] = 1
    #     print(">>>", currentNodeId, "= 1")
    #     if len(currentNode.next) <= 1:      # avoid conditional node for wpcString
    #         wpcString = wpcString + "." + str(currentNodeId)
    #
    #     #..........
    #     if len(currentNode.parent) < 1:
    #         self.finalWpcString = wpcString
    #         return
    #     elif len(currentNode.parent) == 1:
    #         parent = set(currentNode.parent)
    #         self.goodAlgo(parent.pop(), wpcString)
    #     elif len(currentNode.parent) > 1:
    #         setOfParents = set(currentNode.parent)
    #         while len(setOfParents) >= 1:
    #             tempNodeId = setOfParents.pop()
    #             self.goodAlgo(tempNodeId, wpcString)
    #
    # def addWpcString(self, currentNodeId, myVisitedChildId, wpcString):
    #     if self.cfg.nodes[currentNodeId].branching['true'] == myVisitedChildId:
    #         self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString    # fool! don't just edit the copy!
    #     elif self.cfg.nodes[currentNodeId].branching['false'] == myVisitedChildId:
    #         self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString
    #
    # def enrich_wpcMakerHelper(self, currentNodeId, wpcString):
    #     if len(self.cfg.nodes[currentNodeId].wpcMakerHelper) < 2:
    #         if self.cfg.nodes[currentNodeId].wpcMakerHelper.get('true') == None:
    #             self.cfg.nodes[currentNodeId].wpcMakerHelper['true'] = wpcString
    #         elif self.cfg.nodes[currentNodeId].wpcMakerHelper.get('false') == None:
    #             self.cfg.nodes[currentNodeId].wpcMakerHelper['false'] = wpcString


    ### 1st approach...

    # def runner(self, currentNodeId):
    #     print(currentNodeId, end=" ")
    #     if len(self.cfg.nodes[currentNodeId].parent) < 1:
    #         return
    #     else:
    #         setOfParents = set(self.cfg.nodes[currentNodeId].parent)
    #         while len(setOfParents) >= 1:
    #             tempNodeId = setOfParents.pop()
    #             self.runner(tempNodeId)
