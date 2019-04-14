from gen.PlSqlVisitor import PlSqlVisitor


class MyHelper(PlSqlVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.temp = set()
        self.tableDict = dict()         # now it will take from specification
        self.functionDict = dict()      # TODO: complete attributes for FUNCTIONS......{"funName": ({LHS vars}, {RHS vars})}


    def getRuleName(self, ctx):
        if ctx == None:
            return ''
        if ctx.getChildCount() == 0:
            return ''
        s = str(ctx.toStringTree(recog=self.parser))
        n = len(s)
        i = 0
        while not(s[i] == '('):
            i = i+1
        j = i+1
        while not(s[j] == ' '):
            j = j+1
        return s[i+1:j]


    def getVariableSet(self, ctx):
        res = self.generateRHS(ctx)
        res = res.union(self.generateLHS(ctx))
        return res
    
    
    
    def isAssignEq(self, ctx):
        ruleName = self.getRuleName(ctx)
        assignEqSet = {"cursor_declaration", "fetch_statement",
                        "insert_statement", "delete_statement", "update_statement", "assignment_statement", "function_call", "select_statement"}
        if ruleName in assignEqSet:
            return True
        else:
            return False



    def generateRHS(self, ctx):
        res = set()
        ruleName = self.getRuleName(ctx)
        if ruleName == "parameter":
            res.add(ctx.children[0].getText())
        elif ruleName == "variable_declaration":
            res.add(ctx.children[0].getText())
        elif ruleName=="cursor_declaration":
            tempCtx = ctx.children[ctx.getChildCount()-2].children[0].children[0]
            res = self.selectHandling(tempCtx, res)
        elif ruleName == "open_statement":
            res.add(ctx.children[1].getText())
        elif ruleName == "fetch_statement":
            res.add(ctx.children[1].getText())
        elif ruleName == "close_statement":
            res.add(ctx.children[1].getText())
        #incorporating 'if'...
        elif ruleName == "condition":
            self.temp = set()
            self.visit(ctx)
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "insert_statement":
            self.temp = set()
            self.visit(ctx.children[1].children[1])
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "delete_statement":
            self.temp = set()
            self.visit(ctx.children[3])
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "update_statement":
            self.temp = set()
            for i in range(ctx.getChildCount()):
                tempRuleName = self.getRuleName(ctx.children[i])
                if tempRuleName == 'update_set_clause':
                    for j in range(ctx.children[i].getChildCount()):
                        if self.getRuleName(ctx.children[i].children[j]) == 'column_based_update_set_clause':
                            self.visit(ctx.children[i].children[j].children[2])
                elif tempRuleName == 'where_clause':
                    self.visit(ctx.children[i])

            res = res.union(self.temp)
            dTableName = ctx.children[1].getText()
            res = res.union(self.tableDict[dTableName])
            self.temp = set()
            # # self.temp = set()
            # # self.visit(ctx.children[2])   #todo: maybe UPDATE SET CLAUSE
            # # res = res.union(self.temp)
            # # self.temp = set()
            # self.temp = set()
            # self.visit(ctx.children[2].children[1].children[2])     #TODO: make it proper (it's temporary soln)
            # self.visit(ctx.children[3])
            # res = res.union(self.temp)
            # dTableName = ctx.children[1].getText()
            # res = res.union(self.tableDict[dTableName])
            # self.temp = set()
        elif ruleName=="select_statement":
            #print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4 entered in RHS select\n\n\n")
            tempCtx = ctx.children[0].children[0]
            res = self.selectHandling(tempCtx, res)
        elif ruleName == "assignment_statement":
            self.temp = set()
            self.visit(ctx.children[2])
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "function_call":
            funName = ctx.children[0].getText()
            res = res.union(self.functionDict[funName][1])
        elif ruleName == "assert_statement":
            self.temp = set()
            self.visit(ctx.children[1])
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "assume_statement":
            self.temp = set()
            self.visit(ctx.children[1])
            res = res.union(self.temp)
            self.temp = set()
        return res


    
    
    def generateLHS(self, ctx):
        if not(self.isAssignEq(ctx)):
            return {}
        else:
            res = set()
            ruleName = self.getRuleName(ctx)
            # if ruleName=="parameter":
            #     res.add(ctx.children[0].getText())
            # elif ruleName=="variable_declaration":
            #     res.add(ctx.children[0].getText())
            # el
            if ruleName=="cursor_declaration":
                res.add(ctx.children[1].getText())
            elif ruleName=="fetch_statement":
                res.add(ctx.children[3].getText())
            elif ruleName=="insert_statement":
                dTableName = ctx.children[1].children[0].children[1].getText()
                res = res.union(self.tableDict[dTableName])
            elif ruleName=="delete_statement":          #todo: need to hardcode
                dTableName = ctx.children[2].getText()
                res = res.union(self.tableDict[dTableName])
            elif ruleName == "update_statement":          #todo: need to hardcode
                #print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4 entered in LHS update\n\n\n")
                dTableName = ctx.children[1].getText()
                res = res.union(self.tableDict[dTableName])
            elif ruleName == "assignment_statement":
                self.temp = set()
                self.visit(ctx.children[0])
                res = res.union(self.temp)
                self.temp = set()
            elif ruleName == "function_call":
                funName = ctx.children[0].getText()
                res = res.union(self.functionDict[funName][0])
            elif ruleName == "select_statement":
                #print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4 entered in LHS select\n\n\n")
                tempCtx = ctx.children[0].children[0]
                for i in range(tempCtx.getChildCount()):
                    #print("\n\t\t\t", self.getRuleName(tempCtx.children[i]), "\n\n")
                    if self.getRuleName(tempCtx.children[i]) == "into_clause":
                        for x in range(tempCtx.children[i].getChildCount()):
                            if self.getRuleName(tempCtx.children[i].children[x]) == 'variable_name':
                                res.add(tempCtx.children[i].children[x].getText())
                        # #print("\n\t\t\t", tempCtx.children[i].children[1].getText(), "\n\n")
                        # res.add(tempCtx.children[i].children[1].getText())
            return res



    def visitColumn_name(self, ctx):
        self.temp.add(ctx.getText())

    def visitRegular_id(self, ctx):
        self.temp.add(ctx.getText())

    def selectHandling(self, tempCtx, res):
        for i in range(tempCtx.getChildCount()):
            if tempCtx.children[i].getText() == "*":
                tableName = tempCtx.children[i + 1].children[1].getText()
                res = res.union(self.tableDict[tableName])
            elif self.getRuleName(tempCtx.children[i]) == "selected_element":
                #print("**************************************************************", "\n\n\n\n\n\n\n\n\n")
                varStr = tempCtx.children[i].getText().strip()
                tempList = varStr.split('(')
                if len(tempList) > 1:
                    varStr2 = tempList[1].strip(')').strip()
                    if varStr2 == '*':      # for count(*)
                        continue
                    else:
                        res.add(varStr2)
                else:
                    res.add(tempCtx.children[i].getText())
                #res.add(tempCtx.children[i].getText())
            elif self.getRuleName(tempCtx.children[i]) == "from_clause":
                # tableName = tempCtx.children[i].children[1].getText()
                for k in range(tempCtx.children[i].getChildCount()):
                    if self.getRuleName(tempCtx.children[i].children[k]) == "table_ref":
                        tableSet = set()
                        self.extractConditionsInFromClause(tempCtx.children[i].children[k], tableSet)
                        # print("**************************************************************", tableSet, "\n\n\n\n\n\n\n\n\n")
                        for tableName in tableSet:
                            res = res.union(self.tableDict[tableName])
                # res = res.union(self.tableDict[tableName])
            elif self.getRuleName(tempCtx.children[i]) == "where_clause":
                #print("*****************************************where*********************", "\n\n\n\n\n\n\n\n\n")
                self.temp = set()
                self.visit(tempCtx.children[i].children[1])
                res = res.union(self.temp)
                self.temp = set()
        return res


    # Recursive method to extract Tablenames In From_Clause (SELECT, SELECT-IN-CURSOR)
    def extractConditionsInFromClause(self, ctx, resultTableSet):  # ctx ~ from_clause.children[1]
        if self.getRuleName(ctx) == "table_ref":
            if ctx.getChildCount() == 2:
                self.extractConditionsInFromClause(ctx.children[0], resultTableSet)
                self.extractConditionsInFromClause(ctx.children[1], resultTableSet)
            elif ctx.getChildCount() == 1:
                resultTableSet.add(ctx.getText().strip())
        elif self.getRuleName(ctx) == "join_clause":
            for i in range(ctx.getChildCount()):
                if self.getRuleName(ctx.children[i]) == "table_ref":
                    resultTableSet.add(ctx.children[i].getText().strip())


    def updateTableDict(self, tableInfo):               #todo : solve insert issue for all the attributes
        for table in tableInfo:
            attr = set()
            for pair in tableInfo[table]:
                attr.add(pair[0])
            self.tableDict[table] = attr
    
    '''
    def getVariableSet(self, ctx, id):  #TODO: remove id
        if id==0:
            return {'x'}
        if id==1:
            return {'y'}
        if id==2:
            return {'x'}
        if id==3:
            return {'y'}
        if id==4:
            return {'x', 'y'}
        if id==5:
            return {'x'}
        if id==6:
            return {'x', 'y'}
        if id==7:
            return {'x', 'y'}
        if id==8:
            return {'x', 'y'}
        if id==9:
            return {'y'}
        if id==10:
            return {}
        if id==11:
            return {'x', 'y'}

        # return {'x', 'y'}

    def isAssignEq(self, ctx, id):  #TODO: remove id
        # if id == 0 or id == 12 or id == 13 or id == 17 or id == 15 or id == 16 or id == 18 or id == 8:
        #     return True
        # return False
        if id == 7:
            return False
        return True

    def assignedVar(self, ctx, id):  #TODO: remove id, THIS NO LONGER NEEDED, SO PURGED

        if id == 2:
            return 'x'
        if id == 3:
            return 'y'
        if id == 4:
            return 'x'
        if id == 5:
            return 'x'
        if id == 6:
            return 'y'
        if id == 7:
            return ''
        if id == 8:
            return 'x'
        if id == 9:
            return 'y'
        if id == 10:
            return ''
        if id == 11:
            return 'y'

        return ''

    def generateRHS(self, ctx, id):  #TODO: remove id
        if id==0:
            return {}
        if id==1:
            return {}
        if id==2:
            return {}
        if id==3:
            return {}
        if id==4:
            return {'x', 'y'}
        if id==5:
            return {'x'}
        if id==6:
            return {'x'}
        if id==7:
            return {'x', 'y'}
        if id==8:
            return {'x', 'y'}
        if id==9:
            return {'y'}
        if id==10:
            return {}
        if id==11:
            return {'x', 'y'}
        #return {'y'}

    def generateLHS(self, ctx, id):  #TODO: remove id
        if id==0:
            return {'x'}
        if id==1:
            return {'y'}
        if id==2:
            return {'x'}
        if id==3:
            return {'y'}
        if id==4:
            return {'x'}
        if id==5:
            return {'x'}
        if id==6:
            return {'y'}
        if id==7:
            return {}
        if id==8:
            return {'x'}
        if id==9:
            return {'y'}
        if id==10:
            return {}
        if id==11:
            return {'y'}
        #return {'x'}
        '''
