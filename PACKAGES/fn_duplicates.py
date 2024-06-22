# SCRIPT TO REMOVE DUPLICATES FROM A FILE

import os, csv
import pandas as pd


def extract_duplicates(zone):
    
    my_dir = os.getcwd()
        
    if zone == 'internal':
        in_file = f'{my_dir}\\FILES\\fqdn-private-dns.csv'
        out_file = f'{my_dir}\\FILES\\fqdn-int-dns.csv'
        excel_file = f'{my_dir}\\REPORT\\fqdn-private-dns.xlsx'
    elif zone == 'external':
        in_file = f'{my_dir}\\FILES\\fqdn-public-dns.csv'
        out_file = f'{my_dir}\\FILES\\fqdn-public-dns.csv'
        excel_file = f'{my_dir}\\REPORT\\fqdn-ext-dns.xlsx'

    try:
        df = pd.read_csv(in_file)

        df_no_duplicates = df.drop_duplicates()
        df_no_duplicates.to_csv(out_file, index=False)

        print("Duplicates removed and data saved to", out_file)
    except Exception as e:
        print("Error:", str(e))
    
    try:
        sheet_name = 'DNS RECORDS'
        df = pd.read_csv(out_file)
        
        df.to_excel(excel_file, sheet_name=sheet_name, index=False)
        
        print(f"CSV file '{out_file}' converted to Excel file '{excel_file}' in sheet '{sheet_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")



def dns_normalization(zone):
    
    my_dir = os.getcwd()
    in_file = f'{my_dir}\\FILES\\dns-results.csv'
    if zone == 'internal':
        out_file = f'{my_dir}\\FILES\\fqdn-private-dns.csv'
    elif zone == 'external':
        out_file == f'{my_dir}\\FILES\\fqdn-public-dns.csv'
        
    columns_to_extract = ["FQDN", "CURRENT IP"]

    with open(in_file, 'r', newline='') as input_csv:
        csv_reader = csv.DictReader(input_csv)
        with open(out_file, 'w', newline='') as output_csv:
            fieldnames = columns_to_extract
            csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in csv_reader:
                extracted_data = {column: row[column] for column in columns_to_extract}
                csv_writer.writerow(extracted_data)