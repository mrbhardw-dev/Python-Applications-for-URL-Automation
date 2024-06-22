import os
import csv
import socket
from urllib.parse import urlparse, urlunparse
from .fn_message import *
from tqdm import tqdm

def lookup_dns(local):
    
    def dns_lookup(url):
        if ':' in url:
            parsed_url = urlparse(url)
            print(parsed_url)
            url = parsed_url.netloc.split(':')[0]
            print(url)
            print('Looking for', '>'*5, url)
        else:
            pass
        try:
            ip_address = socket.gethostbyname(url)
            return ip_address
        except socket.gaierror:
            return "No DNS Record"

    my_dir = os.getcwd()
    output_file = os.path.join(my_dir, 'FILES', 'dns-results.csv')
    if local == 'internal':
        input_file = os.path.join(my_dir, 'FILES', 'int-verified-list.csv')
    elif local == 'external':
        input_file = os.path.join(my_dir, 'FILES', 'ext-verified-list.csv')
    else:
        click_file_error()

    with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv:
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames + ['CURRENT IP']
        csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in csv_reader:
            url = row['FQDN']
            ip_address = dns_lookup(url)
            row['CURRENT IP'] = ip_address
            csv_writer.writerow(row)