import pandas as pd
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure
class DataProcessing:
	def generateDataProcessing(self):
		transformations=data_transformations.DataTransformations()
#-----------------New DataProcessing-----------------
		data_model_impute_sex_in=pd.read_csv('../data_model.csv')

		
		
#-----------------New DataProcessing-----------------
		data_model_impute_IRSCHOOL_in=pd.read_csv('../data_model.csv')

		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ETHNICITY_in=pd.read_csv('../data_model.csv')

		
		
#-----------------New DataProcessing-----------------
		data_model_impute_in=pd.read_csv('../data_model.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_impute_ACADEMIC_INTEREST_2_in=pd.read_csv('../data_model.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_impute_mean_in=pd.read_csv('../data_model.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_impute_linear_interpolation_in=pd.read_csv('../data_model.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_row_filter_in=pd.read_csv('../workflow_datasets/data_model_impute_out.csv')


		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_column_cont_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_column_cat_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_map_territory_in=pd.read_csv('../workflow_datasets/data_model_col_filter_out.csv')


		print('Transformation of type FixValue-FixValue')
		data_model_map_territory_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_territory_in, fix_value_input=A, fix_value_output=0,
		                                      data_type_input = None,
		                                      data_type_output = None, field = 'TERRITORY')
		
		
		print('Transformation of type FixValue-FixValue')
		data_model_map_territory_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_territory_in, fix_value_input=N, fix_value_output=0,
		                                      data_type_input = None,
		                                      data_type_output = None, field = 'TERRITORY')
		
		
#-----------------New DataProcessing-----------------
		data_model_map_Instate_in=pd.read_csv('../workflow_datasets/data_model_map_territory_out.csv')


		print('Transformation of type FixValue-FixValue')
		data_model_map_Instate_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_Instate_in, fix_value_input=Y, fix_value_output=1,
		                                      data_type_input = None,
		                                      data_type_output = None, field = 'Instate')
		
		
		print('Transformation of type FixValue-FixValue')
		data_model_map_Instate_out=transformations.transform_fix_value_fix_value(data_dictionary=data_model_map_Instate_in, fix_value_input=N, fix_value_output=0,
		                                      data_type_input = None,
		                                      data_type_output = None, field = 'Instate')
		
		
#-----------------New DataProcessing-----------------
		data_model_stringToNumber_in=pd.read_csv('../workflow_datasets/data_model_map_instate_out.csv')


#-----------------New DataProcessing-----------------
		data_model_impute_outlier_closest_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')


		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')


		
		
		
		
		
		
		
		
		
		
		
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')


		
		
		
		
		
		
		
		
		
		
		
		















dp=DataProcessing()
dp.generateDataProcessing()
