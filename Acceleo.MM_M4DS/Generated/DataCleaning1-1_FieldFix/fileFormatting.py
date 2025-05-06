import pandas as pd
import json
import h5py
import pyarrow
				
mapping_native_country__input_dataDictionary=pd.read_csv('home/data/binner_output_dataDictionary.csv', sep = ',')
mapping_native_country__input_dataDictionary.to_parquet('home/data/binner_output_dataDictionary.parquet')
