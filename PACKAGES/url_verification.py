import os
from datetime import datetime
from .utils import *
from .fn_excelToCsv import convert_to_csv
from .fn_failedUrl import failed_browse
from .fn_dnsClean import dns_clean
from .fn_LookupDns import lookup_dns
from .fn_urlconvert import url_convert
from .fn_adjust import format_report


def verify_urls(zone):
    """
    Orchestrates the URL verification process for the specified zone (internal or external).
    
    Args:
        zone (str): The zone to verify URLs for ('internal' or 'external').
        
    Raises:
        ValueError: If an invalid zone is provided.
    """
    if zone not in ['internal', 'external']:
        raise ValueError(f"Invalid zone: {zone}. Valid zones are 'internal' and 'external'.")
    
    convert_to_csv()
    try:
        file_path = f'{packages_location}{zone}-path-check.py'
        if os.path.exists(file_path):
            with open(file_path, "r") as script_file:
                url_code = script_file.read()
                exec(url_code)
        else:
            err_file(f'{zone}-path-check.py', packages_location)
        
        lookup_dns(zone)
        dns_clean(zone)
        url_convert(zone)
        format_report()
        generate_report()
    except Exception as err:
        error(err)
        ic(err)
