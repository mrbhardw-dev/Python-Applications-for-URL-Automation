# FUNCTION TO GENERATE PULSE SECURE DNS RECORD BEFORE MIGRATION

try:
    import os, csv, socket, time
    from fn_message import *
    from tqdm import tqdm
except Exception as err:
    print('Problem importing {err} library')


def pulse_secure():
    def dns_lookup(url):
        try:
            ip_address = socket.gethostbyname(url)
            return ip_address
        except socket.gaierror:
            return "No DNS Record"
            
    my_dir = os.getcwd()
    input_file = f'{my_dir}\\FILES\\ema-prod-app.csv'
    output_file = f'{my_dir}\\FILES\\ema-pulse-results.csv'

    with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(['IP', 'URL'])         
        for row in csv_reader:
            url = row[1]
            ip_address = dns_lookup(url)
            if 'FQDN' in url:
                pass
            else:
                csv_writer.writerow([f'{ip_address}', f'{url}',])
                    