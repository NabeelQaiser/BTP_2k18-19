from SeAPI.gen.PlSqlVisitor import PlSqlVisitor


class MyHelper(PlSqlVisitor):

    def __init__(self, parser):
        self.parser = parser
        self.temp = set()
        self.tableDict = dict({'WAREHOUSE_PARCEL': {'LEFT_WAREHOUSE', 'A_PARCEL_ID', 'WAREHOUSE_ID', 'ENTERED_WAREHOUSE','PARCEL_ID'},
                               'PARCEL_TYPE': {'ID', 'TYPE', 'MAX_ID'},
                               'ITEM_TABLE': {'ITEM_ID', 'ITEM_PRICE', 'ITEM_COUNT'},
                               'LOADS' : {'CUSTOMER_ID', 'LOAD_ID', 'WEIGHT'},
                               'ROUTES' : {'PRICE', 'LOAD_ID'},
                               'CAR_BRAND':{'ID', 'BRAND'},
                               'CAR' : {'LICENSE_NUMBER','BRAND_ID','MODEL','TRUNK_CAPACITY','LOAD_CAPACITY', 'PRODUCTION_YEAR','SERVICING_VALID_THRU'},
                               'CLIENT' : {'ID','NAME', 'SURNAME', 'STREET', 'HOUSE_NUMBER','APARTMENT_NUMBER','POSTAL_CODE','CITY','PROVINCE','COUNTRY_ID',
                               'PHONE_NUMBER'},
                               'COURIER' :{'ID','PESEL','NAME','SURNAME','STREET','HOUSE_NUMBER','APARTMENT_NUMBER','POSTAL_CODE','CITY','PROVINCE',
                               'COUNTRY_ID','CAR_LICENSE_NUMBER','WAREHOUSE_ID','PHONE_NUMBER','SALARY','CONTRACT_TYPE','CONTRACT_START'},
                               'COURIER_DRIVING_LICENSE_CATEGORY': {'COURIER_ID','DRIVING_LICENSE_CATEGORY_ID'},
                               'DELIVERY_STATUS' : {'ID','STATUS'},
                               'DELIVERY_ATTEMPT' : {'PARCEL_ID','COURIER_ID','ATTEMPT_TIMESTAMP','DELIVERY_STATUS_ID'},
                               'DIMENSION_CLASS' : {'ID', 'CLASS'},
                               'STATUS' : {'ID','STATUS'},
                               'WAREHOUSE' : {'ID', 'STREET', 'HOUSE_NUMBER', 'APARTMENT_NUMBER', 'POSTAL_CODE', 'CITY', 'PROVINCE', 'COUNTRY_ID', 'AREA'},
                               'PARCEL' :{'ID', 'SENDER_ID', 'RECEIVER_ID', 'WEIGHT', 'HEIGHT', 'WIDTH', 'DEPTH1', 'DIMENSION_CLASS_ID', 'PARCEL_TYPE_ID',
                               'STATUS_ID', 'CURRENT_WAREHOUSE_ID', 'WORTH', 'IS_COD','IS_INSURED'},
                               'T' : {'A', 'B'},
                               'BUDGET_TAB' : {'DEPT_ID', 'MANPOWER','EQUIPMENT', 'CONTINGENCY', 'CONSUMABLE'},
                               'COURSES':{'COURSE_ID', 'MIN_GPA,','SPECIAL_PERM'},
                               'STUDENT':{'STUDENT_ID','GPA'},
                               'PREREQ':{'PREREQ_ID','COURSE_ID'},
                               'ENROLMENT':{'COURSE_ID','STUDENT_ID'},
                               'PENDING_PERMISSIONS':{'COURSE_ID','STUDENT_ID'},
                               'EMP_TBL':{'SALARY','EMPID'},
                               'ACCOUNTS' : {'BALANCE','ACCT_ID'},
                               'EMPLOYEES':{'SALARY','EMPLOYEE_ID','COMMISSION_PCT'},
                               'EMP_TAB': {'EMPNO','SAL'},
                               'COUNTRY': {'ID','COUNTRY'},
                               'DRIVING_LICENSE_CATEGORY' : {'ID','CATEGORY'},
                               'ACCOUNT':{'BALANCE','ACCNO'} }) #todo: complete attributes for DELETE_TABLE
        self.functionDict = dict() #todo: complete attributes for FUNCTIONS......{"funName": ({LHS vars}, {RHS vars})}


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
        #print(res)
        #input("wait")
        return res
    
    
    
    def isAssignEq(self, ctx):
        ruleName = self.getRuleName(ctx)
        assignEqSet = {"cursor_declaration", "fetch_statement", "insert_statement", "delete_statement", "update_statement",
                       "assignment_statement", "function_call", "select_statement"}
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
            dTableName = ctx.children[2].getText()
            res = res.union(self.tableDict[dTableName])
            self.temp = set()
        elif ruleName == "update_statement":
            # self.temp = set()
            # self.visit(ctx.children[2])   #todo: maybe UPDATE SET CLAUSE
            # res = res.union(self.temp)
            # self.temp = set()
            self.temp = set()
            #self.visit(ctx.children[3])
            self.visit(ctx.children[2].children[1].children[2])     #TODO:  make it proper
            self.visit(ctx.children[3])
            res = res.union(self.temp)
            dTableName = ctx.children[1].getText()
            res = res.union(self.tableDict[dTableName])
            self.temp = set()
        elif ruleName=="select_statement":
            tempCtx = ctx.children[0].children[0]
            res = self.selectHandling(tempCtx, res)
            #print(res)
            #input("wait")
        elif ruleName == "assignment_statement":
            self.temp = set()
            self.visit(ctx.children[2])
            res = res.union(self.temp)
            self.temp = set()
        elif ruleName == "exception_handler":
            temp_ctx = ctx.children[3]
            child_count = temp_ctx.getChildCount()
            for child in range(child_count):
                if temp_ctx.children[child].getText() == ";":
                    continue
                else:
                    child_ctx = temp_ctx.children[child]
                    if self.getRuleName(child_ctx.children[0]) == "assert_statement":
                        ctx = child_ctx.children[0]
                        self.temp = set()
                        self.visit(ctx.children[1])
                        res = res.union(self.temp)
                        self.temp = set()
                    else:
                        continue
        elif ruleName == "function_call":
            pass
            #funName = ctx.children[0].getText()
            #res = res.union(self.functionDict[funName][1]) #TODO: Need to define function handling
        elif ruleName == "assume_statement":
            self.temp = set()
            self.visit(ctx.children[1])
            res = res.union(self.temp)
            self.temp = set()
            #res.add(ctx.children[1].children[0].getText())
        elif ruleName == "assert_statement":
            self.temp = set()
            self.visit(ctx.children[1])
            res = res.union(self.temp)
            self.temp = set()
            #res.add(ctx.children[1].children[0].getText())
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
                dTableName = ctx.children[1].getText()
                res = res.union(self.tableDict[dTableName])
            elif ruleName == "assignment_statement":
                self.temp = set()
                self.visit(ctx.children[0])
                res = res.union(self.temp)
                self.temp = set()
            elif ruleName == "exception_handler":
                pass
            elif ruleName == "function_call":
                pass
                #funName = ctx.children[0].getText()
                #res = res.union(self.functionDict[funName][0])

            elif ruleName == "select_statement":
                #print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4 entered in LHS select\n\n\n")
                tempCtx = ctx.children[0].children[0]
                for i in range(tempCtx.getChildCount()):
                    #print("\n\t\t\t", self.getRuleName(tempCtx.children[i]), "\n\n")
                    if self.getRuleName(tempCtx.children[i]) == "into_clause":
                        res.add(tempCtx.children[i].children[1].getText())
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
                res.add(tempCtx.children[i].getText())
                #var = self.getselected_element(tempCtx.children[i])
                #print(type(var))
                #res.add(var)
                #print(res)
                #input("wait")
            elif self.getRuleName(tempCtx.children[i]) == "from_clause":
                tableName = tempCtx.children[i].children[1].getText()
                #print(self.tableDict[tableName])
                #print(res)
                #input("wait")
                #print("**************************************************************", tableName, "\n\n\n\n\n\n\n\n\n")
                res = res.union(self.tableDict[tableName])
            elif self.getRuleName(tempCtx.children[i]) == "where_clause":
                #print("*****************************************where*********************", "\n\n\n\n\n\n\n\n\n")
                self.temp = set()
                self.visit(tempCtx.children[i].children[1])
                res = res.union(self.temp)
                self.temp = set()
        return res


    def getselected_element(self, ctx):
        tempctx = ctx.children[0]
        #print(self.getRuleName(tempctx))
        #input("wait")
        if self.getRuleName(tempctx) =="aggregate_windowed_function":
            tempagg = tempctx.children[0].getText()
            #print(self.getfunction_arguments(tempctx.children[1].children[1]))
            tempvar = self.getfunction_arguments(tempctx.children[1].children[1])

            #print(tempvar)
            #input("wait")

            aggvar = tempagg +"_"+ tempvar
            #print(aggvar)

            return aggvar
        elif self.getRuleName(tempctx) =="regular_id":
            tempvar = tempctx.getText()
            #print(tempvar)
            return tempvar
        else:
            return self.getselected_element(tempctx)



    def getfunction_arguments(self, ctx):
        ctx = ctx.children[0]
        if self.getRuleName(ctx) =="dot_id":
            temparg = str(ctx.children[0].getText()+ctx.children[2].getText())
            #print(temparg)
            #print(type(temparg))
            #input("wait")
            return temparg
        else:
            return self.getfunction_arguments(ctx)


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
