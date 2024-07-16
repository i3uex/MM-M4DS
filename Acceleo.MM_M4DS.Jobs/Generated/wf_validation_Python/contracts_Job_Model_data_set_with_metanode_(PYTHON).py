import os

import pandas as pd
import numpy as np
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType
from helpers.logger import set_logger

def generateWorkflow():
#-----------------New DataProcessing-----------------
	job_imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')

	job_imputeMissingByMostFrequent(sex, IRISCHOOL, ETHNICITY)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	job_imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')

	job_imputeMissingByFixValue(ACADEMIC_INTEREST_2, ACADEMIC_INTEREST_1)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	job_imputeMissingByMean(avg_income, distance)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')

	job_imputeMissingByMean(avg_income, distance)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	job_imputeMissingByLinearInterpolation(satscore)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_input_dataDictionary.csv', sep = ',')

	job_imputeMissingByLinearInterpolation(satscore)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	job_rowFilterRange(init_span)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/missing_output_dataDictionary.csv', sep = ',')

	job_rowFilterRange(init_span)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')

	job_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/rowFilter_output_dataDictionary.csv', sep = ',')

	job_columnFilter(TRAVEL_INIT_CNTCTS, REFERRAL_CNCTS, telecq, interest, stuemail, CONTACT_CODE1)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')

	job_mapping(TERRITORY)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/columnFilter_output_dataDictionary.csv', sep = ',')

	job_mapping(TERRITORY)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')

	job_mapping(Instate)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/ruleEngine_territory_output_dataDictionary.csv', sep = ',')

	job_mapping(Instate)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')

	job_stringToNumber(TERRITORY, Instate)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/ruleEngine_instate_output_dataDictionary.csv', sep = ',')

	job_stringToNumber(TERRITORY, Instate)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')

	job_imputeOutlierByClosest(avg_income, distance, Instate)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/stringToNumber_output_dataDictionary.csv', sep = ',')

	job_imputeOutlierByClosest(avg_income, distance, Instate)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	job_binner(TOTAL_CONTACTS, SELF_INIT_CNTCTS, SOLICITED_CNTCTS)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	job_binner(TOTAL_CONTACTS, SELF_INIT_CNTCTS, SOLICITED_CNTCTS)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	job_binner(TERRITORY)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	job_binner(TERRITORY)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	job_binner(satscore)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	job_binner(satscore)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

	job_binner(avg_income)_input_dataDictionary=pd.read_csv('./python_dataDictionaries/numericOutliers_output_dataDictionary.csv', sep = ',')

	if os.path.exists('./python_dataDictionaries/numericBinner_output_dataDictionary.csv'):		#If the output DataDictionary exists, we store it
		job_binner(avg_income)_output_dataDictionary=pd.read_csv('./python_dataDictionaries/numericBinner_output_dataDictionary.csv', sep = ',')

set_logger("contracts")
generateWorkflow()
