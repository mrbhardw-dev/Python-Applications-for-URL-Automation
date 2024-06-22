# SCRPT TO CONVERT CSV TO EXCEL AND ADD NEW SHEET TO REPORT

import os, pandas as pd
from datetime import datetime
from .fn_message import click_file_error


def url_convert(local):
    
    my_location = os.getcwd()
    files_location = f'{my_location}\\FILES\\'
    reports_location = f'{my_location}\\REPORT\\'
    current_date = datetime.now().strftime('%Y.%m.%d')
    excel_file = f'{reports_location}app-report.xlsx'
    
    print(f'Convert csv to excel and add new sheet to report in {local} zone')
    
    if local == 'internal':
        csv_file = f'{files_location}int-verified-list.csv'
        sheet_name = f'INT-{current_date}'
    elif local == 'external':
        csv_file = f'{files_location}ext-verified-list.csv'
        sheet_name = f'EXT-{current_date}'
    else:
        click_file_error()
        
    excel_data = pd.read_excel(excel_file)
    #excel_data.to_csv(csv_file, index=False)
    df = pd.read_csv(csv_file)
    with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
    print("Excel to CSV conversion, sheet addition, and Excel conversion completed.")
    
if __name__ == '__main__':
    local = 'internal'
    url_convert(local)
    

    

