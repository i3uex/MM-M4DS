import pandas as pd
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure
class DataProcessing:
	def generateDataProcessing(self):
		transformations=data_transformations.DataTransformations()
#-----------------New DataProcessing-----------------
		data_model_impute_sex_in=pd.read_csv('../data_model.csv')

		
		print('parameter_impute_sex')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_IRSCHOOL_in=pd.read_csv('../data_model.csv')

		
		print('parameter_impute_IRSCHOOL')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ETHNICITY_in=pd.read_csv('../data_model.csv')

		
		print('parameter_impute_ETHNICITY')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_in=pd.read_csv('../data_model.csv')

		
		print('parameter_derivedValue_impute_mostFrequent')
		print('Missing') #SpecialTypeInput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		print('DerivedValue') #Function to call
		print('MostFrequent') #derivedTypeOutput
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ACADEMIC_INTEREST_2_in=pd.read_csv('../data_model.csv')

		
		print('parameter_fixValue_impute_fixValue')
		print('Missing') #SpecialTypeInput
		
		print('FixValue') #Function to call
		print('Unknown') #FixValueOutput
		data_model_impute_ACADEMIC_INTEREST_2_out=transformations.transform_special_value_fix_value(data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, special_type_input=SpecialType(0),
																	  fix_value_output=Unknown, missing_values_list=None
								                                      data_type_output = None, axis_param=0, field = 'ACADEMIC_INTEREST_2')
		
		
		print('FixValue') #Function to call
		print('Unknown') #FixValueOutput
		data_model_impute_ACADEMIC_INTEREST_2_out=transformations.transform_special_value_fix_value(data_dictionary=data_model_impute_ACADEMIC_INTEREST_2_in, special_type_input=SpecialType(0),
																	  fix_value_output=Unknown, missing_values_list=None
								                                      data_type_output = None, axis_param=0, field = 'ACADEMIC_INTEREST_1')
		
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_mean_in=pd.read_csv('../data_model.csv')

		
		print('parameter_num_op_impute_mean')
		print('Missing') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_linear_interpolation_in=pd.read_csv('../data_model.csv')

		
		print('parameter_num_op_impute_mean')
		print('Missing') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Mean') #NumOpOutput
		
		
		
#-----------------New DataProcessing-----------------
		data_model_row_filter_in=pd.read_csv('../workflow_datasets/data_model_impute_out.csv')

		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_column_cont_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')

		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_column_cat_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')

		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_map_territory_in=pd.read_csv('../workflow_datasets/data_model_col_filter_out.csv')

		
		print('Transformation of type FixValue-FixValue')
		
		input_values_list_parameter_map_territory_A=['A', 'N']
		output_values_list_parameter_map_territory_A=['0', '0']
		data_type_input_list_parameter_map_territory_A=[DataType(0), DataType(0)]
		data_type_output_list_parameter_map_territory_A=[DataType(0), DataType(0)]
		
		
		data_model_map_territory_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_territory_in, input_values_list=input_values_list_parameter_map_territory_A,
																	  output_values_list=output_values_list_parameter_map_territory_A,
								                                      data_type_input_list = data_type_input_list_parameter_map_territory_A,
								                                      data_type_output_list = data_type_output_list_parameter_map_territory_A, field = 'TERRITORY')
		
		
		
#-----------------New DataProcessing-----------------
		data_model_map_Instate_in=pd.read_csv('../workflow_datasets/data_model_map_territory_out.csv')

		
		print('Transformation of type FixValue-FixValue')
		
		input_values_list_parameter_map_instate_Y=['Y', 'N']
		output_values_list_parameter_map_instate_Y=['1', '0']
		data_type_input_list_parameter_map_instate_Y=[DataType(0), DataType(0)]
		data_type_output_list_parameter_map_instate_Y=[DataType(0), DataType(0)]
		
		
		data_model_map_Instate_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_Instate_in, input_values_list=input_values_list_parameter_map_instate_Y,
																	  output_values_list=output_values_list_parameter_map_instate_Y,
								                                      data_type_input_list = data_type_input_list_parameter_map_instate_Y,
								                                      data_type_output_list = data_type_output_list_parameter_map_instate_Y, field = 'Instate')
		
		
		
#-----------------New DataProcessing-----------------
		data_model_stringToNumber_in=pd.read_csv('../workflow_datasets/data_model_map_instate_out.csv')

		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_impute_outlier_closest_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		
		print('parameter_num_op_impute_mean')
		print('Outlier') #SpecialTypeInput
		
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		print('NumOp') #Function to call
		print('Closest') #NumOpOutput
		
		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')

		
		
		
		















dp=DataProcessing()
dp.generateDataProcessing()
