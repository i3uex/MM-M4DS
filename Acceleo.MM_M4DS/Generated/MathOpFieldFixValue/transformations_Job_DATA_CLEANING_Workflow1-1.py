import pandas as pd
import numpy as np
import functions.data_transformations as data_transformations
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType, MapOperation, MathOperator
from helpers.logger import set_logger
import pyarrow
from functions.PMML import PMMLModel

def generateWorkflow():

	#-----------------New DataProcessing-----------------
	binner_native-country__input_dataDictionary_df=pd.read_parquet('esta/data/output/CSV_Reader_output_dataDictionary.parquet')
	binner_native-country__input_dataDictionary_df.to_parquet('esta/data/output/CSV_Reader_output_dataDictionary.parquet')
	binner_native-country__input_dataDictionary_transformed=binner_native-country__input_dataDictionary_df.copy()
	binner_native-country__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_native-country__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'native-country', field_out = 'prediction')
	
	binner_native-country__output_dataDictionary_df=binner_native-country__input_dataDictionary_transformed
	binner_native-country__output_dataDictionary_df.to_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	binner_native-country__output_dataDictionary_df=pd.read_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	binner_native-country__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_native-country__input_dataDictionary_transformed,
																  left_margin=-1000000.0, right_margin=1000000.0,
																  closure_type=Closure(0),
																  fix_value_output='PART-TIME',
							                                      data_type_output = DataType(0),
																  field_in = 'native-country',
																  field_out = 'prediction')
	
	binner_native-country__output_dataDictionary_df=binner_native-country__input_dataDictionary_transformed
	binner_native-country__output_dataDictionary_df.to_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	binner_native-country__output_dataDictionary_df=pd.read_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	binner_native-country__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_native-country__input_dataDictionary_transformed,
																  left_margin=40.0, right_margin=1000000.0,
																  closure_type=Closure(2),
																  fix_value_output='FULL-TIME',
							                                      data_type_output = DataType(0),
																  field_in = 'native-country',
																  field_out = 'prediction')
	
	binner_native-country__output_dataDictionary_df=binner_native-country__input_dataDictionary_transformed
	binner_native-country__output_dataDictionary_df.to_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	binner_native-country__output_dataDictionary_df=pd.read_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	mapping_native-country__input_dataDictionary_df=pd.read_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')

	input_values_list=['-']
	output_values_list=[' ']
	data_type_input_list=[DataType(0)]
	data_type_output_list=[DataType(0)]
	map_operation_list=[MapOperation(1)]
	
	mapping_native-country__output_dataDictionary_df=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_native-country__input_dataDictionary_df, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list,
																  map_operation_list = map_operation_list,
																  field_in = 'native-country', field_out = 'native-country')
	
	mapping_native-country__output_dataDictionary_df.to_parquet('esta/data/output/String_Manipulation_output_dataDictionary.parquet')
	mapping_native-country__output_dataDictionary_df=pd.read_parquet('esta/data/output/String_Manipulation_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_df=pd.read_parquet('esta/data/output/String_Manipulation_output_dataDictionary.parquet')

	mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_transformed=mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_df.copy()
	mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_transformed=data_transformations.transform_math_operation(data_dictionary=mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_transformed,
																math_op=MathOperator(1), field_out='Age-of-birth',
																firstOperand=1994, isFieldFirst=False,
																secondOperand='age', isFieldSecond=True)
	
	mathOperationFieldFixValue_Age-of-birth__output_dataDictionary_df=mathOperationFieldFixValue_Age-of-birth__input_dataDictionary_transformed
	mathOperationFieldFixValue_Age-of-birth__output_dataDictionary_df.to_parquet('esta/data/output/Math_Formula_output_dataDictionary.parquet')
	mathOperationFieldFixValue_Age-of-birth__output_dataDictionary_df=pd.read_parquet('esta/data/output/Math_Formula_output_dataDictionary.parquet')
	



set_logger("transformations")
generateWorkflow()
