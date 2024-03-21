import pandas as pd
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator

class DataProcessing:
	def generateDataProcessing(self):
		pre_post=contract_pre_post.ContractsPrePost()
		invariants=contract_invariants.ContractsInvariants()
#-----------------New DataProcessing-----------------
		data_model_impute_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_sex_columns=['D', 4]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_in, field='sex', 
										missing_values=missing_values_PRE_value_range_impute_sex_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_PRE_value_range_impute_IRSCHOOL_columns=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_in, field='IRSCHOOL', 
										missing_values=missing_values_PRE_value_range_impute_IRSCHOOL_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_PRE_value_range_impute_ETHNICITY_columns=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_in, field='ETHNICITY', 
										missing_values=missing_values_PRE_value_range_impute_ETHNICITY_columns,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_sex_columns=['D', 4]
		
		missing_values_POST_value_range_impute_IRSCHOOL_columns=[]
		
		missing_values_POST_value_range_impute_ETHNICITY_columns=[]
		
		missing_values_INV_condition_impute_sex_columns=['D', 4]
		
		missing_values_INV_condition_impute_IRSCHOOL_columns=[]
		
		missing_values_INV_condition_impute_ETHNICITY_columns=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_sex_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_sex=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_sex_in, field='sex', 
										missing_values=missing_values_PRE_value_range_impute_sex,
										quant_op=Operator(2), quant_rel=70.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_sex=[]
		
		missing_values_INV_condition_impute_sex=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_IRSCHOOL_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_IRSCHOOL=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_IRSCHOOL_in, field='IRSCHOOL', 
										missing_values=missing_values_PRE_value_range_impute_IRSCHOOL,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_IRSCHOOL=[]
		
		missing_values_INV_condition_impute_IRSCHOOL=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_ETHNICITY_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_ETHNICITY=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_ETHNICITY_in, field='ETHNICITY', 
										missing_values=missing_values_PRE_value_range_impute_ETHNICITY,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_ETHNICITY=[]
		
		missing_values_INV_condition_impute_ETHNICITY=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_ACADEMIC_INTEREST_2_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_2=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_ACADEMIC_INTEREST_2_in, field='ACADEMIC_INTEREST_2', 
										missing_values=missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_2,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_ACADEMIC_INTEREST_2=[]
		
		missing_values_INV_condition_impute_ACADEMIC_INTEREST_2=[]
		
		missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_1=[]
		
		if pre_post.checkMissingRange(belongOp=Belong(0), dataDictionary=data_model_impute_ACADEMIC_INTEREST_2_in, field='ACADEMIC_INTEREST_1', 
										missing_values=missing_values_PRE_value_range_impute_ACADEMIC_INTEREST_1,
										quant_op=Operator(2), quant_rel=30.0/100):
			print('Precondition call returned TRUE')
		else:
			print('Precondition call returned FALSE')
		
		missing_values_POST_value_range_impute_ACADEMIC_INTEREST_1=[]
		
		missing_values_INV_condition_impute_ACADEMIC_INTEREST_1=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_mean_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_mean_avg_income=[]
		
		missing_values_PRE_value_range_impute_mean_distance=[]
		
		missing_values_POST_value_range_impute_mean_avg_income=[]
		
		missing_values_POST_value_range_impute_mean_distance=[]
		
		missing_values_INV_condition_avg_income=[]
		
		missing_values_INV_condition_distance=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_linear_interpolation_in=pd.read_csv('../data_model.csv')
		missing_values_PRE_value_range_impute_linear_interpolation_satscore=[]
		
		missing_values_POST_value_range_impute_linear_interpolation_satscore=[]
		
#-----------------New DataProcessing-----------------
		data_model_row_filter_in=pd.read_csv('../workflow_datasets/data_model_impute_out.csv')
#-----------------New DataProcessing-----------------
		data_model_column_cont_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')
#-----------------New DataProcessing-----------------
		data_model_column_cat_filter_in=pd.read_csv('../workflow_datasets/data_model_row_filter_out.csv')
#-----------------New DataProcessing-----------------
		data_model_map_territory_in=pd.read_csv('../workflow_datasets/data_model_col_filter_out.csv')
#-----------------New DataProcessing-----------------
		data_model_map_Instate_in=pd.read_csv('../workflow_datasets/data_model_map_territory_out.csv')
		missing_values_PRE_value_range_Instate=[]
		
		missing_values_POST_value_range_Instate=[]
		
#-----------------New DataProcessing-----------------
		data_model_stringToNumber_in=pd.read_csv('../workflow_datasets/data_model_map_instate_out.csv')
		missing_values_INV_condition_TERRITORY=[]
		
		missing_values_INV_condition_init1rat=[]
		
		missing_values_INV_condition_init2rat=[]
		
		missing_values_INV_condition_hscrat=[]
		
		missing_values_INV_condition_Instate=[]
		
#-----------------New DataProcessing-----------------
		data_model_impute_outlier_closest_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')
		missing_values_PRE_value_range_impute_outliers_closest_avg_income=[]
		
		missing_values_PRE_value_range_impute_outliers_closest_distance=[]
		
		missing_values_PRE_value_range_impute_outliers_closest_premiere=[]
		
		missing_values_PRE_value_range_impute_outliers_closest_sex=[]
		
		missing_values_PRE_value_range_impute_outliers_closest_Enroll=[]
		
		missing_values_PRE_value_range_impute_outliers_closest_Instate=[]
		
		missing_values_POST_value_range_impute_outliers_closest_avg_income=[]
		
		missing_values_POST_value_range_impute_outliers_closest_distance=[]
		
		missing_values_POST_value_range_impute_outliers_closest_premiere=[]
		
		missing_values_POST_value_range_impute_outliers_closest_sex=[]
		
		missing_values_POST_value_range_impute_outliers_closest_Enroll=[]
		
		missing_values_POST_value_range_impute_outliers_closest_Instate=[]
		
		missing_values_INV_condition_avg_income=[]
		
		missing_values_INV_condition_distance=[]
		
		missing_values_INV_condition_premiere=[]
		
		missing_values_INV_condition_sex=[]
		
		missing_values_INV_condition_Enroll=[]
		
		missing_values_INV_condition_Instate=[]
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')
		missing_values_PRE_binner_valueRange_TOTAL_CONTACTS=[]
		
		missing_values_PRE_binner_valueRange_SELF_INIT_CNTCTS=[]
		
		missing_values_PRE_binner_valueRange_SOLICITED_CNTCTS=[]
		
		missing_values_POST_binner_valueRange_TOTAL_CONTACTS=[]
		
		missing_values_POST_binner_valueRange_SELF_INIT_CNTCTS=[]
		
		missing_values_POST_binner_valueRange_SOLICITED_CNTCTS=[]
		
		missing_values_INV_binner_condition_TOTAL_CONTACTS=[]
		
		missing_values_INV_binner_condition_SELF_INIT_CNTCTS=[]
		
		missing_values_INV_binner_condition_SOLICITED_CNTCTS=[]
		
#-----------------New DataProcessing-----------------
		data_model_binner_in=pd.read_csv('../workflow_datasets/data_model_stringToNumber_in.csv')
		missing_values_PRE_binner_valueRange_TERRITORY=[]
		
		missing_values_POST_binner_valueRange_TERRITORY=[]
		
dp=DataProcessing()
dp.generateDataProcessing()
