# Python-Applications-for-URL-Automation
Python Applications

## ! Application Optimized for Windows Clients


# Repository with application to automate urls check

    - Current working Application: EMA.py (GUI) / v3.r1
    - PROD Application directory: appprod3


    - Application functions:

        1 - Check url availability and returns page status, http status code, and page title
        1 - Open in a browser tab all the urls identified as not available with status code >= 500
        4 - Generates an aggregated EXCEL report containing Internal and External tests
        5 - Option to edit urls list directly from the application ema-prod-app(.xlsx)
        6 - Log file



# Application files

### Required files:

    * aws-prod-app.xlsx
        Excel file with mandatory format and header containing list of urls to be verified.


### Output files

    Report stored under REPORT folder (appprod3/REPORT)

    * dns_results.xlsx (DEPRECIATED)
        DNS records is now added to the url file as current DNS record

    * app-report.xlsx
        Application report



# Installation Instructions

## Pre-requisites:

    - Python 3.11
    - pip (pip3)
    - Requeired libraries:
        . selenium
        . Pandas
        - Ice Cream
        

## Application package (app.zip)

    1. Unzip application package (appprod3.zip)
    2. Open folder to appprod3 
    3. Whithin the folder tool bar type cmd top open the command line
    4. Make sure that you are in application folder (appprod3)
    3. Execute the application with command: python3 ./EMA.py


## How to enable terminal logs

    Open and edit the following files in PACKAGES folder

        * int-path-check.py 
        * ext-path-check.py
    
    Comment with # the following line (27 by default)

        $ sys.stdout = open(log_file_path, 'a')
