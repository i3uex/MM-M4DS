import pandas as pd
import json
import h5py
import pyarrow
				
join_Name_with_City__input_dataDictionary=pd.read_csv('/pop/data/join_input_dataDictionary.csv', sep = ',')
join_Name_with_City__input_dataDictionary.to_parquet('/pop/data/join_input_dataDictionary.parquet')
