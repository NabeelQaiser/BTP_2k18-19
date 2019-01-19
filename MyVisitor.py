import sys
from inspect import signature
from antlr4 import *
from gen.PlSqlLexer import PlSqlLexer
from gen.PlSqlParser import PlSqlParser
from gen.PlSqlVisitor import PlSqlVisitor

from MyNode import MyNode


class MyVisitor(PlSqlVisitor):

    def __init__(self, parser, cfg, utility):
        self.cfg = cfg
        self.parser = parser
        self.utility = utility
        self.nodeIdCounter = 0
        self.varDict = dict()
        self.cfg.addNode(MyNode(self.nodeIdCounter, None))
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = ""

    def visitSql_script(self, ctx):
        for i in range(ctx.getChildCount()-1):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitCreate_procedure_body(self, ctx):
        self.rawCFG = self.rawCFG + '[ 0 '
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])
        self.rawCFG = self.rawCFG + ' ]'

    def visitParameter(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitBody(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitSeq_of_statements(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitStatement(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitVariable_declaration(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitCursor_declaration(self, ctx):                     # TODO: discussion for further procedure : CURSOR
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitSql_statement(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitCursor_manipulation_statements(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitOpen_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitFetch_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitClose_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitIf_statement(self, ctx):
        self.rawCFG = self.rawCFG + '[ if_'
        node = MyNode(self.nodeIdCounter, ctx.children[1])      # if condition
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '
        self.rawCFG = self.rawCFG + '[ '
        self.visit(ctx.children[3])                             # if-true
        self.rawCFG = self.rawCFG + ' ] '
        childCount = ctx.getChildCount()
        i = 4
        while i < childCount - 3:
            ruleName = self.utility.helper.getRuleName(ctx.children[i])
            if ruleName == 'elsif_part':
                self.rawCFG = self.rawCFG + '[ elsif_'
                node = MyNode(self.nodeIdCounter, ctx.children[i].children[1])  # elsif condition
                self.cfg.addNode(node)
                self.nodeIdCounter = self.nodeIdCounter + 1
                self.rawCFG = self.rawCFG + str(node.id) + ' '
                self.rawCFG = self.rawCFG + '[ '
                self.visit(ctx.children[i].children[3])                         # elsif-true
                self.rawCFG = self.rawCFG + ' ] ] '
            i = i + 1
        # else parrt
        ruleName = self.utility.helper.getRuleName(ctx.children[childCount-3])
        if ruleName == 'else_part':
            self.rawCFG = self.rawCFG + '[ '
            self.visit(ctx.children[childCount-3].children[1])                         # body of else
            self.rawCFG = self.rawCFG + ' ] '
        else:
            node = MyNode(self.nodeIdCounter, None)
            self.cfg.addNode(node)
            self.nodeIdCounter = self.nodeIdCounter + 1
            self.rawCFG = self.rawCFG + ' [ '+ str(node.id) +' ] '                 # empty body of else
        self.rawCFG = self.rawCFG + ' ] '

    def visitData_manipulation_language_statements(self, ctx):
        for i in range(ctx.getChildCount()):
            if ctx.children[i].getChildCount() > 0:
                self.visit(ctx.children[i])

    def visitInsert_statement(self, ctx):                       # TODO: discussion for further procedure : INSERT_STATEMENT
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitDelete_statement(self, ctx):                       # TODO: discussion for further procedure : DELETE_STATEMENT
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitUpdate_statement(self, ctx):                       # TODO: discussion for further procedure : UPDATE_STATEMENT
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitSelect_statement(self, ctx):                       # TODO: discussion for further procedure : SELECT_STATEMENT
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitAssignment_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitFunction_call(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '