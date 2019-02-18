import sys
from MyHelper import MyHelper
from gen.PlSqlVisitor import PlSqlVisitor

global vcs
vcs = " "


class CnfVcGenerator(PlSqlVisitor):

    def __init__(self, cnfCfg, parser):
        self.cnfCfg = cnfCfg
        self.parser = parser
        self.helper = MyHelper(self.parser)

    def generateCnfVc(self, path):
        global vcs
        vcs = "True"
        for node in path:
            context = self.cnfCfg.nodes[node].ctx
            nodeCondition = self.getNodeCondition(node)
            self.cnfCfg.nodes[node].antecedent = nodeCondition
            if context is not None:
                ruleName = self.helper.getRuleName(context)
                if ruleName == "condition":
                    #vcs = "AND(" + vcs + ", " + self.getCondition(node, context) + ")"
                    pass
                if ruleName == "assignment_statement":
                    #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getAssignment_statement(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(self.getAssignment_statement(node, context))
                if ruleName == "update_statement":
                    #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getUpdate_statement(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(
                        self.getUpdate_statement(node, context))
                if ruleName == "insert_statement":
                    self.cnfCfg.nodes[node].consequent = self.getInsert_statement(node, context)
                if ruleName == "cursor_declaration":
                    #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getCursor_declaration(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(
                        self.getCursor_declaration(node, context))
                if ruleName == "fetch_statement":
                    #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getFetch_statement(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(
                        self.getFetch_statement(node, context))
                if ruleName == "select_statement":
                    self.cnfCfg.nodes[node].consequent = self.getSelect_statement(node, context)       #todo: alter the function in case of insert statement
                if ruleName == "assume_statement":
                    #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getAssume_statement(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(
                        self.getAssume_statement(node, context))
                if ruleName == "assert_statement":
                    #vcs = "Implies(" + vcs + ", " + self.getAssert_statement(node, context) + ")"
                    self.cnfCfg.nodes[node].consequent.append(
                        self.getAssert_statement(node, context))
                    self.cnfCfg.nodes[node].isAssertion = True
                    self.cnfCfg.nodes[node].antecedent = [""]
                else:
                    pass
            if True:                                            #todo: rearrange it properly
                if self.cnfCfg.nodes[node].destructedPhi:
                    for element in self.cnfCfg.nodes[node].destructedPhi:
                        values = self.cnfCfg.nodes[node].destructedPhi[element]
                        #vcs = "AND(" + vcs + ", " + values[0] + " == " + values[1] + ")"
                        self.cnfCfg.nodes[node].consequent.append(values[0] + " == " + values[1])
        # print(vcs)
        return vcs

    def getNodeCondition(self, nodeId):
        res = []
        for ancestor in self.cnfCfg.nodes[nodeId].parentBranching:
            if self.cnfCfg.nodes[nodeId].parentBranching[ancestor] == "true":
                #res = "AND( " + res + ", " +  + " )"
                res.append('( ' + self.getConditionalString(nodeId, self.cnfCfg.nodes[ancestor].ctx) + ' )')
            else:
                #res = "AND( " + res + ", ""NOT( " +  + " ))"
                res.append("( ! ( " + self.getConditionalString(nodeId, self.cnfCfg.nodes[ancestor].ctx) + " ) )")
        if len(res) == 0:
            return ["( True )"]
        else:
            return res

    def getAssume_statement(self, nodeId, ctx):
        # global vcs
        res = self.getWhereexpr(nodeId, ctx.children[1])
        return res

    def getAssert_statement(self, nodeId, ctx):
        res = self.getWhereexpr(nodeId, ctx.children[1])
        return res

    def getSelect_statement(self, nodeId, ctx):
        global vcs
        nodeCondition = self.getNodeCondition(nodeId)
        res = []
        # print(ctx.children[0].children[0].getChildCount())
        # print(self.helper.getRuleName(ctx.children[0]))
        # input("Hi")
        # vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getVersionedTerminalRHS(nodeId,
        #                                                          ctx.children[0].children[0].children[1]) + "==" + \
        #       self.getInto_clause(nodeId, ctx.children[0].children[0].children[2]) + ")"
        # vcs = "AND(" + vcs + ", " + nodeCondition + ", " + self.getWhereClause(nodeId, ctx.children[0].children[0].children[4]) + ")"
        temp = "( ( ( " + self.getVersionedTerminalRHS(nodeId,ctx.children[0].children[0].children[1]) + " ) == ( " + self.getInto_clause(nodeId, ctx.children[0].children[0].children[2]) + " ) ) ^ ( " + self.getWhereClause(nodeId, ctx.children[0].children[0].children[4]) + " ) )"
        # res.append( + "==" + )
        res.append(temp)
        return res
        # input("Wait")

    def getInto_clause(self, nodeId, ctx):
        return self.getVersionedTerminalLHS(nodeId, ctx.children[1])

    def getFetch_statement(self, nodeId, ctx):
        # global vcs
        res = "( ( " + self.getVersionedTerminalRHS(nodeId, ctx.children[1]) + " ) == ( " + self.getVersionedTerminalLHS(nodeId, ctx.children[3]) + " ) )"
        return res

    def getCursor_declaration(self, nodeId, ctx):
        # global vcs
        if ctx.children[3].children[0].children[0].getChildCount() == 4:
            res = "( ( ( " + self.getVersionedTerminalLHS(nodeId, ctx.children[1]) + " ) == ( " + self.getVersionedTerminalRHS(nodeId, ctx.children[3].children[0].children[0].children[1]) + " ) ) ^ ( " + self.getWhereClause(nodeId, ctx.children[3].children[0].children[0].children[3]) + " ) )"
        else:
            res = "( ( " + self.getVersionedTerminalLHS(nodeId, ctx.children[1]) + " ) == ( " + self.getVersionedTerminalRHS(nodeId, ctx.children[3].children[0].children[0].children[1]) + " ) )"
        return res

    def getCondition(self, nodeId, ctx):

        res = self.getVersionedTerminalRHS(nodeId, ctx)
        res = res.replace("  ", " ")
        res = res.strip()
        return res

    def getAssignment_statement(self, node, ctx):
        # global vcs
        res = '( ' + self.getVersionedTerminalLHS(node, ctx.children[0]) + ' ) == ( ' + \
              self.getVersionedTerminalRHS(node, ctx.children[2]) + ' )'
        # if self.cnfCfg.nodes[node].destructedPhi:
        #     for element in self.cnfCfg.nodes[node].destructedPhi:
        #         values = self.cnfCfg.nodes[node].destructedPhi[element]

        # this
        #         res = "AND(" + res + ", " + values[0] + "==" + values[1] + ")"
        return res
        # print(vcs)

    def getUpdate_statement(self, nodeId, ctx):
        # global vcs
        # res = []
        # res = "OR(" + "AND(" + self.getSetClause(nodeId, ctx.children[2]) + "," + self.getWhereClause(nodeId, ctx.children[3]) + ")" + ", " + "AND(" + "NOT(" + self.getWhereClause(nodeId, ctx.children[3]) + ")" + ", " + self.getNotSetClause(nodeId, ctx.children[2]) + "))"
        res = "( ( ( "+ self.getSetClause(nodeId, ctx.children[2]) + " ) ^ (" + self.getWhereClause(nodeId, ctx.children[3]) + " ) ) v ( ( ! ( " + self.getWhereClause(nodeId, ctx.children[3]) + " ) ) ^ ( " + self.getNotSetClause(nodeId, ctx.children[2]) + " ) ) )"

        # res.append("OR(" + "AND(" + self.getSetClause(nodeId, ctx.children[2]) + "," \
        #       + self.getWhereClause(nodeId, ctx.children[3]) + ")" + ", " + \
        #       "AND(" + "NOT(" + self.getWhereClause(nodeId, ctx.children[3]) + ")" + ", " + \
        #       self.getNotSetClause(nodeId, ctx.children[2]) + "))")
        # if self.cnfCfg.nodes[nodeId].destructedPhi:
        #     for element in self.cnfCfg.nodes[nodeId].destructedPhi:
        #         values = self.cnfCfg.nodes[nodeId].destructedPhi[element]
        #         res = "AND(" + res + ", " + values[0] + "==" + values[1] + ")"
        return res

    def getSetClause(self, NodeId, ctx):
        child = ctx.getChildCount()
        for i in range(child):
            if self.helper.getRuleName(ctx.children[i]) == "column_based_update_set_clause":
                print(i)
        # print(child)
        # input("wait")
        res = self.getColsetClause(NodeId, ctx.children[1])
        return res

    def getColsetClause(self, nodeId, ctx):
        res = "( ( " + self.getVersionedTerminalLHS(nodeId, ctx.children[0]) + ' ) == ( ' + self.getVersionedTerminalRHS(nodeId, ctx.children[2]) + " ) )"
        return res

    def getNotSetClause(self, nodeId, ctx):
        res = self.getNotColsetClause(nodeId, ctx.children[1])
        return res

    def getNotColsetClause(self, nodeId, ctx):
        res = "( ( " + self.getVersionedTerminalLHS(nodeId, ctx.children[0]) + ' ) == ( ' + self.getVersionedTerminalRHS(nodeId, ctx.children[0]) + " ) )"
        return res

    def getWhereClause(self, nodeId, ctx):
        res = self.getWhereexpr(nodeId, ctx.children[1])
        return res

    def getWhereexpr(self, nodeId, ctx):
        # global vcs
        # opr = ctx.children[1].getText()
        # oper = self.getTerminal(ctx.children[1])
        # print(self.helper.getRuleName(ctx.children[1]))
        # print(ctx.children[1].getText())
        # temp = 'AND'
        # print(opr == temp)
        # input("hi")
        # print(type("AND"))
        # print(self.helper.getRuleName(ctx.children[1]))
        # print(self.getTerminal(ctx.children[1]))
        # input("Wait") ctx.children[1].getText()
        if ctx.children[1].getText() == "AND":
            # print(self.helper.getRuleName(ctx.children[0]))
            res = "( ( " + self.getWhereexpr(nodeId, ctx.children[0]) + " ) ^ ( " + self.getWhereexpr(nodeId, ctx.children[2]) + " ) )"
            # input("wait")

        elif ctx.children[1].getText() == "IN":
            # res =  + "==" +  + "&&" +
            res = "( ( ( " + self.getVersionedTerminalRHS(nodeId, ctx.children[0]) + " ) == ( " + self.getVersionedTerminalRHS(nodeId, ctx.children[3].children[0].children[1]) + " ) ) ^ ( " + self.getWhereexpr(nodeId, ctx.children[3].children[0].children[3].children[1]) + " ) )"
            # print(res)
            # input("Wait")
            # input("HI")

        else:
            # print(self.helper.getRuleName(ctx.children[1]))
            # print(self.getTerminal(ctx.children[1]))
            res = "( " + self.getVersionedTerminalRHS(nodeId, ctx.children[0]) + self.getTerminal(ctx.children[1]) + self.getVersionedTerminalRHS(nodeId, ctx.children[2]) + " )"
        return res
        # c = ctx.getChildCount()
        # print(self.helper.getRuleName(ctx.children[1]))
        # print(self.getTerminal(ctx.children[1]))
        # input("Enter the value")
        # res = ""
        # res = res + self.getVersionedTerminalRHS(nodeId, ctx)
        # return res
        '''
        for i in range(c):
            if ctx.children[i].getChildCount() > 1:
                res = res + self.getWhereexpr(nodeId, ctx.children[i])
        if ctx.children[0].getChildCount() == 3:
            res = ""
            res = res + "&&" + self.getWhereexpr(nodeId, ctx.children[0])
        else:
            res = self.getVersionedTerminalRHS(nodeId, ctx)
        '''
        # print(self.helper.getRuleName(ctx.children[0].children[0]))
        # print(ctx.children[0].children[2].getChildCount())
        # input('enter the vlue')
        # if self.helper.getRuleName(ctx) == "RelExpr":
        # return res
        # res = self.getVersionedTerminalRHS(nodeId, ctx.children[0]) +' == '+ \
        # self.getVersionedTerminalRHS(nodeId, ctx.children[2])

    def getInsert_statement(self, nodeId, ctx):
        global vcs
        return self.getInsertIntoandValueClause(nodeId, ctx.children[1])
        #return vcs

    def getInsertIntoandValueClause(self, nodeId, ctx):
        global vcs
        nodeCondition = self.getNodeCondition(nodeId)
        colmnlistinto = []
        colmnlistvalues = []
        res = []
        c1 = ctx.children[0].getChildCount()
        for item in range(c1):
            if self.helper.getRuleName(ctx.children[0].children[item]) == "column_name":
                # pass
                colmnlistinto.append(self.getVersionedTerminalLHS(nodeId, ctx.children[0].children[item]))
            else:
                pass
        c2 = ctx.children[1].children[1].getChildCount()
        for i in range(c2):
            if self.helper.getRuleName(ctx.children[1].children[1].children[i]) == "expression":
                colmnlistvalues.append(self.getVersionedTerminalRHS(nodeId, ctx.children[1].children[1].children[i]))
            else:
                pass

        for element in range(len(colmnlistinto)):
            #vcs = "AND(" + vcs + ", " + nodeCondition + ", " + colmnlistinto[element] + " == " + colmnlistvalues[element] + ")"
            res.append("( ( " + colmnlistinto[element] + " ) == ( " + colmnlistvalues[element] + " ) )")
        # print("\n\n^^^^^^^^^^^^^^^^^^Insert result^^^^^^^^^^")
        # print(len(res))
        # print("\n\n")
        return res

        # c= str(c1) + " " + str(c2)
        # return colmnlistvalues
        # return self.helper.getRuleName(ctx)

    # def getInsertValueClause(self, nodeId, ctx):
    #  pass

    def getVersionedTerminalRHS(self, nodeId, ctx):
        c = ctx.getChildCount()
        if c == 0:
            if str(ctx) in self.cnfCfg.nodes[nodeId].versionedRHS.keys():
                return self.cnfCfg.nodes[nodeId].versionedRHS[str(ctx)] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[i])
            return res

    def getVersionedTerminalLHS(self, nodeId, ctx):
        c = ctx.getChildCount()
        if c == 0:
            if str(ctx) in self.cnfCfg.nodes[nodeId].versionedLHS.keys():
                return self.cnfCfg.nodes[nodeId].versionedLHS[str(ctx)] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[i])
            return res

    def getTerminal(self, ctx):
        if ctx == None:
            return ""
        c = ctx.getChildCount()
        if c == 0:
            return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getTerminal(ctx.children[i])
            return res


    def getConditionalString(self, nodeId, ctx):   # considering only AND, OR, NOT as 'word' separator
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
                return "( " + self.getVersionedTerminalRHS(nodeId, ctx).strip() + " )"
            else:
                return self.getConditionalString(ctx.children[1])
        elif ctx.getChildCount() == 0:      # for stmts like "UPDATE --blah blah-- WHERE SingleWord;"
            return "( " + self.getVersionedTerminalRHS(nodeId, ctx).strip() + " )"