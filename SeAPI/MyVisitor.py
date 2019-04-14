import sys
from inspect import signature
from antlr4 import *
from SeAPI.gen.PlSqlLexer import PlSqlLexer
from SeAPI.gen.PlSqlParser import PlSqlParser
from SeAPI.gen.PlSqlVisitor import PlSqlVisitor

from SeAPI.MyNode import MyNode


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
        while i < childCount - 2:
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
        
    def visitAssert_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitAssume_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitRaise_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitException_handler(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#order_by_clause.
    def visitOrder_by_clause(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#order_by_elements.
    def visitOrder_by_elements(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitFor_update_options(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

    def visitFor_update_of_part(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '


    def visitLimit_clause(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#merge_statement.

    def visitMerge_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#merge_update_clause.

    def visitMerge_update_clause(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#merge_element.

    def visitMerge_element(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#merge_update_delete_part.

    def visitMerge_update_delete_part(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#merge_insert_clause.

    def visitMerge_insert_clause(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#selected_tableview.

    def visitSelected_tableview(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#lock_table_statement.

    def visitLock_table_statement(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#wait_nowait_part.

    def visitWait_nowait_part(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#lock_table_element.

    def visitLock_table_element(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#lock_mode.

    def visitLock_mode(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#general_table_ref.

    def visitGeneral_table_ref(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#static_returning_clause.

    def visitStatic_returning_clause(self, ctx):
        node = MyNode(self.nodeIdCounter, ctx)
        self.cfg.addNode(node)
        self.nodeIdCounter = self.nodeIdCounter + 1
        self.rawCFG = self.rawCFG + str(node.id) + ' '

        # Visit a parse tree produced by PlSqlParser#AndExpr.
    def visitAndExpr(self, ctx: PlSqlParser.AndExprContext):
        return self.visitChildren(ctx)

        # Visit a parse tree produced by PlSqlParser#LikeExpr.
    def visitLikeExpr(self, ctx:PlSqlParser.LikeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#RelExpr.
    def visitRelExpr(self, ctx:PlSqlParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#MemberExpr.
    def visitMemberExpr(self, ctx:PlSqlParser.MemberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#BetweenExpr.
    def visitBetweenExpr(self, ctx:PlSqlParser.BetweenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#CursorExpr.
    def visitCursorExpr(self, ctx:PlSqlParser.CursorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IsExpr.
    def visitIsExpr(self, ctx:PlSqlParser.IsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#NotExpr.
    def visitNotExpr(self, ctx:PlSqlParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#InExpr.
    def visitInExpr(self, ctx:PlSqlParser.InExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#ParenExpr.
    def visitParenExpr(self, ctx:PlSqlParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#OrExpr.
    def visitOrExpr(self, ctx:PlSqlParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#is_part.
    def visitIs_part(self, ctx:PlSqlParser.Is_partContext):
        return self.visitChildren(ctx)
    # Visit a parse tree produced by PlSqlParser#multiset_type.
    def visitMultiset_type(self, ctx:PlSqlParser.Multiset_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#relational_operator.
    def visitRelational_operator(self, ctx:PlSqlParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#like_type.
    def visitLike_type(self, ctx:PlSqlParser.Like_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#like_escape_part.
    def visitLike_escape_part(self, ctx:PlSqlParser.Like_escape_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#between_elements.
    def visitBetween_elements(self, ctx:PlSqlParser.Between_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#concatenation.
    def visitConcatenation(self, ctx:PlSqlParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#BinaryExpr.
    def visitBinaryExpr(self, ctx:PlSqlParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IgnoreBinaryExpr.
    def visitIgnoreBinaryExpr(self, ctx:PlSqlParser.IgnoreBinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#ParenBinaryExpr.
    def visitParenBinaryExpr(self, ctx:PlSqlParser.ParenBinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#interval_expression.
    def visitInterval_expression(self, ctx:PlSqlParser.Interval_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_expression.
    def visitModel_expression(self, ctx:PlSqlParser.Model_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_expression_element.
    def visitModel_expression_element(self, ctx:PlSqlParser.Model_expression_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#single_column_for_loop.
    def visitSingle_column_for_loop(self, ctx:PlSqlParser.Single_column_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_like_part.
    def visitFor_like_part(self, ctx:PlSqlParser.For_like_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_increment_decrement_type.
    def visitFor_increment_decrement_type(self, ctx:PlSqlParser.For_increment_decrement_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#multi_column_for_loop.
    def visitMulti_column_for_loop(self, ctx:PlSqlParser.Multi_column_for_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IgnoreUnaryExpr.
    def visitIgnoreUnaryExpr(self, ctx:PlSqlParser.IgnoreUnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:PlSqlParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#case_statement.
    def visitCase_statement(self, ctx:PlSqlParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#simple_case_statement.
    def visitSimple_case_statement(self, ctx:PlSqlParser.Simple_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#simple_case_when_part.
    def visitSimple_case_when_part(self, ctx:PlSqlParser.Simple_case_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#searched_case_statement.
    def visitSearched_case_statement(self, ctx:PlSqlParser.Searched_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#searched_case_when_part.
    def visitSearched_case_when_part(self, ctx:PlSqlParser.Searched_case_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#case_else_part.
    def visitCase_else_part(self, ctx:PlSqlParser.Case_else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#atom.
    def visitAtom(self, ctx:PlSqlParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#expression_or_vector.
    def visitExpression_or_vector(self, ctx:PlSqlParser.Expression_or_vectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#vector_expr.
    def visitVector_expr(self, ctx:PlSqlParser.Vector_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#quantified_expression.
    def visitQuantified_expression(self, ctx:PlSqlParser.Quantified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#AggregateCall.
    def visitAggregateCall(self, ctx:PlSqlParser.AggregateCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#TodoCall.
    def visitTodoCall(self, ctx:PlSqlParser.TodoCallContext):
        return self.visitChildren(ctx)

# Visit a parse tree produced by PlSqlParser#over_clause_keyword.
    def visitOver_clause_keyword(self, ctx:PlSqlParser.Over_clause_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#within_or_over_clause_keyword.
    def visitWithin_or_over_clause_keyword(self, ctx:PlSqlParser.Within_or_over_clause_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#standard_prediction_function_keyword.
    def visitStandard_prediction_function_keyword(self, ctx:PlSqlParser.Standard_prediction_function_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#over_clause.
    def visitOver_clause(self, ctx:PlSqlParser.Over_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#windowing_clause.
    def visitWindowing_clause(self, ctx:PlSqlParser.Windowing_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#windowing_type.
    def visitWindowing_type(self, ctx:PlSqlParser.Windowing_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#windowing_elements.
    def visitWindowing_elements(self, ctx:PlSqlParser.Windowing_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#using_clause.
    def visitUsing_clause(self, ctx:PlSqlParser.Using_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#using_element.
    def visitUsing_element(self, ctx:PlSqlParser.Using_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#collect_order_by_part.
    def visitCollect_order_by_part(self, ctx:PlSqlParser.Collect_order_by_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#within_or_over_part.
    def visitWithin_or_over_part(self, ctx:PlSqlParser.Within_or_over_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cost_matrix_clause.
    def visitCost_matrix_clause(self, ctx:PlSqlParser.Cost_matrix_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_passing_clause.
    def visitXml_passing_clause(self, ctx:PlSqlParser.Xml_passing_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_attributes_clause.
    def visitXml_attributes_clause(self, ctx:PlSqlParser.Xml_attributes_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_namespaces_clause.
    def visitXml_namespaces_clause(self, ctx:PlSqlParser.Xml_namespaces_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_table_column.
    def visitXml_table_column(self, ctx:PlSqlParser.Xml_table_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_general_default_part.
    def visitXml_general_default_part(self, ctx:PlSqlParser.Xml_general_default_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_multiuse_expression_element.
    def visitXml_multiuse_expression_element(self, ctx:PlSqlParser.Xml_multiuse_expression_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xmlroot_param_version_part.
    def visitXmlroot_param_version_part(self, ctx:PlSqlParser.Xmlroot_param_version_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xmlroot_param_standalone_part.
    def visitXmlroot_param_standalone_part(self, ctx:PlSqlParser.Xmlroot_param_standalone_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xmlserialize_param_enconding_part.
    def visitXmlserialize_param_enconding_part(self, ctx:PlSqlParser.Xmlserialize_param_enconding_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xmlserialize_param_version_part.
    def visitXmlserialize_param_version_part(self, ctx:PlSqlParser.Xmlserialize_param_version_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xmlserialize_param_ident_part.
    def visitXmlserialize_param_ident_part(self, ctx:PlSqlParser.Xmlserialize_param_ident_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sql_plus_command.
    def visitSql_plus_command(self, ctx:PlSqlParser.Sql_plus_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#whenever_command.
    def visitWhenever_command(self, ctx:PlSqlParser.Whenever_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#set_command.
    def visitSet_command(self, ctx:PlSqlParser.Set_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#exit_command.
    def visitExit_command(self, ctx:PlSqlParser.Exit_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#prompt_command.
    def visitPrompt_command(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#show_errors_command.
    def visitShow_errors_command(self, ctx:PlSqlParser.Show_errors_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#partition_extension_clause.
    def visitPartition_extension_clause(self, ctx:PlSqlParser.Partition_extension_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#column_alias.
    def visitColumn_alias(self, ctx:PlSqlParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_alias.
    def visitTable_alias(self, ctx:PlSqlParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alias_quoted_string.
    def visitAlias_quoted_string(self, ctx:PlSqlParser.Alias_quoted_stringContext):
        return self.visitChildren(ctx)

 # Visit a parse tree produced by PlSqlParser#attribute_name.
    def visitAttribute_name(self, ctx:PlSqlParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#savepoint_name.
    def visitSavepoint_name(self, ctx:PlSqlParser.Savepoint_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#rollback_segment_name.
    def visitRollback_segment_name(self, ctx:PlSqlParser.Rollback_segment_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_var_name.
    def visitTable_var_name(self, ctx:PlSqlParser.Table_var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#schema_name.
    def visitSchema_name(self, ctx:PlSqlParser.Schema_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#routine_name.
    def visitRoutine_name(self, ctx:PlSqlParser.Routine_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#package_name.
    def visitPackage_name(self, ctx:PlSqlParser.Package_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#implementation_type_name.
    def visitImplementation_type_name(self, ctx:PlSqlParser.Implementation_type_nameContext):
        return self.visitChildren(ctx)

# Visit a parse tree produced by PlSqlParser#reference_model_name.
    def visitReference_model_name(self, ctx:PlSqlParser.Reference_model_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#main_model_name.
    def visitMain_model_name(self, ctx:PlSqlParser.Main_model_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#aggregate_function_name.
    def visitAggregate_function_name(self, ctx:PlSqlParser.Aggregate_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#query_name.
    def visitQuery_name(self, ctx:PlSqlParser.Query_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#constraint_name.
    def visitConstraint_name(self, ctx:PlSqlParser.Constraint_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#label_name.
    def visitLabel_name(self, ctx:PlSqlParser.Label_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_name.
    def visitType_name(self, ctx:PlSqlParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sequence_name.
    def visitSequence_name(self, ctx:PlSqlParser.Sequence_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#exception_name.
    def visitException_name(self, ctx:PlSqlParser.Exception_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_name.
    def visitFunction_name(self, ctx:PlSqlParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#procedure_name.
    def visitProcedure_name(self, ctx:PlSqlParser.Procedure_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#trigger_name.
    def visitTrigger_name(self, ctx:PlSqlParser.Trigger_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#variable_name.
    def visitVariable_name(self, ctx:PlSqlParser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#index_name.
    def visitIndex_name(self, ctx:PlSqlParser.Index_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cursor_name.
    def visitCursor_name(self, ctx:PlSqlParser.Cursor_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#record_name.
    def visitRecord_name(self, ctx:PlSqlParser.Record_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#collection_name.
    def visitCollection_name(self, ctx:PlSqlParser.Collection_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#link_name.
    def visitLink_name(self, ctx:PlSqlParser.Link_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#column_name.
    def visitColumn_name(self, ctx:PlSqlParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#tableview_name.
    def visitTableview_name(self, ctx:PlSqlParser.Tableview_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dot_id.
    def visitDot_id(self, ctx:PlSqlParser.Dot_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#star.
    def visitStar(self, ctx:PlSqlParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#keep_clause.
    def visitKeep_clause(self, ctx:PlSqlParser.Keep_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_argument.
    def visitFunction_argument(self, ctx:PlSqlParser.Function_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_argument_analytic.
    def visitFunction_argument_analytic(self, ctx:PlSqlParser.Function_argument_analyticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_argument_modeling.
    def visitFunction_argument_modeling(self, ctx:PlSqlParser.Function_argument_modelingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#respect_or_ignore_nulls.
    def visitRespect_or_ignore_nulls(self, ctx:PlSqlParser.Respect_or_ignore_nullsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#argument.
    def visitArgument(self, ctx:PlSqlParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_spec.
    def visitType_spec(self, ctx:PlSqlParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#datatype.
    def visitDatatype(self, ctx:PlSqlParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#precision_part.
    def visitPrecision_part(self, ctx:PlSqlParser.Precision_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#native_datatype_element.
    def visitNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#bind_variable.
    def visitBind_variable(self, ctx:PlSqlParser.Bind_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#FuncCall.
    def visitFuncCall(self, ctx:PlSqlParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#Identifier.
    def visitIdentifier(self, ctx:PlSqlParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_element.
    def visitTable_element(self, ctx:PlSqlParser.Table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#constant.
    def visitConstant(self, ctx:PlSqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#numeric.
    def visitNumeric(self, ctx:PlSqlParser.NumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#numeric_negative.
    def visitNumeric_negative(self, ctx:PlSqlParser.Numeric_negativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#quoted_string.
    def visitQuoted_string(self, ctx:PlSqlParser.Quoted_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#r_id.
    def visitR_id(self, ctx:PlSqlParser.R_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#id_expression.
    def visitId_expression(self, ctx:PlSqlParser.Id_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#not_equal_op.
    def visitNot_equal_op(self, ctx:PlSqlParser.Not_equal_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#greater_than_or_equals_op.
    def visitGreater_than_or_equals_op(self, ctx:PlSqlParser.Greater_than_or_equals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#less_than_or_equals_op.
    def visitLess_than_or_equals_op(self, ctx:PlSqlParser.Less_than_or_equals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#concatenation_op.
    def visitConcatenation_op(self, ctx:PlSqlParser.Concatenation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#outer_join_sign.
    def visitOuter_join_sign(self, ctx:PlSqlParser.Outer_join_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#regular_id.
    def visitRegular_id(self, ctx:PlSqlParser.Regular_idContext):
        return self.visitChildren(ctx)


    
