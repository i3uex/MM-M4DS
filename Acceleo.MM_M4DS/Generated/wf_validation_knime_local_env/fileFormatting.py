import pandas as pd
import json
import h5py
import pyarrow
from sqlalchemy import create_engine
import mysql.connector

engine = create_engine('mysql+mysqlconnector://root:password@localhost/test_storage')
test_storage_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary = pd.read_sql('SELECT * FROM missing_input_dataDictionary;', engine)
test_storage_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__input_dataDictionary.to_parquet('/wf_validation_python/data/db_mysql/missing_input_dataDictionary.parquet')

test_storage_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary = pd.read_sql('SELECT * FROM missing_output_dataDictionary;', engine)
test_storage_imputeMissingByMostFrequent_sex_IRISCHOOL_ETHNICITY__output_dataDictionary.to_parquet('/wf_validation_python/data/db_mysql/missing_output_dataDictionary.parquet')

test_storage_imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary = pd.read_sql('SELECT * FROM missing_output_dataDictionary;', engine)
test_storage_imputeMissingByFixValue_ACADEMIC_INTEREST_2_ACADEMIC_INTEREST_1__input_dataDictionary.to_parquet('/wf_validation_python/data/db_mysql/missing_output_dataDictionary.parquet')

rowFilterRange_init_span__output_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.csv', sep = ',')
rowFilterRange_init_span__output_dataDictionary.to_parquet('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.parquet')

columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField=pd.read_csv('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.csv', sep = ',')
columnFilter_TRAVEL_INIT_CNTCTS_REFERRAL_CNCTS_telecq_interest_stuemail_CONTACT_CODE1__input_dataField.to_parquet('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.parquet')

data_model_column_cont_filter_out=pd.read_csv('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.csv', sep = ',')
data_model_column_cont_filter_out.to_parquet('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.parquet')

Mapping_TERRITORY__input_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.csv', sep = ',')
Mapping_TERRITORY__input_dataDictionary.to_parquet('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.parquet')

Mapping_TERRITORY__output_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.csv', sep = ',')
Mapping_TERRITORY__output_dataDictionary.to_parquet('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.parquet')

mapping_Instate__input_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.csv', sep = ',')
mapping_Instate__input_dataDictionary.to_parquet('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.parquet')

