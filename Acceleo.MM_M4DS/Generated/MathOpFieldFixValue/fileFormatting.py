import pandas as pd
import json
import h5py
import pyarrow
				
mapping_native-country__input_dataDictionary=pd.read_csv('esta/data/output/Rule_Engine_output_dataDictionary.csv', sep = ',')
mapping_native-country__input_dataDictionary.to_parquet('esta/data/output/Rule_Engine_output_dataDictionary.parquet')
