import pandas as pd
import json
import h5py
import pyarrow
from sqlalchemy import create_engine
import mysql.connector

missing_output_dataDictionary=pd.read_csv('/wf_validation_python/data/missing_output_dataDictionary.csv', sep = ',')
missing_output_dataDictionary.to_parquet('/wf_validation_python/data/missing_output_dataDictionary.parquet')

engine = create_engine('mysql+mysqlconnector://root:password@localhost/test_storage')
test_storage_missing_input_dataDictionary = pd.read_sql('SELECT * FROM missing_input_dataDictionary;', engine)
test_storage_missing_input_dataDictionary.to_parquet('/wf_validation_python/data/missing_input_dataDictionary.parquet')

