# SCRIPT TO VERIFY EXTERNAL URLS HTTPS STATUS CODE

import csv, os, requests, logging, sys
import pandas as pd
from icecream import ic
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse

options = Options()
options = webdriver.ChromeOptions()
options.headless = True
options.accept_insecure_certs = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 2)
response_timeout = 10
my_location = os.getcwd()
urls_file = f'{my_location}\\FILES\\aws-prod-app.csv'
urls_status = f'{my_location}\\FILES\\ext-verified-list.csv'
log_file_path = f'{my_location}\\FILES\\AppExtLogs.log'
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.basicConfig(filename=log_file_path, level=logging.CRITICAL)
sys.stdout = open(log_file_path, 'a')
sys.stderr = open(log_file_path, 'a')

url_list = []
results = []
pvt_ip = []
pub_ip = []

with open(urls_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        url_list.append(row[0])
        pvt_ip = row[3]
        pub_ip = row[4]

for url in url_list:
    if 'URL' in url:
        pass
    elif 'emea' in url:
        print(f'{url} is Internal domain')
        pass
    else:
        try:
            response = requests.get(url, timeout=response_timeout, verify=False)
            status_code = response.status_code
            print(f'{url} ({status_code})')
            driver.set_page_load_timeout(10)
            driver.get(url)
            parsed_url = urlparse(url)
            fqdn = parsed_url.netloc
            results.append([url, fqdn, status_code, pvt_ip, pub_ip])
            sleep(2)
        except Exception as e:
            status_code = '500'
            print('X'*100)
            print(f"Error processing {url}: {e}")
            print(f'{url} has an error, and responds with {status_code}')
            print('X'*100)
            results.append([url, url, status_code, pvt_ip, pub_ip])
driver.quit()

with open(urls_status, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['URL', 'FQDN', 'STATUS CODE', 'F5 PVT', 'F5 PUB'])
    csv_writer.writerows(results)
