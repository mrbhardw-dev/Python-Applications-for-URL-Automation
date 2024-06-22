# SCRIPT TO REMOVE DUPLICATES FROM A FILE

import pandas as pd

def extract_duplicates(in_file, out_file):
    try:
        df = pd.read_csv(in_file)

        df_no_duplicates = df.drop_duplicates()
        df_no_duplicates.to_csv(out_file, index=False)

        print("Duplicates removed and data saved to", out_file)
    except Exception as e:
        print("Error:", str(e))


if __name__ == '__main__':

    extract_duplicates('urls-temp.csv', 'urls-.csv')