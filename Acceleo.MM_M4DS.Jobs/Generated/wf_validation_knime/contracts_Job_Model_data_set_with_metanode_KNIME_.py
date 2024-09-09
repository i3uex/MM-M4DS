import os

import pandas as pd
import numpy as np
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType
from helpers.logger import set_logger

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')
	if os.path.exists('./knime_dataDictionaries/missing_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	missing_values_imputeByDerivedValue_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df, field='sex', 
									missing_values=missing_values_imputeByDerivedValue_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByMostFrequent(sex)_PRE_value_range VALIDATED')
	else:
		print('PRECONDITION imputeMissingByMostFrequent(sex)_PRE_value_range NOT VALIDATED')
	
	missing_values_imputeByDerivedValue_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df, field='IRSCHOOL', 
									missing_values=missing_values_imputeByDerivedValue_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByMostFrequent(IRSCHOOL)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByDerivedValue_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary_df, field='ETHNICITY', 
									missing_values=missing_values_imputeByDerivedValue_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByMostFrequent(ETHNICITY)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByDerivedValue_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df, field='sex', 
									missing_values=missing_values_imputeByDerivedValue_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION POST_value_range_impute_sex_columns VALIDATED')
	else:
		print('POSTCONDITION POST_value_range_impute_sex_columns NOT VALIDATED')
	
	missing_values_imputeByDerivedValue_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df, field='IRSCHOOL', 
									missing_values=missing_values_imputeByDerivedValue_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns VALIDATED')
	else:
		print('POSTCONDITION POST_value_range_impute_IRSCHOOL_columns NOT VALIDATED')
	
	missing_values_imputeByDerivedValue_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary_df, field='ETHNICITY', 
									missing_values=missing_values_imputeByDerivedValue_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns VALIDATED')
	else:
		print('POSTCONDITION POST_value_range_impute_ETHNICITY_columns NOT VALIDATED')
	
	
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/missing_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	missing_values_imputeByFixValue_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df, field='ACADEMIC_INTEREST_2', 
									missing_values=missing_values_imputeByFixValue_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByFixValue_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary_df, field='ACADEMIC_INTEREST_1', 
									missing_values=missing_values_imputeByFixValue_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByFixValue_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df, field='ACADEMIC_INTEREST_2', 
									missing_values=missing_values_imputeByFixValue_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_2)_POST_valueRange NOT VALIDATED')
	
	missing_values_imputeByFixValue_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__output_dataDictionary_df, field='ACADEMIC_INTEREST_1', 
									missing_values=missing_values_imputeByFixValue_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeMissingByFixValue(ACADEMIC_INTEREST_1)_POST_valueRange NOT VALIDATED')
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	imputeMissingByMean_avg_income_distance__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/missing_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		imputeMissingByMean_avg_income_distance__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	missing_values_imputeByNumericOp_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByMean_avg_income_distance__input_dataDictionary_df, field='avg_income', 
									missing_values=missing_values_imputeByNumericOp_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByMean(avg_income)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByMean(avg_income)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByNumericOp_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByMean_avg_income_distance__input_dataDictionary_df, field='distance', 
									missing_values=missing_values_imputeByNumericOp_PRE_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION imputeMissingByMean(distance)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByMean(distance)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByNumericOp_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByMean_avg_income_distance__output_dataDictionary_df, field='avg_income', 
									missing_values=missing_values_imputeByNumericOp_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeMissingByMean(avg_income)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeMissingByMean(avg_income)_POST_valueRange NOT VALIDATED')
	
	missing_values_imputeByNumericOp_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByMean_avg_income_distance__output_dataDictionary_df, field='distance', 
									missing_values=missing_values_imputeByNumericOp_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeMissingByMean(distance)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeMissingByMean(distance)_POST_valueRange NOT VALIDATED')
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	imputeMissingByLinearInterpolation_satscore__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_input_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/missing_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	missing_values_imputeByNumericOp_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=imputeMissingByLinearInterpolation_satscore__input_dataDictionary_df, field='satscore', 
									missing_values=missing_values_imputeByNumericOp_PRE_valueRange,
									quant_op=Operator(3), quant_rel=60.0/100):
		print('PRECONDITION imputeMissingByLinearInterpolation(satscore)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeMissingByLinearInterpolation(satscore)_PRE_valueRange NOT VALIDATED')
	
	missing_values_imputeByNumericOp_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=imputeMissingByLinearInterpolation_satscore__output_dataDictionary_df, field='satscore', 
									missing_values=missing_values_imputeByNumericOp_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeMissingByLinearInterpolation(satscore)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeMissingByLinearInterpolation(satscore)_POST_valueRange NOT VALIDATED')
	
	
	
	#-----------------New DataProcessing-----------------
	rowFilterRange_init_span__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/missing_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		rowFilterRange_init_span__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=rowFilterRange_init_span__input_dataDictionary_df,
	                                	closure_type=Closure(2), belong_op=Belong(1), field='init_span'):
		print('PRECONDITION rowFilter(init_span)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION rowFilter(init_span)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_fix_value_range(value=-216, data_dictionary=rowFilterRange_init_span__output_dataDictionary_df, belong_op=Belong(1), field='init_span',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION rowFilter(init_span)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION rowFilter(init_span)_POST_valueRange NOT VALIDATED')
	
	#-----------------New DataProcessing-----------------
	columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/rowFilter_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')

	field_list_columnFilter_PRE_field_range=['TRAVEL_INIT_CNTCTS', 'REFERRAL_CNTCTS', 'telecq', 'stuemail', 'interest']
	if contract_pre_post.check_field_range(fields=field_list_columnFilter_PRE_field_range,
								data_dictionary=columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataDictionary_df,
								belong_op=Belong(0)):
		print('PRECONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange VALIDATED')
	else:
		print('PRECONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_PRE_fieldRange NOT VALIDATED')
	
	
	field_list_columnFilter_POST_field_range=['stuemail', 'interest', 'telecq', 'TRAVEL_INIT_CNTCTS', 'REFERRAL_CNTCTS']
	if contract_pre_post.check_field_range(fields=field_list_columnFilter_POST_field_range,
								data_dictionary=columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__output_dataDictionary_df,
								belong_op=Belong(1)):
		print('POSTCONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange VALIDATED')
	else:
		print('POSTCONDITION columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_POST_fieldRange NOT VALIDATED')
	
	
	#-----------------New DataProcessing-----------------
	mapping_TERRITORY__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/columnFilter_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		mapping_TERRITORY__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_fix_value_range(value='A', data_dictionary=mapping_TERRITORY__input_dataDictionary_df, belong_op=Belong(0), field='TERRITORY',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION mapping(TERRITORY)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION mapping(TERRITORY)_PRE_valueRange NOT VALIDATED')
	if contract_pre_post.check_fix_value_range(value='N', data_dictionary=mapping_TERRITORY__input_dataDictionary_df, belong_op=Belong(0), field='TERRITORY',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION mapping(TERRITORY)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION mapping(TERRITORY)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_fix_value_range(value='A', data_dictionary=mapping_TERRITORY__output_dataDictionary_df, belong_op=Belong(1), field='TERRITORY',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION mapping(TERRITORY)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION mapping(TERRITORY)_POST_valueRange NOT VALIDATED')
	if contract_pre_post.check_fix_value_range(value='N', data_dictionary=mapping_TERRITORY__output_dataDictionary_df, belong_op=Belong(1), field='TERRITORY',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION mapping(TERRITORY)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION mapping(TERRITORY)_POST_valueRange NOT VALIDATED')
	
	
	input_values_list_def_INV_condition=['A', 'N']
	output_values_list_def_INV_condition=[0, 0]
	
	data_type_input_list_def_INV_condition=[DataType(0), DataType(0)]
	data_type_output_list_def_INV_condition=[DataType(2), DataType(2)]
	
	if contract_invariants.check_inv_fix_value_fix_value(data_dictionary_in=mapping_TERRITORY__input_dataDictionary_df,
											data_dictionary_out=mapping_TERRITORY__output_dataDictionary_df,
											input_values_list=input_values_list_def_INV_condition, 
											output_values_list=output_values_list_def_INV_condition,
											belong_op_in=Belong(0),
											belong_op_out=Belong(0),
											data_type_input_list=data_type_input_list_def_INV_condition,
											data_type_output_list=data_type_output_list_def_INV_condition,
											field_in='TERRITORY', field_out='TERRITORY'):
		print('INVARIANT Mapping(TERRITORY)_INV_condition VALIDATED')
	else:
		print('INVARIANT Mapping(TERRITORY)_INV_condition NOT VALIDATED')
	
	
	#-----------------New DataProcessing-----------------
	mapping_Instate__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		mapping_Instate__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_fix_value_range(value='Y', data_dictionary=mapping_Instate__input_dataDictionary_df, belong_op=Belong(0), field='Instate',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION mapping(Instate)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION mapping(Instate)_PRE_valueRange NOT VALIDATED')
	if contract_pre_post.check_fix_value_range(value='N', data_dictionary=mapping_Instate__input_dataDictionary_df, belong_op=Belong(0), field='Instate',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION mapping(Instate)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION mapping(Instate)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_fix_value_range(value='Y', data_dictionary=mapping_Instate__output_dataDictionary_df, belong_op=Belong(1), field='Instate',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION mapping(Instate)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION mapping(Instate)_POST_valueRange NOT VALIDATED')
	if contract_pre_post.check_fix_value_range(value='N', data_dictionary=mapping_Instate__output_dataDictionary_df, belong_op=Belong(1), field='Instate',
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION mapping(Instate)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION mapping(Instate)_POST_valueRange NOT VALIDATED')
	
	
	input_values_list_def_INV_condition=['Y', 'N']
	output_values_list_def_INV_condition=[1, 0]
	
	data_type_input_list_def_INV_condition=[DataType(0), DataType(0)]
	data_type_output_list_def_INV_condition=[DataType(2), DataType(2)]
	
	if contract_invariants.check_inv_fix_value_fix_value(data_dictionary_in=mapping_Instate__input_dataDictionary_df,
											data_dictionary_out=mapping_Instate__output_dataDictionary_df,
											input_values_list=input_values_list_def_INV_condition, 
											output_values_list=output_values_list_def_INV_condition,
											belong_op_in=Belong(0),
											belong_op_out=Belong(0),
											data_type_input_list=data_type_input_list_def_INV_condition,
											data_type_output_list=data_type_output_list_def_INV_condition,
											field_in='Instate', field_out='Instate'):
		print('INVARIANT mapping(Instate)_INV_condition VALIDATED')
	else:
		print('INVARIANT mapping(Instate)_INV_condition NOT VALIDATED')
	
	
	#-----------------New DataProcessing-----------------
	stringToNumber_TERRITORY_Instate__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		stringToNumber_TERRITORY_Instate__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')

	if contract_invariants.check_inv_missing_value_missing_value(data_dictionary_in=stringToNumber_TERRITORY_Instate__input_dataDictionary_df,
											data_dictionary_out=stringToNumber_TERRITORY_Instate__output_dataDictionary_df,
											belong_op_out=Belong(1), field_in='TERRITORY', field_out='TERRITORY'):
		print('INVARIANT INV_condition_TERRITORY VALIDATED')
	else:
		print('INVARIANT INV_condition_TERRITORY NOT VALIDATED')
	
	
	if contract_invariants.check_inv_missing_value_missing_value(data_dictionary_in=stringToNumber_TERRITORY_Instate__input_dataDictionary_df,
											data_dictionary_out=stringToNumber_TERRITORY_Instate__output_dataDictionary_df,
											belong_op_out=Belong(1), field_in='Instate', field_out='Instate'):
		print('INVARIANT INV_condition_Instate VALIDATED')
	else:
		print('INVARIANT INV_condition_Instate NOT VALIDATED')
	
	
	#-----------------New DataProcessing-----------------
	imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df, field='avg_income', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION imputeOutlierByClosest(avg_income)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeOutlierByClosest(avg_income)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df, field='distance', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION imputeOutlierByClosest(distance)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeOutlierByClosest(distance)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_outliers(belong_op=Belong(0), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__input_dataDictionary_df, field='Instate', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('PRECONDITION imputeOutlierByClosest(Instate)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION imputeOutlierByClosest(Instate)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df, field='avg_income', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeOutlierByClosest(avg_income)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeOutlierByClosest(avg_income)_POST_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df, field='distance', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeOutlierByClosest(distance)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION imputeOutlierByClosest(distance)_POST_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_outliers(belong_op=Belong(1), data_dictionary=imputeOutlierByClosest_avg_income_distance_Instate__output_dataDictionary_df, field='Instate', 
									quant_abs=None, quant_rel=None, quant_op=None):
		print('POSTCONDITION imputeOutlierByClosest(Instate)_POST_valueRange´ VALIDATED')
	else:
		print('POSTCONDITION imputeOutlierByClosest(Instate)_POST_valueRange´ NOT VALIDATED')
	
	
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(0), field='TOTAL_CONTACTS'):
		print('PRECONDITION binner(TOTAL_CONTACTS)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(TOTAL_CONTACTS)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(0), field='SELF_INIT_CNTCTS'):
		print('PRECONDITION binner(SELF_INIT_CNTCTS)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(SELF_INIT_CNTCTS)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__input_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(0), field='SOLICITED_CNTCTS'):
		print('PRECONDITION binner(SOLICITED_CNTCTS)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(SOLICITED_CNTCTS)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='TOTAL_CONTACTS_binned'):
		print('POSTCONDITION binner(TOTAL_CONTACTS)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(TOTAL_CONTACTS)_POST_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='SELF_INIT_CNTCTS_binned'):
		print('POSTCONDITION binner(SELF_INIT_CNTCTS)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(SELF_INIT_CNTCTS)_POST_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=1000.0, data_dictionary=binner_TOTAL_CONTACTS_SELF_INIT_CNTCTS_SOLICITED_CNTCTS__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='SOLICITED_CNTCTS_binned'):
		print('POSTCONDITION binner(SOLICITED_CNTCTS)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(SOLICITED_CNTCTS)_POST_valueRange NOT VALIDATED')
	
	
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	binner_TERRITORY__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		binner_TERRITORY__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_TERRITORY__input_dataDictionary_df,
	                                	closure_type=Closure(3), belong_op=Belong(0), field='TERRITORY'):
		print('PRECONDITION binner(TERRITORY)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(TERRITORY)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_TERRITORY__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='TERRITORY_binned'):
		print('POSTCONDITION binner(TERRITORY)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(TERRITORY)_POST_valueRange NOT VALIDATED')
	
	
	
	#-----------------New DataProcessing-----------------
	binner_satscore__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		binner_satscore__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=2000.0, data_dictionary=binner_satscore__input_dataDictionary_df,
	                                	closure_type=Closure(3), belong_op=Belong(0), field='satscore'):
		print('PRECONDITION binner(satscore)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(satscore)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=-1000.0, right_margin=2000.0, data_dictionary=binner_satscore__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='satscore_binned'):
		print('POSTCONDITION binner(satscore)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(satscore)_POST_valueRange NOT VALIDATED')
	
	
	
	#-----------------New DataProcessing-----------------
	binner_avg_income__input_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep=',')

	if os.path.exists('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		binner_avg_income__output_dataDictionary_df=pd.read_csv('./knime_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	if contract_pre_post.check_interval_range_float(left_margin=9.0, right_margin=100000.0, data_dictionary=binner_avg_income__input_dataDictionary_df,
	                                	closure_type=Closure(3), belong_op=Belong(0), field='avg_income'):
		print('PRECONDITION binner(avg_income)_PRE_valueRange VALIDATED')
	else:
		print('PRECONDITION binner(avg_income)_PRE_valueRange NOT VALIDATED')
	
	if contract_pre_post.check_interval_range_float(left_margin=9.0, right_margin=100000.0, data_dictionary=binner_avg_income__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='avg_income_binned'):
		print('POSTCONDITION binner(avg_income)_POST_valueRange VALIDATED')
	else:
		print('POSTCONDITION binner(avg_income)_POST_valueRange NOT VALIDATED')
	
	
	














set_logger("contracts")
generateWorkflow()
