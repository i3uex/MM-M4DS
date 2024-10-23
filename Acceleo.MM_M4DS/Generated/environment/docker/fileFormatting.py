import pandas as pd
import json
import h5py
import pyarrow
from sqlalchemy import create_engine
import mysql.connector
import psycopg2

rowFilter_output_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.csv', sep = ',')
rowFilter_output_dataDictionary.to_parquet('/wf_validation_python/data/dataset1/rowFilter_output_dataDictionary.parquet')

columnFilter_output_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.csv', sep = ',')
columnFilter_output_dataDictionary.to_parquet('/wf_validation_python/data/dataset2/columnFilter_output_dataDictionary.parquet')

ruleEngine_territory_output_dataDictionary=pd.read_csv('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.csv', sep = ',')
ruleEngine_territory_output_dataDictionary.to_parquet('/wf_validation_python/data/dataset2/ruleEngine_territory_output_dataDictionary.parquet')

engine = create_engine('mysql+mysqlconnector://root:password@localhost/test_storage')
test_storage_missing_output_dataDictionary.csv = pd.read_sql('SELECT * FROM missing_output_dataDictionary.csv;', engine)
test_storage_missing_output_dataDictionary.csv.to_parquet('/wf_validation_python/data/db1/missing_output_dataDictionary.csv.parquet')

engine = create_engine('postgresql+psycopg2://root:pass@localhost/test_storage_postgre')
test_storage_postgre_missing_input_dataDictionary.csv = pd.read_sql('SELECT * FROM missing_input_dataDictionary.csv;', engine)
test_storage_postgre_missing_input_dataDictionary.csv.to_parquet('/wf_validation_python/data/db2/missing_input_dataDictionary.csv.parquet')

