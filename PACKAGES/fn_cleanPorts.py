# FUNCTION TO REMOVE PORTS FROM URL

import csv, os
from urllib.parse import urlparse, urlunparse


def clean_ports():

    def remove_ports_from_url(url):
        parsed_url = urlparse(url)
        cleaned_url = urlunparse((parsed_url.scheme, parsed_url.netloc.split(':')[0], parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
        return cleaned_url

    my_dir = os.getcwd()
    input_file = f'{my_dir}dns-results.csv'
    output_file = f'{my_dir}fmt-dns-results.csv'
    url_column = 'URL'

    with open(input_file, 'r') as input_file, open(output_file, 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            url = row[url_column]
            cleaned_url = remove_ports_from_url(url)
            row[url_column] = cleaned_url
            writer.writerow(row)

    print(f'Ports removed and saved to {output_file}')
