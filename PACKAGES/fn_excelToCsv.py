# SCRIPT TO CONVERT EXCEL TO CSV

try:
    import os
    import pandas as pd
    from icecream import ic
except Exception as err:
    ic(err)


def convert_to_csv():
    my_dir = os.getcwd()
    in_excel = f'{my_dir}\\FILES\\ema-prod-app.xlsx'
    out_csv = f'{my_dir}\\FILES\\ema-prod-app.csv'
    data = pd.read_excel(in_excel)
    data.to_csv(out_csv, index=False)
    ic(f'Excel file "{in_excel}" has been converted to CSV file "{out_csv}"')