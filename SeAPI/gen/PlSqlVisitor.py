# Generated from /home/iitp/antlr-plsql/DBVC/Final-project/PlSql.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PlSqlParser import PlSqlParser
else:
    from PlSqlParser import PlSqlParser

# This class defines a complete generic visitor for a parse tree produced by PlSqlParser.

class PlSqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PlSqlParser#swallow_to_semi.
    def visitSwallow_to_semi(self, ctx:PlSqlParser.Swallow_to_semiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sql_script.
    def visitSql_script(self, ctx:PlSqlParser.Sql_scriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#unit_statement.
    def visitUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_function.
    def visitDrop_function(self, ctx:PlSqlParser.Drop_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_function.
    def visitAlter_function(self, ctx:PlSqlParser.Alter_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_function_body.
    def visitCreate_function_body(self, ctx:PlSqlParser.Create_function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#parallel_enable_clause.
    def visitParallel_enable_clause(self, ctx:PlSqlParser.Parallel_enable_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#partition_by_clause.
    def visitPartition_by_clause(self, ctx:PlSqlParser.Partition_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#result_cache_clause.
    def visitResult_cache_clause(self, ctx:PlSqlParser.Result_cache_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#relies_on_part.
    def visitRelies_on_part(self, ctx:PlSqlParser.Relies_on_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#streaming_clause.
    def visitStreaming_clause(self, ctx:PlSqlParser.Streaming_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_package.
    def visitDrop_package(self, ctx:PlSqlParser.Drop_packageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_package.
    def visitAlter_package(self, ctx:PlSqlParser.Alter_packageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_package.
    def visitCreate_package(self, ctx:PlSqlParser.Create_packageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#package_body.
    def visitPackage_body(self, ctx:PlSqlParser.Package_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#package_spec.
    def visitPackage_spec(self, ctx:PlSqlParser.Package_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#package_obj_spec.
    def visitPackage_obj_spec(self, ctx:PlSqlParser.Package_obj_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#procedure_spec.
    def visitProcedure_spec(self, ctx:PlSqlParser.Procedure_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_spec.
    def visitFunction_spec(self, ctx:PlSqlParser.Function_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#package_obj_body.
    def visitPackage_obj_body(self, ctx:PlSqlParser.Package_obj_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_procedure.
    def visitDrop_procedure(self, ctx:PlSqlParser.Drop_procedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_procedure.
    def visitAlter_procedure(self, ctx:PlSqlParser.Alter_procedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_procedure_body.
    def visitCreate_procedure_body(self, ctx:PlSqlParser.Create_procedure_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_trigger.
    def visitDrop_trigger(self, ctx:PlSqlParser.Drop_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_trigger.
    def visitAlter_trigger(self, ctx:PlSqlParser.Alter_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_trigger.
    def visitCreate_trigger(self, ctx:PlSqlParser.Create_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#trigger_follows_clause.
    def visitTrigger_follows_clause(self, ctx:PlSqlParser.Trigger_follows_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#trigger_when_clause.
    def visitTrigger_when_clause(self, ctx:PlSqlParser.Trigger_when_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#simple_dml_trigger.
    def visitSimple_dml_trigger(self, ctx:PlSqlParser.Simple_dml_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_each_row.
    def visitFor_each_row(self, ctx:PlSqlParser.For_each_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#compound_dml_trigger.
    def visitCompound_dml_trigger(self, ctx:PlSqlParser.Compound_dml_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#non_dml_trigger.
    def visitNon_dml_trigger(self, ctx:PlSqlParser.Non_dml_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#trigger_body.
    def visitTrigger_body(self, ctx:PlSqlParser.Trigger_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#routine_clause.
    def visitRoutine_clause(self, ctx:PlSqlParser.Routine_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#compound_trigger_block.
    def visitCompound_trigger_block(self, ctx:PlSqlParser.Compound_trigger_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#timing_point_section.
    def visitTiming_point_section(self, ctx:PlSqlParser.Timing_point_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#non_dml_event.
    def visitNon_dml_event(self, ctx:PlSqlParser.Non_dml_eventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dml_event_clause.
    def visitDml_event_clause(self, ctx:PlSqlParser.Dml_event_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dml_event_element.
    def visitDml_event_element(self, ctx:PlSqlParser.Dml_event_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dml_event_nested_clause.
    def visitDml_event_nested_clause(self, ctx:PlSqlParser.Dml_event_nested_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#referencing_clause.
    def visitReferencing_clause(self, ctx:PlSqlParser.Referencing_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#referencing_element.
    def visitReferencing_element(self, ctx:PlSqlParser.Referencing_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_type.
    def visitDrop_type(self, ctx:PlSqlParser.Drop_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_type.
    def visitAlter_type(self, ctx:PlSqlParser.Alter_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#compile_type_clause.
    def visitCompile_type_clause(self, ctx:PlSqlParser.Compile_type_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#replace_type_clause.
    def visitReplace_type_clause(self, ctx:PlSqlParser.Replace_type_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_method_spec.
    def visitAlter_method_spec(self, ctx:PlSqlParser.Alter_method_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_method_element.
    def visitAlter_method_element(self, ctx:PlSqlParser.Alter_method_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_attribute_definition.
    def visitAlter_attribute_definition(self, ctx:PlSqlParser.Alter_attribute_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#attribute_definition.
    def visitAttribute_definition(self, ctx:PlSqlParser.Attribute_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_collection_clauses.
    def visitAlter_collection_clauses(self, ctx:PlSqlParser.Alter_collection_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dependent_handling_clause.
    def visitDependent_handling_clause(self, ctx:PlSqlParser.Dependent_handling_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dependent_exceptions_part.
    def visitDependent_exceptions_part(self, ctx:PlSqlParser.Dependent_exceptions_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_type.
    def visitCreate_type(self, ctx:PlSqlParser.Create_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_definition.
    def visitType_definition(self, ctx:PlSqlParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#object_type_def.
    def visitObject_type_def(self, ctx:PlSqlParser.Object_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#object_as_part.
    def visitObject_as_part(self, ctx:PlSqlParser.Object_as_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#object_under_part.
    def visitObject_under_part(self, ctx:PlSqlParser.Object_under_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#nested_table_type_def.
    def visitNested_table_type_def(self, ctx:PlSqlParser.Nested_table_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sqlj_object_type.
    def visitSqlj_object_type(self, ctx:PlSqlParser.Sqlj_object_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_body.
    def visitType_body(self, ctx:PlSqlParser.Type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_body_elements.
    def visitType_body_elements(self, ctx:PlSqlParser.Type_body_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#map_order_func_declaration.
    def visitMap_order_func_declaration(self, ctx:PlSqlParser.Map_order_func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subprog_decl_in_type.
    def visitSubprog_decl_in_type(self, ctx:PlSqlParser.Subprog_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#proc_decl_in_type.
    def visitProc_decl_in_type(self, ctx:PlSqlParser.Proc_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#func_decl_in_type.
    def visitFunc_decl_in_type(self, ctx:PlSqlParser.Func_decl_in_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#constructor_declaration.
    def visitConstructor_declaration(self, ctx:PlSqlParser.Constructor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#modifier_clause.
    def visitModifier_clause(self, ctx:PlSqlParser.Modifier_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#object_member_spec.
    def visitObject_member_spec(self, ctx:PlSqlParser.Object_member_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sqlj_object_type_attr.
    def visitSqlj_object_type_attr(self, ctx:PlSqlParser.Sqlj_object_type_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#element_spec.
    def visitElement_spec(self, ctx:PlSqlParser.Element_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#element_spec_options.
    def visitElement_spec_options(self, ctx:PlSqlParser.Element_spec_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subprogram_spec.
    def visitSubprogram_spec(self, ctx:PlSqlParser.Subprogram_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_procedure_spec.
    def visitType_procedure_spec(self, ctx:PlSqlParser.Type_procedure_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_function_spec.
    def visitType_function_spec(self, ctx:PlSqlParser.Type_function_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#constructor_spec.
    def visitConstructor_spec(self, ctx:PlSqlParser.Constructor_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#map_order_function_spec.
    def visitMap_order_function_spec(self, ctx:PlSqlParser.Map_order_function_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pragma_clause.
    def visitPragma_clause(self, ctx:PlSqlParser.Pragma_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pragma_elements.
    def visitPragma_elements(self, ctx:PlSqlParser.Pragma_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#type_elements_parameter.
    def visitType_elements_parameter(self, ctx:PlSqlParser.Type_elements_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#drop_sequence.
    def visitDrop_sequence(self, ctx:PlSqlParser.Drop_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#alter_sequence.
    def visitAlter_sequence(self, ctx:PlSqlParser.Alter_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#create_sequence.
    def visitCreate_sequence(self, ctx:PlSqlParser.Create_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sequence_spec.
    def visitSequence_spec(self, ctx:PlSqlParser.Sequence_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sequence_start_clause.
    def visitSequence_start_clause(self, ctx:PlSqlParser.Sequence_start_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#invoker_rights_clause.
    def visitInvoker_rights_clause(self, ctx:PlSqlParser.Invoker_rights_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#compiler_parameters_clause.
    def visitCompiler_parameters_clause(self, ctx:PlSqlParser.Compiler_parameters_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#call_spec.
    def visitCall_spec(self, ctx:PlSqlParser.Call_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#java_spec.
    def visitJava_spec(self, ctx:PlSqlParser.Java_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#c_spec.
    def visitC_spec(self, ctx:PlSqlParser.C_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#c_agent_in_clause.
    def visitC_agent_in_clause(self, ctx:PlSqlParser.C_agent_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#c_parameters_clause.
    def visitC_parameters_clause(self, ctx:PlSqlParser.C_parameters_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#parameter.
    def visitParameter(self, ctx:PlSqlParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#default_value_part.
    def visitDefault_value_part(self, ctx:PlSqlParser.Default_value_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#declare_spec.
    def visitDeclare_spec(self, ctx:PlSqlParser.Declare_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#variable_declaration.
    def visitVariable_declaration(self, ctx:PlSqlParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subtype_declaration.
    def visitSubtype_declaration(self, ctx:PlSqlParser.Subtype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cursor_declaration.
    def visitCursor_declaration(self, ctx:PlSqlParser.Cursor_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#parameter_spec.
    def visitParameter_spec(self, ctx:PlSqlParser.Parameter_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#exception_declaration.
    def visitException_declaration(self, ctx:PlSqlParser.Exception_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pragma_declaration.
    def visitPragma_declaration(self, ctx:PlSqlParser.Pragma_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#record_declaration.
    def visitRecord_declaration(self, ctx:PlSqlParser.Record_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#record_type_dec.
    def visitRecord_type_dec(self, ctx:PlSqlParser.Record_type_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#field_spec.
    def visitField_spec(self, ctx:PlSqlParser.Field_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#record_var_dec.
    def visitRecord_var_dec(self, ctx:PlSqlParser.Record_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_declaration.
    def visitTable_declaration(self, ctx:PlSqlParser.Table_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_type_dec.
    def visitTable_type_dec(self, ctx:PlSqlParser.Table_type_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_indexed_by_part.
    def visitTable_indexed_by_part(self, ctx:PlSqlParser.Table_indexed_by_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#varray_type_def.
    def visitVarray_type_def(self, ctx:PlSqlParser.Varray_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_var_dec.
    def visitTable_var_dec(self, ctx:PlSqlParser.Table_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#seq_of_statements.
    def visitSeq_of_statements(self, ctx:PlSqlParser.Seq_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#label_declaration.
    def visitLabel_declaration(self, ctx:PlSqlParser.Label_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#statement.
    def visitStatement(self, ctx:PlSqlParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#assume_statement.
    def visitAssume_statement(self, ctx:PlSqlParser.Assume_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#assert_statement.
    def visitAssert_statement(self, ctx:PlSqlParser.Assert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#assignment_statement.
    def visitAssignment_statement(self, ctx:PlSqlParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#continue_statement.
    def visitContinue_statement(self, ctx:PlSqlParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#exit_statement.
    def visitExit_statement(self, ctx:PlSqlParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#goto_statement.
    def visitGoto_statement(self, ctx:PlSqlParser.Goto_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#if_statement.
    def visitIf_statement(self, ctx:PlSqlParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#elsif_part.
    def visitElsif_part(self, ctx:PlSqlParser.Elsif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#else_part.
    def visitElse_part(self, ctx:PlSqlParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#loop_statement.
    def visitLoop_statement(self, ctx:PlSqlParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cursor_loop_param.
    def visitCursor_loop_param(self, ctx:PlSqlParser.Cursor_loop_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#forall_statement.
    def visitForall_statement(self, ctx:PlSqlParser.Forall_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#bounds_clause.
    def visitBounds_clause(self, ctx:PlSqlParser.Bounds_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#between_bound.
    def visitBetween_bound(self, ctx:PlSqlParser.Between_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#lower_bound.
    def visitLower_bound(self, ctx:PlSqlParser.Lower_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#upper_bound.
    def visitUpper_bound(self, ctx:PlSqlParser.Upper_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#null_statement.
    def visitNull_statement(self, ctx:PlSqlParser.Null_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#raise_statement.
    def visitRaise_statement(self, ctx:PlSqlParser.Raise_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#return_statement.
    def visitReturn_statement(self, ctx:PlSqlParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#function_call.
    def visitFunction_call(self, ctx:PlSqlParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#body.
    def visitBody(self, ctx:PlSqlParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#exception_handler.
    def visitException_handler(self, ctx:PlSqlParser.Exception_handlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#trigger_block.
    def visitTrigger_block(self, ctx:PlSqlParser.Trigger_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#block.
    def visitBlock(self, ctx:PlSqlParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sql_statement.
    def visitSql_statement(self, ctx:PlSqlParser.Sql_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#execute_immediate.
    def visitExecute_immediate(self, ctx:PlSqlParser.Execute_immediateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dynamic_returning_clause.
    def visitDynamic_returning_clause(self, ctx:PlSqlParser.Dynamic_returning_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#data_manipulation_language_statements.
    def visitData_manipulation_language_statements(self, ctx:PlSqlParser.Data_manipulation_language_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cursor_manipulation_statements.
    def visitCursor_manipulation_statements(self, ctx:PlSqlParser.Cursor_manipulation_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#close_statement.
    def visitClose_statement(self, ctx:PlSqlParser.Close_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#open_statement.
    def visitOpen_statement(self, ctx:PlSqlParser.Open_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#fetch_statement.
    def visitFetch_statement(self, ctx:PlSqlParser.Fetch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#open_for_statement.
    def visitOpen_for_statement(self, ctx:PlSqlParser.Open_for_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#transaction_control_statements.
    def visitTransaction_control_statements(self, ctx:PlSqlParser.Transaction_control_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#set_transaction_command.
    def visitSet_transaction_command(self, ctx:PlSqlParser.Set_transaction_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#set_constraint_command.
    def visitSet_constraint_command(self, ctx:PlSqlParser.Set_constraint_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#commit_statement.
    def visitCommit_statement(self, ctx:PlSqlParser.Commit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#write_clause.
    def visitWrite_clause(self, ctx:PlSqlParser.Write_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#rollback_statement.
    def visitRollback_statement(self, ctx:PlSqlParser.Rollback_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#savepoint_statement.
    def visitSavepoint_statement(self, ctx:PlSqlParser.Savepoint_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#explain_statement.
    def visitExplain_statement(self, ctx:PlSqlParser.Explain_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#select_statement.
    def visitSelect_statement(self, ctx:PlSqlParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subquery_factoring_clause.
    def visitSubquery_factoring_clause(self, ctx:PlSqlParser.Subquery_factoring_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#factoring_element.
    def visitFactoring_element(self, ctx:PlSqlParser.Factoring_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#search_clause.
    def visitSearch_clause(self, ctx:PlSqlParser.Search_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cycle_clause.
    def visitCycle_clause(self, ctx:PlSqlParser.Cycle_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#SubqueryParen.
    def visitSubqueryParen(self, ctx:PlSqlParser.SubqueryParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IgnoreSubquery.
    def visitIgnoreSubquery(self, ctx:PlSqlParser.IgnoreSubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#SubqueryCompound.
    def visitSubqueryCompound(self, ctx:PlSqlParser.SubqueryCompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subquery_operation_part.
    def visitSubquery_operation_part(self, ctx:PlSqlParser.Subquery_operation_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#query_block.
    def visitQuery_block(self, ctx:PlSqlParser.Query_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#Star1.
    def visitStar1(self, ctx:PlSqlParser.Star1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#StarTable.
    def visitStarTable(self, ctx:PlSqlParser.StarTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IgnoreTableview_name.
    def visitIgnoreTableview_name(self, ctx:PlSqlParser.IgnoreTableview_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#Alias_expr.
    def visitAlias_expr(self, ctx:PlSqlParser.Alias_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#from_clause.
    def visitFrom_clause(self, ctx:PlSqlParser.From_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_ref_pivot.
    def visitTable_ref_pivot(self, ctx:PlSqlParser.Table_ref_pivotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#JoinExpr.
    def visitJoinExpr(self, ctx:PlSqlParser.JoinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#TableRefSimple.
    def visitTableRefSimple(self, ctx:PlSqlParser.TableRefSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#TableRefAux.
    def visitTableRefAux(self, ctx:PlSqlParser.TableRefAuxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_ref_aux.
    def visitTable_ref_aux(self, ctx:PlSqlParser.Table_ref_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#join_clause.
    def visitJoin_clause(self, ctx:PlSqlParser.Join_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#join_on_part.
    def visitJoin_on_part(self, ctx:PlSqlParser.Join_on_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#join_using_part.
    def visitJoin_using_part(self, ctx:PlSqlParser.Join_using_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#join_type.
    def visitJoin_type(self, ctx:PlSqlParser.Join_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#query_partition_clause.
    def visitQuery_partition_clause(self, ctx:PlSqlParser.Query_partition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#flashback_query_clause.
    def visitFlashback_query_clause(self, ctx:PlSqlParser.Flashback_query_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_clause.
    def visitPivot_clause(self, ctx:PlSqlParser.Pivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_element.
    def visitPivot_element(self, ctx:PlSqlParser.Pivot_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_for_clause.
    def visitPivot_for_clause(self, ctx:PlSqlParser.Pivot_for_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_in_clause.
    def visitPivot_in_clause(self, ctx:PlSqlParser.Pivot_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_in_clause_element.
    def visitPivot_in_clause_element(self, ctx:PlSqlParser.Pivot_in_clause_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#pivot_in_clause_elements.
    def visitPivot_in_clause_elements(self, ctx:PlSqlParser.Pivot_in_clause_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#unpivot_clause.
    def visitUnpivot_clause(self, ctx:PlSqlParser.Unpivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#unpivot_in_clause.
    def visitUnpivot_in_clause(self, ctx:PlSqlParser.Unpivot_in_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#unpivot_in_elements.
    def visitUnpivot_in_elements(self, ctx:PlSqlParser.Unpivot_in_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#hierarchical_query_clause.
    def visitHierarchical_query_clause(self, ctx:PlSqlParser.Hierarchical_query_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#start_part.
    def visitStart_part(self, ctx:PlSqlParser.Start_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#group_by_clause.
    def visitGroup_by_clause(self, ctx:PlSqlParser.Group_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#group_by_elements.
    def visitGroup_by_elements(self, ctx:PlSqlParser.Group_by_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#rollup_cube_clause.
    def visitRollup_cube_clause(self, ctx:PlSqlParser.Rollup_cube_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#grouping_sets_clause.
    def visitGrouping_sets_clause(self, ctx:PlSqlParser.Grouping_sets_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#grouping_sets_elements.
    def visitGrouping_sets_elements(self, ctx:PlSqlParser.Grouping_sets_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#having_clause.
    def visitHaving_clause(self, ctx:PlSqlParser.Having_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_clause.
    def visitModel_clause(self, ctx:PlSqlParser.Model_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cell_reference_options.
    def visitCell_reference_options(self, ctx:PlSqlParser.Cell_reference_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#return_rows_clause.
    def visitReturn_rows_clause(self, ctx:PlSqlParser.Return_rows_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#reference_model.
    def visitReference_model(self, ctx:PlSqlParser.Reference_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#main_model.
    def visitMain_model(self, ctx:PlSqlParser.Main_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_column_clauses.
    def visitModel_column_clauses(self, ctx:PlSqlParser.Model_column_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_column_partition_part.
    def visitModel_column_partition_part(self, ctx:PlSqlParser.Model_column_partition_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_column_list.
    def visitModel_column_list(self, ctx:PlSqlParser.Model_column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_column.
    def visitModel_column(self, ctx:PlSqlParser.Model_columnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_rules_clause.
    def visitModel_rules_clause(self, ctx:PlSqlParser.Model_rules_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_rules_part.
    def visitModel_rules_part(self, ctx:PlSqlParser.Model_rules_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_rules_element.
    def visitModel_rules_element(self, ctx:PlSqlParser.Model_rules_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cell_assignment.
    def visitCell_assignment(self, ctx:PlSqlParser.Cell_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#model_iterate_clause.
    def visitModel_iterate_clause(self, ctx:PlSqlParser.Model_iterate_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#until_part.
    def visitUntil_part(self, ctx:PlSqlParser.Until_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:PlSqlParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#order_by_elements.
    def visitOrder_by_elements(self, ctx:PlSqlParser.Order_by_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_update_clause.
    def visitFor_update_clause(self, ctx:PlSqlParser.For_update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_update_of_part.
    def visitFor_update_of_part(self, ctx:PlSqlParser.For_update_of_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#for_update_options.
    def visitFor_update_options(self, ctx:PlSqlParser.For_update_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#limit_clause.
    def visitLimit_clause(self, ctx:PlSqlParser.Limit_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#update_statement.
    def visitUpdate_statement(self, ctx:PlSqlParser.Update_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#update_set_clause.
    def visitUpdate_set_clause(self, ctx:PlSqlParser.Update_set_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#column_based_update_set_clause.
    def visitColumn_based_update_set_clause(self, ctx:PlSqlParser.Column_based_update_set_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#delete_statement.
    def visitDelete_statement(self, ctx:PlSqlParser.Delete_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#insert_statement.
    def visitInsert_statement(self, ctx:PlSqlParser.Insert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#single_table_insert.
    def visitSingle_table_insert(self, ctx:PlSqlParser.Single_table_insertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#multi_table_insert.
    def visitMulti_table_insert(self, ctx:PlSqlParser.Multi_table_insertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#multi_table_element.
    def visitMulti_table_element(self, ctx:PlSqlParser.Multi_table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#conditional_insert_clause.
    def visitConditional_insert_clause(self, ctx:PlSqlParser.Conditional_insert_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#conditional_insert_when_part.
    def visitConditional_insert_when_part(self, ctx:PlSqlParser.Conditional_insert_when_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#conditional_insert_else_part.
    def visitConditional_insert_else_part(self, ctx:PlSqlParser.Conditional_insert_else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#insert_into_clause.
    def visitInsert_into_clause(self, ctx:PlSqlParser.Insert_into_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#values_clause.
    def visitValues_clause(self, ctx:PlSqlParser.Values_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#merge_statement.
    def visitMerge_statement(self, ctx:PlSqlParser.Merge_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#merge_update_clause.
    def visitMerge_update_clause(self, ctx:PlSqlParser.Merge_update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#merge_element.
    def visitMerge_element(self, ctx:PlSqlParser.Merge_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#merge_update_delete_part.
    def visitMerge_update_delete_part(self, ctx:PlSqlParser.Merge_update_delete_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#merge_insert_clause.
    def visitMerge_insert_clause(self, ctx:PlSqlParser.Merge_insert_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#selected_tableview.
    def visitSelected_tableview(self, ctx:PlSqlParser.Selected_tableviewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#lock_table_statement.
    def visitLock_table_statement(self, ctx:PlSqlParser.Lock_table_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#wait_nowait_part.
    def visitWait_nowait_part(self, ctx:PlSqlParser.Wait_nowait_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#lock_table_element.
    def visitLock_table_element(self, ctx:PlSqlParser.Lock_table_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#lock_mode.
    def visitLock_mode(self, ctx:PlSqlParser.Lock_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#general_table_ref.
    def visitGeneral_table_ref(self, ctx:PlSqlParser.General_table_refContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#static_returning_clause.
    def visitStatic_returning_clause(self, ctx:PlSqlParser.Static_returning_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#error_logging_clause.
    def visitError_logging_clause(self, ctx:PlSqlParser.Error_logging_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#error_logging_into_part.
    def visitError_logging_into_part(self, ctx:PlSqlParser.Error_logging_into_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#error_logging_reject_part.
    def visitError_logging_reject_part(self, ctx:PlSqlParser.Error_logging_reject_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#dml_table_expression_clause.
    def visitDml_table_expression_clause(self, ctx:PlSqlParser.Dml_table_expression_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#table_collection_expression.
    def visitTable_collection_expression(self, ctx:PlSqlParser.Table_collection_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#subquery_restriction_clause.
    def visitSubquery_restriction_clause(self, ctx:PlSqlParser.Subquery_restriction_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#sample_clause.
    def visitSample_clause(self, ctx:PlSqlParser.Sample_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#seed_part.
    def visitSeed_part(self, ctx:PlSqlParser.Seed_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cursor_expression.
    def visitCursor_expression(self, ctx:PlSqlParser.Cursor_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#expression_list.
    def visitExpression_list(self, ctx:PlSqlParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#condition.
    def visitCondition(self, ctx:PlSqlParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#IgnoreExpr.
    def visitIgnoreExpr(self, ctx:PlSqlParser.IgnoreExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#AndExpr.
    def visitAndExpr(self, ctx:PlSqlParser.AndExprContext):
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


    # Visit a parse tree produced by PlSqlParser#cursor_part.
    def visitCursor_part(self, ctx:PlSqlParser.Cursor_partContext):
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


    # Visit a parse tree produced by PlSqlParser#XmlCall.
    def visitXmlCall(self, ctx:PlSqlParser.XmlCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#aggregate_windowed_function.
    def visitAggregate_windowed_function(self, ctx:PlSqlParser.Aggregate_windowed_functionContext):
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
    def visitPrompt_command(self, ctx:PlSqlParser.Prompt_commandContext):
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


    # Visit a parse tree produced by PlSqlParser#where_clause.
    def visitWhere_clause(self, ctx:PlSqlParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#current_of_clause.
    def visitCurrent_of_clause(self, ctx:PlSqlParser.Current_of_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#into_clause.
    def visitInto_clause(self, ctx:PlSqlParser.Into_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#xml_column_name.
    def visitXml_column_name(self, ctx:PlSqlParser.Xml_column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PlSqlParser#cost_class_name.
    def visitCost_class_name(self, ctx:PlSqlParser.Cost_class_nameContext):
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


    # Visit a parse tree produced by PlSqlParser#parameter_name.
    def visitParameter_name(self, ctx:PlSqlParser.Parameter_nameContext):
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



del PlSqlParser