import os
from .fn_message import *


def dns_clean(local):
    
    my_dir = os.getcwd()
    
    if local == 'internal':
        f_del = f'{my_dir}\\FILES\\int-verified-list.csv'
        local = 'internal'
    elif local == 'external':
        f_del = f'{my_dir}\\FILES\\ext-verified-list.csv'
        local = 'external'
    else:
        click_file_error()
        return
    
    
    f_ren = f'{my_dir}\\FILES\\dns-results.csv'

    if os.path.exists(f_del):
        os.remove(f_del)
        print(f"File '{f_del}' has been deleted.")
    else:
        print(f"File '{f_del}' does not exist and cannot be deleted.")

    if os.path.exists(f_ren):
        os.rename(f_ren, f_del)
        print(f"File '{f_ren}' has been renamed to '{f_del}'.")
    else:
        print(f"File '{f_ren}' does not exist and cannot be renamed.")
