import pandas as pd
import json
import h5py
import pyarrow
				
mathOperationFieldField_Difference_in_Latitude_Altitude__input_dataDictionary=pd.read_csv('ruta/data/output/CSV_Reader_output_dataDictionary.csv', sep = ',')
mathOperationFieldField_Difference_in_Latitude_Altitude__input_dataDictionary.to_parquet('ruta/data/output/CSV_Reader_output_dataDictionary.parquet')
