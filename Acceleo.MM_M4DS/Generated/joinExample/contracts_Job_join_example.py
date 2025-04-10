import os

import pandas as pd
import numpy as np
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType, MapOperation, MathOperator
from helpers.logger import set_logger
import pyarrow
from functions.PMML import PMMLModel

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	join_Name_with_City__input_dataDictionary_df=pd.read_parquet('/pop/data/join_input_dataDictionary.parquet')

	if os.path.exists('/pop/data/join_output_dataDictionary.parquet'):
		join_Name_with_City__output_dataDictionary_df=pd.read_parquet('/pop/data/join_output_dataDictionary.parquet')

	if contract_invariants.check_inv_missing_value_missing_value(data_dictionary_in=join_Name_with_City__input_dataDictionary_df,
											data_dictionary_out=join_Name_with_City__output_dataDictionary_df,
											belong_op_out=Belong(1), field_in='name', field_out='Name with City'):
		print('INVARIANT INV_specialValue_condition VALIDATED')
	else:
		print('INVARIANT INV_specialValue_condition NOT VALIDATED')
	if contract_invariants.check_inv_missing_value_missing_value(data_dictionary_in=join_Name_with_City__input_dataDictionary_df,
											data_dictionary_out=join_Name_with_City__output_dataDictionary_df,
											belong_op_out=Belong(1), field_in='City', field_out='Name with City'):
		print('INVARIANT INV_specialValue_condition VALIDATED')
	else:
		print('INVARIANT INV_specialValue_condition NOT VALIDATED')
	
	
	
	
	
set_logger("contracts")
generateWorkflow()
