import pandas as pd
import json
import h5py
import pyarrow

missing_input_dataDictionary=pd.read_csv('/wf_validation_python/data/missing_input_dataDictionary.csv', sep = ',')
missing_input_dataDictionary.to_parquet('/wf_validation_python/data/missing_input_dataDictionary.parquet')

missing_output_dataDictionary=pd.read_csv('/wf_validation_python/data/missing_output_dataDictionary.csv', sep = ',')
missing_output_dataDictionary.to_parquet('/wf_validation_python/data/missing_output_dataDictionary.parquet')

