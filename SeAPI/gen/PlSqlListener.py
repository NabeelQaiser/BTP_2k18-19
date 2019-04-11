# Generated from /home/iitp/antlr-plsql/DBVC/Final-project/PlSql.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PlSqlParser import PlSqlParser
else:
    from PlSqlParser import PlSqlParser

# This class defines a complete listener for a parse tree produced by PlSqlParser.
class PlSqlListener(ParseTreeListener):

    # Enter a parse tree produced by PlSqlParser#swallow_to_semi.
    def enterSwallow_to_semi(self, ctx:PlSqlParser.Swallow_to_semiContext):
        pass

    # Exit a parse tree produced by PlSqlParser#swallow_to_semi.
    def exitSwallow_to_semi(self, ctx:PlSqlParser.Swallow_to_semiContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_script.
    def enterSql_script(self, ctx:PlSqlParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_script.
    def exitSql_script(self, ctx:PlSqlParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unit_statement.
    def enterUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unit_statement.
    def exitUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_function.
    def enterDrop_function(self, ctx:PlSqlParser.Drop_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_function.
    def exitDrop_function(self, ctx:PlSqlParser.Drop_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_function.
    def enterAlter_function(self, ctx:PlSqlParser.Alter_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_function.
    def exitAlter_function(self, ctx:PlSqlParser.Alter_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_function_body.
    def enterCreate_function_body(self, ctx:PlSqlParser.Create_function_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_function_body.
    def exitCreate_function_body(self, ctx:PlSqlParser.Create_function_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parallel_enable_clause.
    def enterParallel_enable_clause(self, ctx:PlSqlParser.Parallel_enable_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parallel_enable_clause.
    def exitParallel_enable_clause(self, ctx:PlSqlParser.Parallel_enable_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_by_clause.
    def enterPartition_by_clause(self, ctx:PlSqlParser.Partition_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_by_clause.
    def exitPartition_by_clause(self, ctx:PlSqlParser.Partition_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#result_cache_clause.
    def enterResult_cache_clause(self, ctx:PlSqlParser.Result_cache_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#result_cache_clause.
    def exitResult_cache_clause(self, ctx:PlSqlParser.Result_cache_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relies_on_part.
    def enterRelies_on_part(self, ctx:PlSqlParser.Relies_on_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relies_on_part.
    def exitRelies_on_part(self, ctx:PlSqlParser.Relies_on_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#streaming_clause.
    def enterStreaming_clause(self, ctx:PlSqlParser.Streaming_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#streaming_clause.
    def exitStreaming_clause(self, ctx:PlSqlParser.Streaming_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_package.
    def enterDrop_package(self, ctx:PlSqlParser.Drop_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_package.
    def exitDrop_package(self, ctx:PlSqlParser.Drop_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_package.
    def enterAlter_package(self, ctx:PlSqlParser.Alter_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_package.
    def exitAlter_package(self, ctx:PlSqlParser.Alter_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_package.
    def enterCreate_package(self, ctx:PlSqlParser.Create_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_package.
    def exitCreate_package(self, ctx:PlSqlParser.Create_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_body.
    def enterPackage_body(self, ctx:PlSqlParser.Package_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_body.
    def exitPackage_body(self, ctx:PlSqlParser.Package_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_spec.
    def enterPackage_spec(self, ctx:PlSqlParser.Package_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_spec.
    def exitPackage_spec(self, ctx:PlSqlParser.Package_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_obj_spec.
    def enterPackage_obj_spec(self, ctx:PlSqlParser.Package_obj_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_obj_spec.
    def exitPackage_obj_spec(self, ctx:PlSqlParser.Package_obj_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#procedure_spec.
    def enterProcedure_spec(self, ctx:PlSqlParser.Procedure_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#procedure_spec.
    def exitProcedure_spec(self, ctx:PlSqlParser.Procedure_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_spec.
    def enterFunction_spec(self, ctx:PlSqlParser.Function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_spec.
    def exitFunction_spec(self, ctx:PlSqlParser.Function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_obj_body.
    def enterPackage_obj_body(self, ctx:PlSqlParser.Package_obj_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_obj_body.
    def exitPackage_obj_body(self, ctx:PlSqlParser.Package_obj_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_procedure.
    def enterDrop_procedure(self, ctx:PlSqlParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_procedure.
    def exitDrop_procedure(self, ctx:PlSqlParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_procedure.
    def enterAlter_procedure(self, ctx:PlSqlParser.Alter_procedureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_procedure.
    def exitAlter_procedure(self, ctx:PlSqlParser.Alter_procedureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_procedure_body.
    def enterCreate_procedure_body(self, ctx:PlSqlParser.Create_procedure_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_procedure_body.
    def exitCreate_procedure_body(self, ctx:PlSqlParser.Create_procedure_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_trigger.
    def enterDrop_trigger(self, ctx:PlSqlParser.Drop_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_trigger.
    def exitDrop_trigger(self, ctx:PlSqlParser.Drop_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_trigger.
    def enterAlter_trigger(self, ctx:PlSqlParser.Alter_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_trigger.
    def exitAlter_trigger(self, ctx:PlSqlParser.Alter_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_trigger.
    def enterCreate_trigger(self, ctx:PlSqlParser.Create_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_trigger.
    def exitCreate_trigger(self, ctx:PlSqlParser.Create_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_follows_clause.
    def enterTrigger_follows_clause(self, ctx:PlSqlParser.Trigger_follows_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_follows_clause.
    def exitTrigger_follows_clause(self, ctx:PlSqlParser.Trigger_follows_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_when_clause.
    def enterTrigger_when_clause(self, ctx:PlSqlParser.Trigger_when_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_when_clause.
    def exitTrigger_when_clause(self, ctx:PlSqlParser.Trigger_when_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_dml_trigger.
    def enterSimple_dml_trigger(self, ctx:PlSqlParser.Simple_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_dml_trigger.
    def exitSimple_dml_trigger(self, ctx:PlSqlParser.Simple_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_each_row.
    def enterFor_each_row(self, ctx:PlSqlParser.For_each_rowContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_each_row.
    def exitFor_each_row(self, ctx:PlSqlParser.For_each_rowContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compound_dml_trigger.
    def enterCompound_dml_trigger(self, ctx:PlSqlParser.Compound_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compound_dml_trigger.
    def exitCompound_dml_trigger(self, ctx:PlSqlParser.Compound_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_dml_trigger.
    def enterNon_dml_trigger(self, ctx:PlSqlParser.Non_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_dml_trigger.
    def exitNon_dml_trigger(self, ctx:PlSqlParser.Non_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_body.
    def enterTrigger_body(self, ctx:PlSqlParser.Trigger_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_body.
    def exitTrigger_body(self, ctx:PlSqlParser.Trigger_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#routine_clause.
    def enterRoutine_clause(self, ctx:PlSqlParser.Routine_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#routine_clause.
    def exitRoutine_clause(self, ctx:PlSqlParser.Routine_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compound_trigger_block.
    def enterCompound_trigger_block(self, ctx:PlSqlParser.Compound_trigger_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compound_trigger_block.
    def exitCompound_trigger_block(self, ctx:PlSqlParser.Compound_trigger_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#timing_point_section.
    def enterTiming_point_section(self, ctx:PlSqlParser.Timing_point_sectionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#timing_point_section.
    def exitTiming_point_section(self, ctx:PlSqlParser.Timing_point_sectionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_dml_event.
    def enterNon_dml_event(self, ctx:PlSqlParser.Non_dml_eventContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_dml_event.
    def exitNon_dml_event(self, ctx:PlSqlParser.Non_dml_eventContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_clause.
    def enterDml_event_clause(self, ctx:PlSqlParser.Dml_event_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_clause.
    def exitDml_event_clause(self, ctx:PlSqlParser.Dml_event_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_element.
    def enterDml_event_element(self, ctx:PlSqlParser.Dml_event_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_element.
    def exitDml_event_element(self, ctx:PlSqlParser.Dml_event_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_nested_clause.
    def enterDml_event_nested_clause(self, ctx:PlSqlParser.Dml_event_nested_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_nested_clause.
    def exitDml_event_nested_clause(self, ctx:PlSqlParser.Dml_event_nested_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#referencing_clause.
    def enterReferencing_clause(self, ctx:PlSqlParser.Referencing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#referencing_clause.
    def exitReferencing_clause(self, ctx:PlSqlParser.Referencing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#referencing_element.
    def enterReferencing_element(self, ctx:PlSqlParser.Referencing_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#referencing_element.
    def exitReferencing_element(self, ctx:PlSqlParser.Referencing_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_type.
    def enterDrop_type(self, ctx:PlSqlParser.Drop_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_type.
    def exitDrop_type(self, ctx:PlSqlParser.Drop_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_type.
    def enterAlter_type(self, ctx:PlSqlParser.Alter_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_type.
    def exitAlter_type(self, ctx:PlSqlParser.Alter_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compile_type_clause.
    def enterCompile_type_clause(self, ctx:PlSqlParser.Compile_type_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compile_type_clause.
    def exitCompile_type_clause(self, ctx:PlSqlParser.Compile_type_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#replace_type_clause.
    def enterReplace_type_clause(self, ctx:PlSqlParser.Replace_type_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#replace_type_clause.
    def exitReplace_type_clause(self, ctx:PlSqlParser.Replace_type_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_method_spec.
    def enterAlter_method_spec(self, ctx:PlSqlParser.Alter_method_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_method_spec.
    def exitAlter_method_spec(self, ctx:PlSqlParser.Alter_method_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_method_element.
    def enterAlter_method_element(self, ctx:PlSqlParser.Alter_method_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_method_element.
    def exitAlter_method_element(self, ctx:PlSqlParser.Alter_method_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_attribute_definition.
    def enterAlter_attribute_definition(self, ctx:PlSqlParser.Alter_attribute_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_attribute_definition.
    def exitAlter_attribute_definition(self, ctx:PlSqlParser.Alter_attribute_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_definition.
    def enterAttribute_definition(self, ctx:PlSqlParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_definition.
    def exitAttribute_definition(self, ctx:PlSqlParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_collection_clauses.
    def enterAlter_collection_clauses(self, ctx:PlSqlParser.Alter_collection_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_collection_clauses.
    def exitAlter_collection_clauses(self, ctx:PlSqlParser.Alter_collection_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dependent_handling_clause.
    def enterDependent_handling_clause(self, ctx:PlSqlParser.Dependent_handling_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dependent_handling_clause.
    def exitDependent_handling_clause(self, ctx:PlSqlParser.Dependent_handling_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dependent_exceptions_part.
    def enterDependent_exceptions_part(self, ctx:PlSqlParser.Dependent_exceptions_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dependent_exceptions_part.
    def exitDependent_exceptions_part(self, ctx:PlSqlParser.Dependent_exceptions_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_type.
    def enterCreate_type(self, ctx:PlSqlParser.Create_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_type.
    def exitCreate_type(self, ctx:PlSqlParser.Create_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_definition.
    def enterType_definition(self, ctx:PlSqlParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_definition.
    def exitType_definition(self, ctx:PlSqlParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_type_def.
    def enterObject_type_def(self, ctx:PlSqlParser.Object_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_type_def.
    def exitObject_type_def(self, ctx:PlSqlParser.Object_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_as_part.
    def enterObject_as_part(self, ctx:PlSqlParser.Object_as_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_as_part.
    def exitObject_as_part(self, ctx:PlSqlParser.Object_as_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_under_part.
    def enterObject_under_part(self, ctx:PlSqlParser.Object_under_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_under_part.
    def exitObject_under_part(self, ctx:PlSqlParser.Object_under_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#nested_table_type_def.
    def enterNested_table_type_def(self, ctx:PlSqlParser.Nested_table_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#nested_table_type_def.
    def exitNested_table_type_def(self, ctx:PlSqlParser.Nested_table_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sqlj_object_type.
    def enterSqlj_object_type(self, ctx:PlSqlParser.Sqlj_object_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sqlj_object_type.
    def exitSqlj_object_type(self, ctx:PlSqlParser.Sqlj_object_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_body.
    def enterType_body(self, ctx:PlSqlParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_body.
    def exitType_body(self, ctx:PlSqlParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_body_elements.
    def enterType_body_elements(self, ctx:PlSqlParser.Type_body_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_body_elements.
    def exitType_body_elements(self, ctx:PlSqlParser.Type_body_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#map_order_func_declaration.
    def enterMap_order_func_declaration(self, ctx:PlSqlParser.Map_order_func_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#map_order_func_declaration.
    def exitMap_order_func_declaration(self, ctx:PlSqlParser.Map_order_func_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subprog_decl_in_type.
    def enterSubprog_decl_in_type(self, ctx:PlSqlParser.Subprog_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subprog_decl_in_type.
    def exitSubprog_decl_in_type(self, ctx:PlSqlParser.Subprog_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#proc_decl_in_type.
    def enterProc_decl_in_type(self, ctx:PlSqlParser.Proc_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#proc_decl_in_type.
    def exitProc_decl_in_type(self, ctx:PlSqlParser.Proc_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#func_decl_in_type.
    def enterFunc_decl_in_type(self, ctx:PlSqlParser.Func_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#func_decl_in_type.
    def exitFunc_decl_in_type(self, ctx:PlSqlParser.Func_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:PlSqlParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:PlSqlParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modifier_clause.
    def enterModifier_clause(self, ctx:PlSqlParser.Modifier_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modifier_clause.
    def exitModifier_clause(self, ctx:PlSqlParser.Modifier_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_member_spec.
    def enterObject_member_spec(self, ctx:PlSqlParser.Object_member_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_member_spec.
    def exitObject_member_spec(self, ctx:PlSqlParser.Object_member_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sqlj_object_type_attr.
    def enterSqlj_object_type_attr(self, ctx:PlSqlParser.Sqlj_object_type_attrContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sqlj_object_type_attr.
    def exitSqlj_object_type_attr(self, ctx:PlSqlParser.Sqlj_object_type_attrContext):
        pass


    # Enter a parse tree produced by PlSqlParser#element_spec.
    def enterElement_spec(self, ctx:PlSqlParser.Element_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#element_spec.
    def exitElement_spec(self, ctx:PlSqlParser.Element_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#element_spec_options.
    def enterElement_spec_options(self, ctx:PlSqlParser.Element_spec_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#element_spec_options.
    def exitElement_spec_options(self, ctx:PlSqlParser.Element_spec_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subprogram_spec.
    def enterSubprogram_spec(self, ctx:PlSqlParser.Subprogram_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subprogram_spec.
    def exitSubprogram_spec(self, ctx:PlSqlParser.Subprogram_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_procedure_spec.
    def enterType_procedure_spec(self, ctx:PlSqlParser.Type_procedure_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_procedure_spec.
    def exitType_procedure_spec(self, ctx:PlSqlParser.Type_procedure_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_function_spec.
    def enterType_function_spec(self, ctx:PlSqlParser.Type_function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_function_spec.
    def exitType_function_spec(self, ctx:PlSqlParser.Type_function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constructor_spec.
    def enterConstructor_spec(self, ctx:PlSqlParser.Constructor_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constructor_spec.
    def exitConstructor_spec(self, ctx:PlSqlParser.Constructor_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#map_order_function_spec.
    def enterMap_order_function_spec(self, ctx:PlSqlParser.Map_order_function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#map_order_function_spec.
    def exitMap_order_function_spec(self, ctx:PlSqlParser.Map_order_function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_clause.
    def enterPragma_clause(self, ctx:PlSqlParser.Pragma_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_clause.
    def exitPragma_clause(self, ctx:PlSqlParser.Pragma_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_elements.
    def enterPragma_elements(self, ctx:PlSqlParser.Pragma_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_elements.
    def exitPragma_elements(self, ctx:PlSqlParser.Pragma_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_elements_parameter.
    def enterType_elements_parameter(self, ctx:PlSqlParser.Type_elements_parameterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_elements_parameter.
    def exitType_elements_parameter(self, ctx:PlSqlParser.Type_elements_parameterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_sequence.
    def enterDrop_sequence(self, ctx:PlSqlParser.Drop_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_sequence.
    def exitDrop_sequence(self, ctx:PlSqlParser.Drop_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_sequence.
    def enterAlter_sequence(self, ctx:PlSqlParser.Alter_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_sequence.
    def exitAlter_sequence(self, ctx:PlSqlParser.Alter_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_sequence.
    def enterCreate_sequence(self, ctx:PlSqlParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_sequence.
    def exitCreate_sequence(self, ctx:PlSqlParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_spec.
    def enterSequence_spec(self, ctx:PlSqlParser.Sequence_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_spec.
    def exitSequence_spec(self, ctx:PlSqlParser.Sequence_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_start_clause.
    def enterSequence_start_clause(self, ctx:PlSqlParser.Sequence_start_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_start_clause.
    def exitSequence_start_clause(self, ctx:PlSqlParser.Sequence_start_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#invoker_rights_clause.
    def enterInvoker_rights_clause(self, ctx:PlSqlParser.Invoker_rights_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#invoker_rights_clause.
    def exitInvoker_rights_clause(self, ctx:PlSqlParser.Invoker_rights_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compiler_parameters_clause.
    def enterCompiler_parameters_clause(self, ctx:PlSqlParser.Compiler_parameters_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compiler_parameters_clause.
    def exitCompiler_parameters_clause(self, ctx:PlSqlParser.Compiler_parameters_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#call_spec.
    def enterCall_spec(self, ctx:PlSqlParser.Call_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#call_spec.
    def exitCall_spec(self, ctx:PlSqlParser.Call_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#java_spec.
    def enterJava_spec(self, ctx:PlSqlParser.Java_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#java_spec.
    def exitJava_spec(self, ctx:PlSqlParser.Java_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_spec.
    def enterC_spec(self, ctx:PlSqlParser.C_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_spec.
    def exitC_spec(self, ctx:PlSqlParser.C_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_agent_in_clause.
    def enterC_agent_in_clause(self, ctx:PlSqlParser.C_agent_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_agent_in_clause.
    def exitC_agent_in_clause(self, ctx:PlSqlParser.C_agent_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_parameters_clause.
    def enterC_parameters_clause(self, ctx:PlSqlParser.C_parameters_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_parameters_clause.
    def exitC_parameters_clause(self, ctx:PlSqlParser.C_parameters_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter.
    def enterParameter(self, ctx:PlSqlParser.ParameterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter.
    def exitParameter(self, ctx:PlSqlParser.ParameterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_value_part.
    def enterDefault_value_part(self, ctx:PlSqlParser.Default_value_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_value_part.
    def exitDefault_value_part(self, ctx:PlSqlParser.Default_value_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#declare_spec.
    def enterDeclare_spec(self, ctx:PlSqlParser.Declare_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#declare_spec.
    def exitDeclare_spec(self, ctx:PlSqlParser.Declare_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#variable_declaration.
    def enterVariable_declaration(self, ctx:PlSqlParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#variable_declaration.
    def exitVariable_declaration(self, ctx:PlSqlParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:PlSqlParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:PlSqlParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:PlSqlParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:PlSqlParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter_spec.
    def enterParameter_spec(self, ctx:PlSqlParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter_spec.
    def exitParameter_spec(self, ctx:PlSqlParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_declaration.
    def enterException_declaration(self, ctx:PlSqlParser.Exception_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_declaration.
    def exitException_declaration(self, ctx:PlSqlParser.Exception_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_declaration.
    def enterPragma_declaration(self, ctx:PlSqlParser.Pragma_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_declaration.
    def exitPragma_declaration(self, ctx:PlSqlParser.Pragma_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_declaration.
    def enterRecord_declaration(self, ctx:PlSqlParser.Record_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_declaration.
    def exitRecord_declaration(self, ctx:PlSqlParser.Record_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_type_dec.
    def enterRecord_type_dec(self, ctx:PlSqlParser.Record_type_decContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_type_dec.
    def exitRecord_type_dec(self, ctx:PlSqlParser.Record_type_decContext):
        pass


    # Enter a parse tree produced by PlSqlParser#field_spec.
    def enterField_spec(self, ctx:PlSqlParser.Field_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#field_spec.
    def exitField_spec(self, ctx:PlSqlParser.Field_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_var_dec.
    def enterRecord_var_dec(self, ctx:PlSqlParser.Record_var_decContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_var_dec.
    def exitRecord_var_dec(self, ctx:PlSqlParser.Record_var_decContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_declaration.
    def enterTable_declaration(self, ctx:PlSqlParser.Table_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_declaration.
    def exitTable_declaration(self, ctx:PlSqlParser.Table_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_type_dec.
    def enterTable_type_dec(self, ctx:PlSqlParser.Table_type_decContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_type_dec.
    def exitTable_type_dec(self, ctx:PlSqlParser.Table_type_decContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_indexed_by_part.
    def enterTable_indexed_by_part(self, ctx:PlSqlParser.Table_indexed_by_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_indexed_by_part.
    def exitTable_indexed_by_part(self, ctx:PlSqlParser.Table_indexed_by_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#varray_type_def.
    def enterVarray_type_def(self, ctx:PlSqlParser.Varray_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#varray_type_def.
    def exitVarray_type_def(self, ctx:PlSqlParser.Varray_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_var_dec.
    def enterTable_var_dec(self, ctx:PlSqlParser.Table_var_decContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_var_dec.
    def exitTable_var_dec(self, ctx:PlSqlParser.Table_var_decContext):
        pass


    # Enter a parse tree produced by PlSqlParser#seq_of_statements.
    def enterSeq_of_statements(self, ctx:PlSqlParser.Seq_of_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#seq_of_statements.
    def exitSeq_of_statements(self, ctx:PlSqlParser.Seq_of_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#label_declaration.
    def enterLabel_declaration(self, ctx:PlSqlParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#label_declaration.
    def exitLabel_declaration(self, ctx:PlSqlParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#statement.
    def enterStatement(self, ctx:PlSqlParser.StatementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#statement.
    def exitStatement(self, ctx:PlSqlParser.StatementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#assume_statement.
    def enterAssume_statement(self, ctx:PlSqlParser.Assume_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#assume_statement.
    def exitAssume_statement(self, ctx:PlSqlParser.Assume_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#assert_statement.
    def enterAssert_statement(self, ctx:PlSqlParser.Assert_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#assert_statement.
    def exitAssert_statement(self, ctx:PlSqlParser.Assert_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#assignment_statement.
    def enterAssignment_statement(self, ctx:PlSqlParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#assignment_statement.
    def exitAssignment_statement(self, ctx:PlSqlParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#continue_statement.
    def enterContinue_statement(self, ctx:PlSqlParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#continue_statement.
    def exitContinue_statement(self, ctx:PlSqlParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exit_statement.
    def enterExit_statement(self, ctx:PlSqlParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exit_statement.
    def exitExit_statement(self, ctx:PlSqlParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#goto_statement.
    def enterGoto_statement(self, ctx:PlSqlParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#goto_statement.
    def exitGoto_statement(self, ctx:PlSqlParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#if_statement.
    def enterIf_statement(self, ctx:PlSqlParser.If_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#if_statement.
    def exitIf_statement(self, ctx:PlSqlParser.If_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#elsif_part.
    def enterElsif_part(self, ctx:PlSqlParser.Elsif_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#elsif_part.
    def exitElsif_part(self, ctx:PlSqlParser.Elsif_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#else_part.
    def enterElse_part(self, ctx:PlSqlParser.Else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#else_part.
    def exitElse_part(self, ctx:PlSqlParser.Else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#loop_statement.
    def enterLoop_statement(self, ctx:PlSqlParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#loop_statement.
    def exitLoop_statement(self, ctx:PlSqlParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_loop_param.
    def enterCursor_loop_param(self, ctx:PlSqlParser.Cursor_loop_paramContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_loop_param.
    def exitCursor_loop_param(self, ctx:PlSqlParser.Cursor_loop_paramContext):
        pass


    # Enter a parse tree produced by PlSqlParser#forall_statement.
    def enterForall_statement(self, ctx:PlSqlParser.Forall_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#forall_statement.
    def exitForall_statement(self, ctx:PlSqlParser.Forall_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#bounds_clause.
    def enterBounds_clause(self, ctx:PlSqlParser.Bounds_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#bounds_clause.
    def exitBounds_clause(self, ctx:PlSqlParser.Bounds_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#between_bound.
    def enterBetween_bound(self, ctx:PlSqlParser.Between_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#between_bound.
    def exitBetween_bound(self, ctx:PlSqlParser.Between_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lower_bound.
    def enterLower_bound(self, ctx:PlSqlParser.Lower_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lower_bound.
    def exitLower_bound(self, ctx:PlSqlParser.Lower_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#upper_bound.
    def enterUpper_bound(self, ctx:PlSqlParser.Upper_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#upper_bound.
    def exitUpper_bound(self, ctx:PlSqlParser.Upper_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#null_statement.
    def enterNull_statement(self, ctx:PlSqlParser.Null_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#null_statement.
    def exitNull_statement(self, ctx:PlSqlParser.Null_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#raise_statement.
    def enterRaise_statement(self, ctx:PlSqlParser.Raise_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#raise_statement.
    def exitRaise_statement(self, ctx:PlSqlParser.Raise_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#return_statement.
    def enterReturn_statement(self, ctx:PlSqlParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#return_statement.
    def exitReturn_statement(self, ctx:PlSqlParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_call.
    def enterFunction_call(self, ctx:PlSqlParser.Function_callContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_call.
    def exitFunction_call(self, ctx:PlSqlParser.Function_callContext):
        pass


    # Enter a parse tree produced by PlSqlParser#body.
    def enterBody(self, ctx:PlSqlParser.BodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#body.
    def exitBody(self, ctx:PlSqlParser.BodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_handler.
    def enterException_handler(self, ctx:PlSqlParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_handler.
    def exitException_handler(self, ctx:PlSqlParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_block.
    def enterTrigger_block(self, ctx:PlSqlParser.Trigger_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_block.
    def exitTrigger_block(self, ctx:PlSqlParser.Trigger_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#block.
    def enterBlock(self, ctx:PlSqlParser.BlockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#block.
    def exitBlock(self, ctx:PlSqlParser.BlockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_statement.
    def enterSql_statement(self, ctx:PlSqlParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_statement.
    def exitSql_statement(self, ctx:PlSqlParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#execute_immediate.
    def enterExecute_immediate(self, ctx:PlSqlParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by PlSqlParser#execute_immediate.
    def exitExecute_immediate(self, ctx:PlSqlParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dynamic_returning_clause.
    def enterDynamic_returning_clause(self, ctx:PlSqlParser.Dynamic_returning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dynamic_returning_clause.
    def exitDynamic_returning_clause(self, ctx:PlSqlParser.Dynamic_returning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#data_manipulation_language_statements.
    def enterData_manipulation_language_statements(self, ctx:PlSqlParser.Data_manipulation_language_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#data_manipulation_language_statements.
    def exitData_manipulation_language_statements(self, ctx:PlSqlParser.Data_manipulation_language_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_manipulation_statements.
    def enterCursor_manipulation_statements(self, ctx:PlSqlParser.Cursor_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_manipulation_statements.
    def exitCursor_manipulation_statements(self, ctx:PlSqlParser.Cursor_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#close_statement.
    def enterClose_statement(self, ctx:PlSqlParser.Close_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#close_statement.
    def exitClose_statement(self, ctx:PlSqlParser.Close_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#open_statement.
    def enterOpen_statement(self, ctx:PlSqlParser.Open_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#open_statement.
    def exitOpen_statement(self, ctx:PlSqlParser.Open_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#fetch_statement.
    def enterFetch_statement(self, ctx:PlSqlParser.Fetch_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#fetch_statement.
    def exitFetch_statement(self, ctx:PlSqlParser.Fetch_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#open_for_statement.
    def enterOpen_for_statement(self, ctx:PlSqlParser.Open_for_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#open_for_statement.
    def exitOpen_for_statement(self, ctx:PlSqlParser.Open_for_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#transaction_control_statements.
    def enterTransaction_control_statements(self, ctx:PlSqlParser.Transaction_control_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#transaction_control_statements.
    def exitTransaction_control_statements(self, ctx:PlSqlParser.Transaction_control_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_transaction_command.
    def enterSet_transaction_command(self, ctx:PlSqlParser.Set_transaction_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_transaction_command.
    def exitSet_transaction_command(self, ctx:PlSqlParser.Set_transaction_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_constraint_command.
    def enterSet_constraint_command(self, ctx:PlSqlParser.Set_constraint_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_constraint_command.
    def exitSet_constraint_command(self, ctx:PlSqlParser.Set_constraint_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#commit_statement.
    def enterCommit_statement(self, ctx:PlSqlParser.Commit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#commit_statement.
    def exitCommit_statement(self, ctx:PlSqlParser.Commit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#write_clause.
    def enterWrite_clause(self, ctx:PlSqlParser.Write_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#write_clause.
    def exitWrite_clause(self, ctx:PlSqlParser.Write_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollback_statement.
    def enterRollback_statement(self, ctx:PlSqlParser.Rollback_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollback_statement.
    def exitRollback_statement(self, ctx:PlSqlParser.Rollback_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#savepoint_statement.
    def enterSavepoint_statement(self, ctx:PlSqlParser.Savepoint_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#savepoint_statement.
    def exitSavepoint_statement(self, ctx:PlSqlParser.Savepoint_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#explain_statement.
    def enterExplain_statement(self, ctx:PlSqlParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#explain_statement.
    def exitExplain_statement(self, ctx:PlSqlParser.Explain_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#select_statement.
    def enterSelect_statement(self, ctx:PlSqlParser.Select_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#select_statement.
    def exitSelect_statement(self, ctx:PlSqlParser.Select_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_factoring_clause.
    def enterSubquery_factoring_clause(self, ctx:PlSqlParser.Subquery_factoring_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_factoring_clause.
    def exitSubquery_factoring_clause(self, ctx:PlSqlParser.Subquery_factoring_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#factoring_element.
    def enterFactoring_element(self, ctx:PlSqlParser.Factoring_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#factoring_element.
    def exitFactoring_element(self, ctx:PlSqlParser.Factoring_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#search_clause.
    def enterSearch_clause(self, ctx:PlSqlParser.Search_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#search_clause.
    def exitSearch_clause(self, ctx:PlSqlParser.Search_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cycle_clause.
    def enterCycle_clause(self, ctx:PlSqlParser.Cycle_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cycle_clause.
    def exitCycle_clause(self, ctx:PlSqlParser.Cycle_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#SubqueryParen.
    def enterSubqueryParen(self, ctx:PlSqlParser.SubqueryParenContext):
        pass

    # Exit a parse tree produced by PlSqlParser#SubqueryParen.
    def exitSubqueryParen(self, ctx:PlSqlParser.SubqueryParenContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IgnoreSubquery.
    def enterIgnoreSubquery(self, ctx:PlSqlParser.IgnoreSubqueryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IgnoreSubquery.
    def exitIgnoreSubquery(self, ctx:PlSqlParser.IgnoreSubqueryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#SubqueryCompound.
    def enterSubqueryCompound(self, ctx:PlSqlParser.SubqueryCompoundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#SubqueryCompound.
    def exitSubqueryCompound(self, ctx:PlSqlParser.SubqueryCompoundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_operation_part.
    def enterSubquery_operation_part(self, ctx:PlSqlParser.Subquery_operation_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_operation_part.
    def exitSubquery_operation_part(self, ctx:PlSqlParser.Subquery_operation_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_block.
    def enterQuery_block(self, ctx:PlSqlParser.Query_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_block.
    def exitQuery_block(self, ctx:PlSqlParser.Query_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#Star1.
    def enterStar1(self, ctx:PlSqlParser.Star1Context):
        pass

    # Exit a parse tree produced by PlSqlParser#Star1.
    def exitStar1(self, ctx:PlSqlParser.Star1Context):
        pass


    # Enter a parse tree produced by PlSqlParser#StarTable.
    def enterStarTable(self, ctx:PlSqlParser.StarTableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#StarTable.
    def exitStarTable(self, ctx:PlSqlParser.StarTableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IgnoreTableview_name.
    def enterIgnoreTableview_name(self, ctx:PlSqlParser.IgnoreTableview_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IgnoreTableview_name.
    def exitIgnoreTableview_name(self, ctx:PlSqlParser.IgnoreTableview_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#Alias_expr.
    def enterAlias_expr(self, ctx:PlSqlParser.Alias_exprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#Alias_expr.
    def exitAlias_expr(self, ctx:PlSqlParser.Alias_exprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#from_clause.
    def enterFrom_clause(self, ctx:PlSqlParser.From_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#from_clause.
    def exitFrom_clause(self, ctx:PlSqlParser.From_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_pivot.
    def enterTable_ref_pivot(self, ctx:PlSqlParser.Table_ref_pivotContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_pivot.
    def exitTable_ref_pivot(self, ctx:PlSqlParser.Table_ref_pivotContext):
        pass


    # Enter a parse tree produced by PlSqlParser#JoinExpr.
    def enterJoinExpr(self, ctx:PlSqlParser.JoinExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#JoinExpr.
    def exitJoinExpr(self, ctx:PlSqlParser.JoinExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#TableRefSimple.
    def enterTableRefSimple(self, ctx:PlSqlParser.TableRefSimpleContext):
        pass

    # Exit a parse tree produced by PlSqlParser#TableRefSimple.
    def exitTableRefSimple(self, ctx:PlSqlParser.TableRefSimpleContext):
        pass


    # Enter a parse tree produced by PlSqlParser#TableRefAux.
    def enterTableRefAux(self, ctx:PlSqlParser.TableRefAuxContext):
        pass

    # Exit a parse tree produced by PlSqlParser#TableRefAux.
    def exitTableRefAux(self, ctx:PlSqlParser.TableRefAuxContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_aux.
    def enterTable_ref_aux(self, ctx:PlSqlParser.Table_ref_auxContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_aux.
    def exitTable_ref_aux(self, ctx:PlSqlParser.Table_ref_auxContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_clause.
    def enterJoin_clause(self, ctx:PlSqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_clause.
    def exitJoin_clause(self, ctx:PlSqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_on_part.
    def enterJoin_on_part(self, ctx:PlSqlParser.Join_on_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_on_part.
    def exitJoin_on_part(self, ctx:PlSqlParser.Join_on_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_using_part.
    def enterJoin_using_part(self, ctx:PlSqlParser.Join_using_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_using_part.
    def exitJoin_using_part(self, ctx:PlSqlParser.Join_using_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_type.
    def enterJoin_type(self, ctx:PlSqlParser.Join_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_type.
    def exitJoin_type(self, ctx:PlSqlParser.Join_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_partition_clause.
    def enterQuery_partition_clause(self, ctx:PlSqlParser.Query_partition_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_partition_clause.
    def exitQuery_partition_clause(self, ctx:PlSqlParser.Query_partition_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_query_clause.
    def enterFlashback_query_clause(self, ctx:PlSqlParser.Flashback_query_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_query_clause.
    def exitFlashback_query_clause(self, ctx:PlSqlParser.Flashback_query_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_clause.
    def enterPivot_clause(self, ctx:PlSqlParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_clause.
    def exitPivot_clause(self, ctx:PlSqlParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_element.
    def enterPivot_element(self, ctx:PlSqlParser.Pivot_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_element.
    def exitPivot_element(self, ctx:PlSqlParser.Pivot_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_for_clause.
    def enterPivot_for_clause(self, ctx:PlSqlParser.Pivot_for_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_for_clause.
    def exitPivot_for_clause(self, ctx:PlSqlParser.Pivot_for_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause.
    def enterPivot_in_clause(self, ctx:PlSqlParser.Pivot_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause.
    def exitPivot_in_clause(self, ctx:PlSqlParser.Pivot_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause_element.
    def enterPivot_in_clause_element(self, ctx:PlSqlParser.Pivot_in_clause_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause_element.
    def exitPivot_in_clause_element(self, ctx:PlSqlParser.Pivot_in_clause_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause_elements.
    def enterPivot_in_clause_elements(self, ctx:PlSqlParser.Pivot_in_clause_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause_elements.
    def exitPivot_in_clause_elements(self, ctx:PlSqlParser.Pivot_in_clause_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:PlSqlParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:PlSqlParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_in_clause.
    def enterUnpivot_in_clause(self, ctx:PlSqlParser.Unpivot_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_in_clause.
    def exitUnpivot_in_clause(self, ctx:PlSqlParser.Unpivot_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_in_elements.
    def enterUnpivot_in_elements(self, ctx:PlSqlParser.Unpivot_in_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_in_elements.
    def exitUnpivot_in_elements(self, ctx:PlSqlParser.Unpivot_in_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hierarchical_query_clause.
    def enterHierarchical_query_clause(self, ctx:PlSqlParser.Hierarchical_query_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hierarchical_query_clause.
    def exitHierarchical_query_clause(self, ctx:PlSqlParser.Hierarchical_query_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#start_part.
    def enterStart_part(self, ctx:PlSqlParser.Start_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#start_part.
    def exitStart_part(self, ctx:PlSqlParser.Start_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:PlSqlParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:PlSqlParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#group_by_elements.
    def enterGroup_by_elements(self, ctx:PlSqlParser.Group_by_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#group_by_elements.
    def exitGroup_by_elements(self, ctx:PlSqlParser.Group_by_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollup_cube_clause.
    def enterRollup_cube_clause(self, ctx:PlSqlParser.Rollup_cube_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollup_cube_clause.
    def exitRollup_cube_clause(self, ctx:PlSqlParser.Rollup_cube_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:PlSqlParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:PlSqlParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grouping_sets_elements.
    def enterGrouping_sets_elements(self, ctx:PlSqlParser.Grouping_sets_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grouping_sets_elements.
    def exitGrouping_sets_elements(self, ctx:PlSqlParser.Grouping_sets_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#having_clause.
    def enterHaving_clause(self, ctx:PlSqlParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#having_clause.
    def exitHaving_clause(self, ctx:PlSqlParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_clause.
    def enterModel_clause(self, ctx:PlSqlParser.Model_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_clause.
    def exitModel_clause(self, ctx:PlSqlParser.Model_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cell_reference_options.
    def enterCell_reference_options(self, ctx:PlSqlParser.Cell_reference_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cell_reference_options.
    def exitCell_reference_options(self, ctx:PlSqlParser.Cell_reference_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#return_rows_clause.
    def enterReturn_rows_clause(self, ctx:PlSqlParser.Return_rows_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#return_rows_clause.
    def exitReturn_rows_clause(self, ctx:PlSqlParser.Return_rows_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_model.
    def enterReference_model(self, ctx:PlSqlParser.Reference_modelContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_model.
    def exitReference_model(self, ctx:PlSqlParser.Reference_modelContext):
        pass


    # Enter a parse tree produced by PlSqlParser#main_model.
    def enterMain_model(self, ctx:PlSqlParser.Main_modelContext):
        pass

    # Exit a parse tree produced by PlSqlParser#main_model.
    def exitMain_model(self, ctx:PlSqlParser.Main_modelContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_clauses.
    def enterModel_column_clauses(self, ctx:PlSqlParser.Model_column_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_clauses.
    def exitModel_column_clauses(self, ctx:PlSqlParser.Model_column_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_partition_part.
    def enterModel_column_partition_part(self, ctx:PlSqlParser.Model_column_partition_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_partition_part.
    def exitModel_column_partition_part(self, ctx:PlSqlParser.Model_column_partition_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_list.
    def enterModel_column_list(self, ctx:PlSqlParser.Model_column_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_list.
    def exitModel_column_list(self, ctx:PlSqlParser.Model_column_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column.
    def enterModel_column(self, ctx:PlSqlParser.Model_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column.
    def exitModel_column(self, ctx:PlSqlParser.Model_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_clause.
    def enterModel_rules_clause(self, ctx:PlSqlParser.Model_rules_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_clause.
    def exitModel_rules_clause(self, ctx:PlSqlParser.Model_rules_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_part.
    def enterModel_rules_part(self, ctx:PlSqlParser.Model_rules_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_part.
    def exitModel_rules_part(self, ctx:PlSqlParser.Model_rules_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_element.
    def enterModel_rules_element(self, ctx:PlSqlParser.Model_rules_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_element.
    def exitModel_rules_element(self, ctx:PlSqlParser.Model_rules_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cell_assignment.
    def enterCell_assignment(self, ctx:PlSqlParser.Cell_assignmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cell_assignment.
    def exitCell_assignment(self, ctx:PlSqlParser.Cell_assignmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_iterate_clause.
    def enterModel_iterate_clause(self, ctx:PlSqlParser.Model_iterate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_iterate_clause.
    def exitModel_iterate_clause(self, ctx:PlSqlParser.Model_iterate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#until_part.
    def enterUntil_part(self, ctx:PlSqlParser.Until_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#until_part.
    def exitUntil_part(self, ctx:PlSqlParser.Until_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:PlSqlParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:PlSqlParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#order_by_elements.
    def enterOrder_by_elements(self, ctx:PlSqlParser.Order_by_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#order_by_elements.
    def exitOrder_by_elements(self, ctx:PlSqlParser.Order_by_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_clause.
    def enterFor_update_clause(self, ctx:PlSqlParser.For_update_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_clause.
    def exitFor_update_clause(self, ctx:PlSqlParser.For_update_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_of_part.
    def enterFor_update_of_part(self, ctx:PlSqlParser.For_update_of_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_of_part.
    def exitFor_update_of_part(self, ctx:PlSqlParser.For_update_of_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_options.
    def enterFor_update_options(self, ctx:PlSqlParser.For_update_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_options.
    def exitFor_update_options(self, ctx:PlSqlParser.For_update_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#limit_clause.
    def enterLimit_clause(self, ctx:PlSqlParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#limit_clause.
    def exitLimit_clause(self, ctx:PlSqlParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_statement.
    def enterUpdate_statement(self, ctx:PlSqlParser.Update_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_statement.
    def exitUpdate_statement(self, ctx:PlSqlParser.Update_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_set_clause.
    def enterUpdate_set_clause(self, ctx:PlSqlParser.Update_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_set_clause.
    def exitUpdate_set_clause(self, ctx:PlSqlParser.Update_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_based_update_set_clause.
    def enterColumn_based_update_set_clause(self, ctx:PlSqlParser.Column_based_update_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_based_update_set_clause.
    def exitColumn_based_update_set_clause(self, ctx:PlSqlParser.Column_based_update_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#delete_statement.
    def enterDelete_statement(self, ctx:PlSqlParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#delete_statement.
    def exitDelete_statement(self, ctx:PlSqlParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#insert_statement.
    def enterInsert_statement(self, ctx:PlSqlParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#insert_statement.
    def exitInsert_statement(self, ctx:PlSqlParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#single_table_insert.
    def enterSingle_table_insert(self, ctx:PlSqlParser.Single_table_insertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#single_table_insert.
    def exitSingle_table_insert(self, ctx:PlSqlParser.Single_table_insertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_table_insert.
    def enterMulti_table_insert(self, ctx:PlSqlParser.Multi_table_insertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_table_insert.
    def exitMulti_table_insert(self, ctx:PlSqlParser.Multi_table_insertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_table_element.
    def enterMulti_table_element(self, ctx:PlSqlParser.Multi_table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_table_element.
    def exitMulti_table_element(self, ctx:PlSqlParser.Multi_table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_clause.
    def enterConditional_insert_clause(self, ctx:PlSqlParser.Conditional_insert_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_clause.
    def exitConditional_insert_clause(self, ctx:PlSqlParser.Conditional_insert_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_when_part.
    def enterConditional_insert_when_part(self, ctx:PlSqlParser.Conditional_insert_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_when_part.
    def exitConditional_insert_when_part(self, ctx:PlSqlParser.Conditional_insert_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_else_part.
    def enterConditional_insert_else_part(self, ctx:PlSqlParser.Conditional_insert_else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_else_part.
    def exitConditional_insert_else_part(self, ctx:PlSqlParser.Conditional_insert_else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#insert_into_clause.
    def enterInsert_into_clause(self, ctx:PlSqlParser.Insert_into_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#insert_into_clause.
    def exitInsert_into_clause(self, ctx:PlSqlParser.Insert_into_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#values_clause.
    def enterValues_clause(self, ctx:PlSqlParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#values_clause.
    def exitValues_clause(self, ctx:PlSqlParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_statement.
    def enterMerge_statement(self, ctx:PlSqlParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_statement.
    def exitMerge_statement(self, ctx:PlSqlParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:PlSqlParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:PlSqlParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_element.
    def enterMerge_element(self, ctx:PlSqlParser.Merge_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_element.
    def exitMerge_element(self, ctx:PlSqlParser.Merge_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_update_delete_part.
    def enterMerge_update_delete_part(self, ctx:PlSqlParser.Merge_update_delete_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_update_delete_part.
    def exitMerge_update_delete_part(self, ctx:PlSqlParser.Merge_update_delete_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:PlSqlParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:PlSqlParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#selected_tableview.
    def enterSelected_tableview(self, ctx:PlSqlParser.Selected_tableviewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#selected_tableview.
    def exitSelected_tableview(self, ctx:PlSqlParser.Selected_tableviewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_table_statement.
    def enterLock_table_statement(self, ctx:PlSqlParser.Lock_table_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_table_statement.
    def exitLock_table_statement(self, ctx:PlSqlParser.Lock_table_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#wait_nowait_part.
    def enterWait_nowait_part(self, ctx:PlSqlParser.Wait_nowait_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#wait_nowait_part.
    def exitWait_nowait_part(self, ctx:PlSqlParser.Wait_nowait_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_table_element.
    def enterLock_table_element(self, ctx:PlSqlParser.Lock_table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_table_element.
    def exitLock_table_element(self, ctx:PlSqlParser.Lock_table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_mode.
    def enterLock_mode(self, ctx:PlSqlParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_mode.
    def exitLock_mode(self, ctx:PlSqlParser.Lock_modeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#general_table_ref.
    def enterGeneral_table_ref(self, ctx:PlSqlParser.General_table_refContext):
        pass

    # Exit a parse tree produced by PlSqlParser#general_table_ref.
    def exitGeneral_table_ref(self, ctx:PlSqlParser.General_table_refContext):
        pass


    # Enter a parse tree produced by PlSqlParser#static_returning_clause.
    def enterStatic_returning_clause(self, ctx:PlSqlParser.Static_returning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#static_returning_clause.
    def exitStatic_returning_clause(self, ctx:PlSqlParser.Static_returning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_clause.
    def enterError_logging_clause(self, ctx:PlSqlParser.Error_logging_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_clause.
    def exitError_logging_clause(self, ctx:PlSqlParser.Error_logging_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_into_part.
    def enterError_logging_into_part(self, ctx:PlSqlParser.Error_logging_into_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_into_part.
    def exitError_logging_into_part(self, ctx:PlSqlParser.Error_logging_into_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_reject_part.
    def enterError_logging_reject_part(self, ctx:PlSqlParser.Error_logging_reject_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_reject_part.
    def exitError_logging_reject_part(self, ctx:PlSqlParser.Error_logging_reject_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_table_expression_clause.
    def enterDml_table_expression_clause(self, ctx:PlSqlParser.Dml_table_expression_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_table_expression_clause.
    def exitDml_table_expression_clause(self, ctx:PlSqlParser.Dml_table_expression_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_collection_expression.
    def enterTable_collection_expression(self, ctx:PlSqlParser.Table_collection_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_collection_expression.
    def exitTable_collection_expression(self, ctx:PlSqlParser.Table_collection_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_restriction_clause.
    def enterSubquery_restriction_clause(self, ctx:PlSqlParser.Subquery_restriction_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_restriction_clause.
    def exitSubquery_restriction_clause(self, ctx:PlSqlParser.Subquery_restriction_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sample_clause.
    def enterSample_clause(self, ctx:PlSqlParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sample_clause.
    def exitSample_clause(self, ctx:PlSqlParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#seed_part.
    def enterSeed_part(self, ctx:PlSqlParser.Seed_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#seed_part.
    def exitSeed_part(self, ctx:PlSqlParser.Seed_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_expression.
    def enterCursor_expression(self, ctx:PlSqlParser.Cursor_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_expression.
    def exitCursor_expression(self, ctx:PlSqlParser.Cursor_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#expression_list.
    def enterExpression_list(self, ctx:PlSqlParser.Expression_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#expression_list.
    def exitExpression_list(self, ctx:PlSqlParser.Expression_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#condition.
    def enterCondition(self, ctx:PlSqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#condition.
    def exitCondition(self, ctx:PlSqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IgnoreExpr.
    def enterIgnoreExpr(self, ctx:PlSqlParser.IgnoreExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IgnoreExpr.
    def exitIgnoreExpr(self, ctx:PlSqlParser.IgnoreExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#AndExpr.
    def enterAndExpr(self, ctx:PlSqlParser.AndExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#AndExpr.
    def exitAndExpr(self, ctx:PlSqlParser.AndExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#LikeExpr.
    def enterLikeExpr(self, ctx:PlSqlParser.LikeExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#LikeExpr.
    def exitLikeExpr(self, ctx:PlSqlParser.LikeExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#RelExpr.
    def enterRelExpr(self, ctx:PlSqlParser.RelExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#RelExpr.
    def exitRelExpr(self, ctx:PlSqlParser.RelExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#MemberExpr.
    def enterMemberExpr(self, ctx:PlSqlParser.MemberExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#MemberExpr.
    def exitMemberExpr(self, ctx:PlSqlParser.MemberExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#BetweenExpr.
    def enterBetweenExpr(self, ctx:PlSqlParser.BetweenExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#BetweenExpr.
    def exitBetweenExpr(self, ctx:PlSqlParser.BetweenExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#CursorExpr.
    def enterCursorExpr(self, ctx:PlSqlParser.CursorExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#CursorExpr.
    def exitCursorExpr(self, ctx:PlSqlParser.CursorExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IsExpr.
    def enterIsExpr(self, ctx:PlSqlParser.IsExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IsExpr.
    def exitIsExpr(self, ctx:PlSqlParser.IsExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#NotExpr.
    def enterNotExpr(self, ctx:PlSqlParser.NotExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#NotExpr.
    def exitNotExpr(self, ctx:PlSqlParser.NotExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#InExpr.
    def enterInExpr(self, ctx:PlSqlParser.InExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#InExpr.
    def exitInExpr(self, ctx:PlSqlParser.InExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ParenExpr.
    def enterParenExpr(self, ctx:PlSqlParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ParenExpr.
    def exitParenExpr(self, ctx:PlSqlParser.ParenExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#OrExpr.
    def enterOrExpr(self, ctx:PlSqlParser.OrExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#OrExpr.
    def exitOrExpr(self, ctx:PlSqlParser.OrExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#is_part.
    def enterIs_part(self, ctx:PlSqlParser.Is_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#is_part.
    def exitIs_part(self, ctx:PlSqlParser.Is_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_part.
    def enterCursor_part(self, ctx:PlSqlParser.Cursor_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_part.
    def exitCursor_part(self, ctx:PlSqlParser.Cursor_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multiset_type.
    def enterMultiset_type(self, ctx:PlSqlParser.Multiset_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multiset_type.
    def exitMultiset_type(self, ctx:PlSqlParser.Multiset_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relational_operator.
    def enterRelational_operator(self, ctx:PlSqlParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relational_operator.
    def exitRelational_operator(self, ctx:PlSqlParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#like_type.
    def enterLike_type(self, ctx:PlSqlParser.Like_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#like_type.
    def exitLike_type(self, ctx:PlSqlParser.Like_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#like_escape_part.
    def enterLike_escape_part(self, ctx:PlSqlParser.Like_escape_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#like_escape_part.
    def exitLike_escape_part(self, ctx:PlSqlParser.Like_escape_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#between_elements.
    def enterBetween_elements(self, ctx:PlSqlParser.Between_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#between_elements.
    def exitBetween_elements(self, ctx:PlSqlParser.Between_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#concatenation.
    def enterConcatenation(self, ctx:PlSqlParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#concatenation.
    def exitConcatenation(self, ctx:PlSqlParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#BinaryExpr.
    def enterBinaryExpr(self, ctx:PlSqlParser.BinaryExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#BinaryExpr.
    def exitBinaryExpr(self, ctx:PlSqlParser.BinaryExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IgnoreBinaryExpr.
    def enterIgnoreBinaryExpr(self, ctx:PlSqlParser.IgnoreBinaryExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IgnoreBinaryExpr.
    def exitIgnoreBinaryExpr(self, ctx:PlSqlParser.IgnoreBinaryExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ParenBinaryExpr.
    def enterParenBinaryExpr(self, ctx:PlSqlParser.ParenBinaryExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ParenBinaryExpr.
    def exitParenBinaryExpr(self, ctx:PlSqlParser.ParenBinaryExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#interval_expression.
    def enterInterval_expression(self, ctx:PlSqlParser.Interval_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#interval_expression.
    def exitInterval_expression(self, ctx:PlSqlParser.Interval_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_expression.
    def enterModel_expression(self, ctx:PlSqlParser.Model_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_expression.
    def exitModel_expression(self, ctx:PlSqlParser.Model_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_expression_element.
    def enterModel_expression_element(self, ctx:PlSqlParser.Model_expression_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_expression_element.
    def exitModel_expression_element(self, ctx:PlSqlParser.Model_expression_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#single_column_for_loop.
    def enterSingle_column_for_loop(self, ctx:PlSqlParser.Single_column_for_loopContext):
        pass

    # Exit a parse tree produced by PlSqlParser#single_column_for_loop.
    def exitSingle_column_for_loop(self, ctx:PlSqlParser.Single_column_for_loopContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_like_part.
    def enterFor_like_part(self, ctx:PlSqlParser.For_like_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_like_part.
    def exitFor_like_part(self, ctx:PlSqlParser.For_like_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_increment_decrement_type.
    def enterFor_increment_decrement_type(self, ctx:PlSqlParser.For_increment_decrement_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_increment_decrement_type.
    def exitFor_increment_decrement_type(self, ctx:PlSqlParser.For_increment_decrement_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_column_for_loop.
    def enterMulti_column_for_loop(self, ctx:PlSqlParser.Multi_column_for_loopContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_column_for_loop.
    def exitMulti_column_for_loop(self, ctx:PlSqlParser.Multi_column_for_loopContext):
        pass


    # Enter a parse tree produced by PlSqlParser#IgnoreUnaryExpr.
    def enterIgnoreUnaryExpr(self, ctx:PlSqlParser.IgnoreUnaryExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#IgnoreUnaryExpr.
    def exitIgnoreUnaryExpr(self, ctx:PlSqlParser.IgnoreUnaryExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#UnaryExpr.
    def enterUnaryExpr(self, ctx:PlSqlParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#UnaryExpr.
    def exitUnaryExpr(self, ctx:PlSqlParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#case_statement.
    def enterCase_statement(self, ctx:PlSqlParser.Case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#case_statement.
    def exitCase_statement(self, ctx:PlSqlParser.Case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_case_statement.
    def enterSimple_case_statement(self, ctx:PlSqlParser.Simple_case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_case_statement.
    def exitSimple_case_statement(self, ctx:PlSqlParser.Simple_case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_case_when_part.
    def enterSimple_case_when_part(self, ctx:PlSqlParser.Simple_case_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_case_when_part.
    def exitSimple_case_when_part(self, ctx:PlSqlParser.Simple_case_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#searched_case_statement.
    def enterSearched_case_statement(self, ctx:PlSqlParser.Searched_case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#searched_case_statement.
    def exitSearched_case_statement(self, ctx:PlSqlParser.Searched_case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#searched_case_when_part.
    def enterSearched_case_when_part(self, ctx:PlSqlParser.Searched_case_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#searched_case_when_part.
    def exitSearched_case_when_part(self, ctx:PlSqlParser.Searched_case_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#case_else_part.
    def enterCase_else_part(self, ctx:PlSqlParser.Case_else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#case_else_part.
    def exitCase_else_part(self, ctx:PlSqlParser.Case_else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#atom.
    def enterAtom(self, ctx:PlSqlParser.AtomContext):
        pass

    # Exit a parse tree produced by PlSqlParser#atom.
    def exitAtom(self, ctx:PlSqlParser.AtomContext):
        pass


    # Enter a parse tree produced by PlSqlParser#expression_or_vector.
    def enterExpression_or_vector(self, ctx:PlSqlParser.Expression_or_vectorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#expression_or_vector.
    def exitExpression_or_vector(self, ctx:PlSqlParser.Expression_or_vectorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#vector_expr.
    def enterVector_expr(self, ctx:PlSqlParser.Vector_exprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#vector_expr.
    def exitVector_expr(self, ctx:PlSqlParser.Vector_exprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quantified_expression.
    def enterQuantified_expression(self, ctx:PlSqlParser.Quantified_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quantified_expression.
    def exitQuantified_expression(self, ctx:PlSqlParser.Quantified_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#AggregateCall.
    def enterAggregateCall(self, ctx:PlSqlParser.AggregateCallContext):
        pass

    # Exit a parse tree produced by PlSqlParser#AggregateCall.
    def exitAggregateCall(self, ctx:PlSqlParser.AggregateCallContext):
        pass


    # Enter a parse tree produced by PlSqlParser#TodoCall.
    def enterTodoCall(self, ctx:PlSqlParser.TodoCallContext):
        pass

    # Exit a parse tree produced by PlSqlParser#TodoCall.
    def exitTodoCall(self, ctx:PlSqlParser.TodoCallContext):
        pass


    # Enter a parse tree produced by PlSqlParser#XmlCall.
    def enterXmlCall(self, ctx:PlSqlParser.XmlCallContext):
        pass

    # Exit a parse tree produced by PlSqlParser#XmlCall.
    def exitXmlCall(self, ctx:PlSqlParser.XmlCallContext):
        pass


    # Enter a parse tree produced by PlSqlParser#aggregate_windowed_function.
    def enterAggregate_windowed_function(self, ctx:PlSqlParser.Aggregate_windowed_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#aggregate_windowed_function.
    def exitAggregate_windowed_function(self, ctx:PlSqlParser.Aggregate_windowed_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#over_clause_keyword.
    def enterOver_clause_keyword(self, ctx:PlSqlParser.Over_clause_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#over_clause_keyword.
    def exitOver_clause_keyword(self, ctx:PlSqlParser.Over_clause_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#within_or_over_clause_keyword.
    def enterWithin_or_over_clause_keyword(self, ctx:PlSqlParser.Within_or_over_clause_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#within_or_over_clause_keyword.
    def exitWithin_or_over_clause_keyword(self, ctx:PlSqlParser.Within_or_over_clause_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#standard_prediction_function_keyword.
    def enterStandard_prediction_function_keyword(self, ctx:PlSqlParser.Standard_prediction_function_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#standard_prediction_function_keyword.
    def exitStandard_prediction_function_keyword(self, ctx:PlSqlParser.Standard_prediction_function_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#over_clause.
    def enterOver_clause(self, ctx:PlSqlParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#over_clause.
    def exitOver_clause(self, ctx:PlSqlParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_clause.
    def enterWindowing_clause(self, ctx:PlSqlParser.Windowing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_clause.
    def exitWindowing_clause(self, ctx:PlSqlParser.Windowing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_type.
    def enterWindowing_type(self, ctx:PlSqlParser.Windowing_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_type.
    def exitWindowing_type(self, ctx:PlSqlParser.Windowing_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_elements.
    def enterWindowing_elements(self, ctx:PlSqlParser.Windowing_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_elements.
    def exitWindowing_elements(self, ctx:PlSqlParser.Windowing_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_clause.
    def enterUsing_clause(self, ctx:PlSqlParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_clause.
    def exitUsing_clause(self, ctx:PlSqlParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_element.
    def enterUsing_element(self, ctx:PlSqlParser.Using_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_element.
    def exitUsing_element(self, ctx:PlSqlParser.Using_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collect_order_by_part.
    def enterCollect_order_by_part(self, ctx:PlSqlParser.Collect_order_by_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collect_order_by_part.
    def exitCollect_order_by_part(self, ctx:PlSqlParser.Collect_order_by_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#within_or_over_part.
    def enterWithin_or_over_part(self, ctx:PlSqlParser.Within_or_over_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#within_or_over_part.
    def exitWithin_or_over_part(self, ctx:PlSqlParser.Within_or_over_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cost_matrix_clause.
    def enterCost_matrix_clause(self, ctx:PlSqlParser.Cost_matrix_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cost_matrix_clause.
    def exitCost_matrix_clause(self, ctx:PlSqlParser.Cost_matrix_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_passing_clause.
    def enterXml_passing_clause(self, ctx:PlSqlParser.Xml_passing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_passing_clause.
    def exitXml_passing_clause(self, ctx:PlSqlParser.Xml_passing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_attributes_clause.
    def enterXml_attributes_clause(self, ctx:PlSqlParser.Xml_attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_attributes_clause.
    def exitXml_attributes_clause(self, ctx:PlSqlParser.Xml_attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_namespaces_clause.
    def enterXml_namespaces_clause(self, ctx:PlSqlParser.Xml_namespaces_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_namespaces_clause.
    def exitXml_namespaces_clause(self, ctx:PlSqlParser.Xml_namespaces_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_table_column.
    def enterXml_table_column(self, ctx:PlSqlParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_table_column.
    def exitXml_table_column(self, ctx:PlSqlParser.Xml_table_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_general_default_part.
    def enterXml_general_default_part(self, ctx:PlSqlParser.Xml_general_default_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_general_default_part.
    def exitXml_general_default_part(self, ctx:PlSqlParser.Xml_general_default_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_multiuse_expression_element.
    def enterXml_multiuse_expression_element(self, ctx:PlSqlParser.Xml_multiuse_expression_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_multiuse_expression_element.
    def exitXml_multiuse_expression_element(self, ctx:PlSqlParser.Xml_multiuse_expression_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlroot_param_version_part.
    def enterXmlroot_param_version_part(self, ctx:PlSqlParser.Xmlroot_param_version_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlroot_param_version_part.
    def exitXmlroot_param_version_part(self, ctx:PlSqlParser.Xmlroot_param_version_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlroot_param_standalone_part.
    def enterXmlroot_param_standalone_part(self, ctx:PlSqlParser.Xmlroot_param_standalone_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlroot_param_standalone_part.
    def exitXmlroot_param_standalone_part(self, ctx:PlSqlParser.Xmlroot_param_standalone_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_enconding_part.
    def enterXmlserialize_param_enconding_part(self, ctx:PlSqlParser.Xmlserialize_param_enconding_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_enconding_part.
    def exitXmlserialize_param_enconding_part(self, ctx:PlSqlParser.Xmlserialize_param_enconding_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_version_part.
    def enterXmlserialize_param_version_part(self, ctx:PlSqlParser.Xmlserialize_param_version_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_version_part.
    def exitXmlserialize_param_version_part(self, ctx:PlSqlParser.Xmlserialize_param_version_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_ident_part.
    def enterXmlserialize_param_ident_part(self, ctx:PlSqlParser.Xmlserialize_param_ident_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_ident_part.
    def exitXmlserialize_param_ident_part(self, ctx:PlSqlParser.Xmlserialize_param_ident_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_plus_command.
    def enterSql_plus_command(self, ctx:PlSqlParser.Sql_plus_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_plus_command.
    def exitSql_plus_command(self, ctx:PlSqlParser.Sql_plus_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#whenever_command.
    def enterWhenever_command(self, ctx:PlSqlParser.Whenever_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#whenever_command.
    def exitWhenever_command(self, ctx:PlSqlParser.Whenever_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_command.
    def enterSet_command(self, ctx:PlSqlParser.Set_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_command.
    def exitSet_command(self, ctx:PlSqlParser.Set_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exit_command.
    def enterExit_command(self, ctx:PlSqlParser.Exit_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exit_command.
    def exitExit_command(self, ctx:PlSqlParser.Exit_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#prompt_command.
    def enterPrompt_command(self, ctx:PlSqlParser.Prompt_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#prompt_command.
    def exitPrompt_command(self, ctx:PlSqlParser.Prompt_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#show_errors_command.
    def enterShow_errors_command(self, ctx:PlSqlParser.Show_errors_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#show_errors_command.
    def exitShow_errors_command(self, ctx:PlSqlParser.Show_errors_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_extension_clause.
    def enterPartition_extension_clause(self, ctx:PlSqlParser.Partition_extension_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_extension_clause.
    def exitPartition_extension_clause(self, ctx:PlSqlParser.Partition_extension_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_alias.
    def enterColumn_alias(self, ctx:PlSqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_alias.
    def exitColumn_alias(self, ctx:PlSqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_alias.
    def enterTable_alias(self, ctx:PlSqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_alias.
    def exitTable_alias(self, ctx:PlSqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alias_quoted_string.
    def enterAlias_quoted_string(self, ctx:PlSqlParser.Alias_quoted_stringContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alias_quoted_string.
    def exitAlias_quoted_string(self, ctx:PlSqlParser.Alias_quoted_stringContext):
        pass


    # Enter a parse tree produced by PlSqlParser#where_clause.
    def enterWhere_clause(self, ctx:PlSqlParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#where_clause.
    def exitWhere_clause(self, ctx:PlSqlParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#current_of_clause.
    def enterCurrent_of_clause(self, ctx:PlSqlParser.Current_of_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#current_of_clause.
    def exitCurrent_of_clause(self, ctx:PlSqlParser.Current_of_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#into_clause.
    def enterInto_clause(self, ctx:PlSqlParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#into_clause.
    def exitInto_clause(self, ctx:PlSqlParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_column_name.
    def enterXml_column_name(self, ctx:PlSqlParser.Xml_column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_column_name.
    def exitXml_column_name(self, ctx:PlSqlParser.Xml_column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cost_class_name.
    def enterCost_class_name(self, ctx:PlSqlParser.Cost_class_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cost_class_name.
    def exitCost_class_name(self, ctx:PlSqlParser.Cost_class_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_name.
    def enterAttribute_name(self, ctx:PlSqlParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_name.
    def exitAttribute_name(self, ctx:PlSqlParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#savepoint_name.
    def enterSavepoint_name(self, ctx:PlSqlParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#savepoint_name.
    def exitSavepoint_name(self, ctx:PlSqlParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollback_segment_name.
    def enterRollback_segment_name(self, ctx:PlSqlParser.Rollback_segment_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollback_segment_name.
    def exitRollback_segment_name(self, ctx:PlSqlParser.Rollback_segment_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_var_name.
    def enterTable_var_name(self, ctx:PlSqlParser.Table_var_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_var_name.
    def exitTable_var_name(self, ctx:PlSqlParser.Table_var_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#schema_name.
    def enterSchema_name(self, ctx:PlSqlParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#schema_name.
    def exitSchema_name(self, ctx:PlSqlParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#routine_name.
    def enterRoutine_name(self, ctx:PlSqlParser.Routine_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#routine_name.
    def exitRoutine_name(self, ctx:PlSqlParser.Routine_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_name.
    def enterPackage_name(self, ctx:PlSqlParser.Package_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_name.
    def exitPackage_name(self, ctx:PlSqlParser.Package_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#implementation_type_name.
    def enterImplementation_type_name(self, ctx:PlSqlParser.Implementation_type_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#implementation_type_name.
    def exitImplementation_type_name(self, ctx:PlSqlParser.Implementation_type_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter_name.
    def enterParameter_name(self, ctx:PlSqlParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter_name.
    def exitParameter_name(self, ctx:PlSqlParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_model_name.
    def enterReference_model_name(self, ctx:PlSqlParser.Reference_model_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_model_name.
    def exitReference_model_name(self, ctx:PlSqlParser.Reference_model_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#main_model_name.
    def enterMain_model_name(self, ctx:PlSqlParser.Main_model_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#main_model_name.
    def exitMain_model_name(self, ctx:PlSqlParser.Main_model_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#aggregate_function_name.
    def enterAggregate_function_name(self, ctx:PlSqlParser.Aggregate_function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#aggregate_function_name.
    def exitAggregate_function_name(self, ctx:PlSqlParser.Aggregate_function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_name.
    def enterQuery_name(self, ctx:PlSqlParser.Query_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_name.
    def exitQuery_name(self, ctx:PlSqlParser.Query_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constraint_name.
    def enterConstraint_name(self, ctx:PlSqlParser.Constraint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constraint_name.
    def exitConstraint_name(self, ctx:PlSqlParser.Constraint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#label_name.
    def enterLabel_name(self, ctx:PlSqlParser.Label_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#label_name.
    def exitLabel_name(self, ctx:PlSqlParser.Label_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_name.
    def enterType_name(self, ctx:PlSqlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_name.
    def exitType_name(self, ctx:PlSqlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_name.
    def enterSequence_name(self, ctx:PlSqlParser.Sequence_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_name.
    def exitSequence_name(self, ctx:PlSqlParser.Sequence_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_name.
    def enterException_name(self, ctx:PlSqlParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_name.
    def exitException_name(self, ctx:PlSqlParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_name.
    def enterFunction_name(self, ctx:PlSqlParser.Function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_name.
    def exitFunction_name(self, ctx:PlSqlParser.Function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#procedure_name.
    def enterProcedure_name(self, ctx:PlSqlParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#procedure_name.
    def exitProcedure_name(self, ctx:PlSqlParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_name.
    def enterTrigger_name(self, ctx:PlSqlParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_name.
    def exitTrigger_name(self, ctx:PlSqlParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#variable_name.
    def enterVariable_name(self, ctx:PlSqlParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#variable_name.
    def exitVariable_name(self, ctx:PlSqlParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_name.
    def enterIndex_name(self, ctx:PlSqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_name.
    def exitIndex_name(self, ctx:PlSqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_name.
    def enterCursor_name(self, ctx:PlSqlParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_name.
    def exitCursor_name(self, ctx:PlSqlParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_name.
    def enterRecord_name(self, ctx:PlSqlParser.Record_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_name.
    def exitRecord_name(self, ctx:PlSqlParser.Record_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collection_name.
    def enterCollection_name(self, ctx:PlSqlParser.Collection_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collection_name.
    def exitCollection_name(self, ctx:PlSqlParser.Collection_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#link_name.
    def enterLink_name(self, ctx:PlSqlParser.Link_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#link_name.
    def exitLink_name(self, ctx:PlSqlParser.Link_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_name.
    def enterColumn_name(self, ctx:PlSqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_name.
    def exitColumn_name(self, ctx:PlSqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tableview_name.
    def enterTableview_name(self, ctx:PlSqlParser.Tableview_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tableview_name.
    def exitTableview_name(self, ctx:PlSqlParser.Tableview_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dot_id.
    def enterDot_id(self, ctx:PlSqlParser.Dot_idContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dot_id.
    def exitDot_id(self, ctx:PlSqlParser.Dot_idContext):
        pass


    # Enter a parse tree produced by PlSqlParser#star.
    def enterStar(self, ctx:PlSqlParser.StarContext):
        pass

    # Exit a parse tree produced by PlSqlParser#star.
    def exitStar(self, ctx:PlSqlParser.StarContext):
        pass


    # Enter a parse tree produced by PlSqlParser#keep_clause.
    def enterKeep_clause(self, ctx:PlSqlParser.Keep_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#keep_clause.
    def exitKeep_clause(self, ctx:PlSqlParser.Keep_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument.
    def enterFunction_argument(self, ctx:PlSqlParser.Function_argumentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument.
    def exitFunction_argument(self, ctx:PlSqlParser.Function_argumentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument_analytic.
    def enterFunction_argument_analytic(self, ctx:PlSqlParser.Function_argument_analyticContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument_analytic.
    def exitFunction_argument_analytic(self, ctx:PlSqlParser.Function_argument_analyticContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument_modeling.
    def enterFunction_argument_modeling(self, ctx:PlSqlParser.Function_argument_modelingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument_modeling.
    def exitFunction_argument_modeling(self, ctx:PlSqlParser.Function_argument_modelingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#respect_or_ignore_nulls.
    def enterRespect_or_ignore_nulls(self, ctx:PlSqlParser.Respect_or_ignore_nullsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#respect_or_ignore_nulls.
    def exitRespect_or_ignore_nulls(self, ctx:PlSqlParser.Respect_or_ignore_nullsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#argument.
    def enterArgument(self, ctx:PlSqlParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#argument.
    def exitArgument(self, ctx:PlSqlParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_spec.
    def enterType_spec(self, ctx:PlSqlParser.Type_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_spec.
    def exitType_spec(self, ctx:PlSqlParser.Type_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datatype.
    def enterDatatype(self, ctx:PlSqlParser.DatatypeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datatype.
    def exitDatatype(self, ctx:PlSqlParser.DatatypeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#precision_part.
    def enterPrecision_part(self, ctx:PlSqlParser.Precision_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#precision_part.
    def exitPrecision_part(self, ctx:PlSqlParser.Precision_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#native_datatype_element.
    def enterNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#native_datatype_element.
    def exitNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#bind_variable.
    def enterBind_variable(self, ctx:PlSqlParser.Bind_variableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#bind_variable.
    def exitBind_variable(self, ctx:PlSqlParser.Bind_variableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#FuncCall.
    def enterFuncCall(self, ctx:PlSqlParser.FuncCallContext):
        pass

    # Exit a parse tree produced by PlSqlParser#FuncCall.
    def exitFuncCall(self, ctx:PlSqlParser.FuncCallContext):
        pass


    # Enter a parse tree produced by PlSqlParser#Identifier.
    def enterIdentifier(self, ctx:PlSqlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PlSqlParser#Identifier.
    def exitIdentifier(self, ctx:PlSqlParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_element.
    def enterTable_element(self, ctx:PlSqlParser.Table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_element.
    def exitTable_element(self, ctx:PlSqlParser.Table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constant.
    def enterConstant(self, ctx:PlSqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constant.
    def exitConstant(self, ctx:PlSqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric.
    def enterNumeric(self, ctx:PlSqlParser.NumericContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric.
    def exitNumeric(self, ctx:PlSqlParser.NumericContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric_negative.
    def enterNumeric_negative(self, ctx:PlSqlParser.Numeric_negativeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric_negative.
    def exitNumeric_negative(self, ctx:PlSqlParser.Numeric_negativeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quoted_string.
    def enterQuoted_string(self, ctx:PlSqlParser.Quoted_stringContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quoted_string.
    def exitQuoted_string(self, ctx:PlSqlParser.Quoted_stringContext):
        pass


    # Enter a parse tree produced by PlSqlParser#r_id.
    def enterR_id(self, ctx:PlSqlParser.R_idContext):
        pass

    # Exit a parse tree produced by PlSqlParser#r_id.
    def exitR_id(self, ctx:PlSqlParser.R_idContext):
        pass


    # Enter a parse tree produced by PlSqlParser#id_expression.
    def enterId_expression(self, ctx:PlSqlParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#id_expression.
    def exitId_expression(self, ctx:PlSqlParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#not_equal_op.
    def enterNot_equal_op(self, ctx:PlSqlParser.Not_equal_opContext):
        pass

    # Exit a parse tree produced by PlSqlParser#not_equal_op.
    def exitNot_equal_op(self, ctx:PlSqlParser.Not_equal_opContext):
        pass


    # Enter a parse tree produced by PlSqlParser#greater_than_or_equals_op.
    def enterGreater_than_or_equals_op(self, ctx:PlSqlParser.Greater_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by PlSqlParser#greater_than_or_equals_op.
    def exitGreater_than_or_equals_op(self, ctx:PlSqlParser.Greater_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by PlSqlParser#less_than_or_equals_op.
    def enterLess_than_or_equals_op(self, ctx:PlSqlParser.Less_than_or_equals_opContext):
        pass

    # Exit a parse tree produced by PlSqlParser#less_than_or_equals_op.
    def exitLess_than_or_equals_op(self, ctx:PlSqlParser.Less_than_or_equals_opContext):
        pass


    # Enter a parse tree produced by PlSqlParser#concatenation_op.
    def enterConcatenation_op(self, ctx:PlSqlParser.Concatenation_opContext):
        pass

    # Exit a parse tree produced by PlSqlParser#concatenation_op.
    def exitConcatenation_op(self, ctx:PlSqlParser.Concatenation_opContext):
        pass


    # Enter a parse tree produced by PlSqlParser#outer_join_sign.
    def enterOuter_join_sign(self, ctx:PlSqlParser.Outer_join_signContext):
        pass

    # Exit a parse tree produced by PlSqlParser#outer_join_sign.
    def exitOuter_join_sign(self, ctx:PlSqlParser.Outer_join_signContext):
        pass


    # Enter a parse tree produced by PlSqlParser#regular_id.
    def enterRegular_id(self, ctx:PlSqlParser.Regular_idContext):
        pass

    # Exit a parse tree produced by PlSqlParser#regular_id.
    def exitRegular_id(self, ctx:PlSqlParser.Regular_idContext):
        pass


