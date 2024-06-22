# SCRIPT TO ADD PULSE SECURE PRIVATE IP TO EXCEL FILE
# NOT IN USE !!!

import os
import pandas as pd
from icecream import ic


my_location = os.getcwd()
report_location = f'{my_location}\\REPORT\\'
source_file = f'{report_location}PROD-EXT-REF-DNS.xlsx'
destination_file = f'{report_location}PROD-EXT-REF-APP-STATUS.xlsx'

source_column_name = 'IP'
destination_column_name = 'PS PRIVATE IP'
source_data = pd.read_excel(source_file)
ic(source_data)
data_to_copy = source_data[source_column_name]
destination_data = pd.read_excel(destination_file)
destination_data[destination_column_name] = data_to_copy
destination_data.to_excel(destination_file, index=False)

print(f'Data from column "{source_column_name}" in "{source_file}" '
      f'has been copied to column "{destination_column_name}" in "{destination_file}"')
