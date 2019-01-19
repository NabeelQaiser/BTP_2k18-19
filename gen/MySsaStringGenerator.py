from MyHelper import MyHelper
from gen.PlSqlVisitor import PlSqlVisitor


class MySsaStringGenerator(PlSqlVisitor):

    def __init__(self, cfg, parser):
        self.cfg = cfg
        self.parser = parser
        self.helper = MyHelper(self.parser)


    def execute(self):
        for nodeId in self.cfg.nodes:
            self.cfg.nodes[nodeId].oldString = self.getTerminal(self.cfg.nodes[nodeId].ctx)
            self.cfg.nodes[nodeId].stringSsa = self.getSsaString(nodeId)


    def getSsaString(self, nodeId):
        ctx = self.cfg.nodes[nodeId].ctx
        res = ""
        if ctx==None:
            print()
            #todo: destructed phi nodes
        else:
            ruleName = self.helper.getRuleName(ctx)
            if ruleName == "parameter":
                res = self.getParameter(nodeId, ctx)
            if ruleName == "variable_declaration":
                res = self.getVariable_declaration(nodeId, ctx)
            if ruleName == "cursor_declaration":
                res = self.getCursor_declaration(nodeId, ctx)
            if ruleName == "open_statement":
                res = self.getOpen_statement(nodeId, ctx)
            if ruleName == "fetch_statement":
                res = self.getFetch_statement(nodeId, ctx)
            if ruleName == "close_statement":
                res = self.getClose_statement(nodeId, ctx)
            if ruleName == "condition":
                res = self.getCondition(nodeId, ctx)
            if ruleName == "insert_statement":
                res = self.getInsert_statement(nodeId, ctx)
            if ruleName == "delete_statement":
                res = self.getDelete_statement(nodeId, ctx)
            if ruleName == "update_statement":
                res = self.getUpdate_statement(nodeId, ctx)
            if ruleName == "select_statement":
                res = self.getSelect_statement(nodeId, ctx)
            if ruleName == "assignment_statement":
                res = self.getAssignment_statement(nodeId, ctx)
            if ruleName == "function_call":
                res = self.getFunction_call(nodeId, ctx)
        return res



    def getParameter(self, nodeId, ctx):
        # varName = ctx.children[0].getText()
        # res = self.cfg.nodes[nodeId].versionedRHS[varName] + " " + ctx.children[1].getText() + " " + ctx.children[2].getText()
        res = self.getVersionedTerminalRHS(nodeId, ctx)
        return res

    def getVariable_declaration(self, nodeId, ctx):     # variable_declaration : variable_name CONSTANT? type_spec (NOT NULL)? default_value_part? ';'
        # varName = ctx.children[0].getText()
        # res = self.cfg.nodes[nodeId].versionedRHS[varName]
        # for i in range(1, ctx.getChildCount()-1):       # removed last ";"
        #     res = res + " " + ctx.children[i].getText()
        res = self.getVersionedTerminalRHS(nodeId, ctx)
        return res

    def getCursor_declaration(self, nodeId, ctx):
        res = "" + str(ctx.children[0]) + " "
        res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[1]) + str(ctx.children[2]) + " "
        res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[3])
        return res

    def getOpen_statement(self, nodeId, ctx):
        return self.getVersionedTerminalRHS(nodeId, ctx)

    def getFetch_statement(self, nodeId, ctx):
        res = "" + str(ctx.children[0]) + " "
        res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[1]) + str(ctx.children[2]) + " "
        res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[3])
        return res

    def getClose_statement(self, nodeId, ctx):
        return self.getVersionedTerminalRHS(nodeId, ctx)

    def getCondition(self, nodeId, ctx):
        return self.getVersionedTerminalRHS(nodeId, ctx)

    def getInsert_statement(self, nodeId, ctx):
        res = "" + str(ctx.children[0]) + " "
        res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[1].children[0])
        res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[1].children[1])
        return res

    def getDelete_statement(self, nodeId, ctx):
        return self.getVersionedTerminalRHS(nodeId, ctx)

    def getUpdate_statement(self, nodeId, ctx):
        res = "" + str(ctx.children[0]) + " " + self.getTerminal(ctx.children[1])
        res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[2])
        res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[3])   # considering WHERE is mandatory for UPDATE statement
        return res

    def getSelect_statement(self, nodeId, ctx):
        #res = "" + ctx.children[0] + " "
        return self.getVersionedTerminalRHS(nodeId, ctx)

    def getAssignment_statement(self, nodeId, ctx):
        res = ""
        res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[0]) + str(ctx.children[1]) + " "
        res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[2])
        return res

    def getFunction_call(self, nodeId, ctx):
        return "FUNCTION-CALL"


    def getVersionedTerminalRHS(self, nodeId, ctx):
        c = ctx.getChildCount()
        if c==0:
            if str(ctx) in self.cfg.nodes[nodeId].versionedRHS.keys():
                return self.cfg.nodes[nodeId].versionedRHS[str(ctx)] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalRHS(nodeId, ctx.children[i])
            return res


    def getVersionedTerminalLHS(self, nodeId, ctx):
        c = ctx.getChildCount()
        if c==0:
            if str(ctx) in self.cfg.nodes[nodeId].versionedLHS.keys():
                return self.cfg.nodes[nodeId].versionedLHS[str(ctx)] + " "
            else:
                return str(ctx) + " "
        else:
            res = ""
            for i in range(c):
                res = res + self.getVersionedTerminalLHS(nodeId, ctx.children[i])
            return res


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