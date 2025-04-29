import pandas as pd
import json
import h5py
import pyarrow
				
mathOperation_Difference_in_Latitude_Altitude__input_dataDictionary=pd.read_csv('/home/data/mathOperation_input_dataDictionary.csv', sep = ',')
mathOperation_Difference_in_Latitude_Altitude__input_dataDictionary.to_parquet('/home/data/mathOperation_input_dataDictionary.parquet')
