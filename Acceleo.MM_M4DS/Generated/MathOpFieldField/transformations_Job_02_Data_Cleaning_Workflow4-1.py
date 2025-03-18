import pandas as pd
import numpy as np
import functions.data_transformations as data_transformations
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType
from helpers.logger import set_logger
import pyarrow
from functions.PMML import PMMLModel

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_df=pd.read_parquet('ruta/data/output/CSV_Reader_output_dataDictionary.parquet')

	mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_transformed=mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_df.copy()
	mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_transformed=data_transformations.transform_math_operation(data_dictionary=mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_transformed,
																math_op=MathOperator(1), field_out='Difference in Latitude/Altitude',
																firstOperand='Latitude', isFieldFirst=True,
																secondOperand='Altitude', isFieldSecond=True)
	
	mathOperationFieldField_Difference_in_Latitude/Altitude__output_dataDictionary_df=mathOperationFieldField_Difference_in_Latitude/Altitude__input_dataDictionary_transformed
	mathOperationFieldField_Difference_in_Latitude/Altitude__output_dataDictionary_df.to_parquet('ruta/data/output/Math_Formula_output_dataDictionary.parquet')
	mathOperationFieldField_Difference_in_Latitude/Altitude__output_dataDictionary_df=pd.read_parquet('ruta/data/output/Math_Formula_output_dataDictionary.parquet')
	

set_logger("transformations")
generateWorkflow()
