# SCRIPT TO OPEN IN A BROWSER ALL URLS WITH ERROR STATUS CODE

try:
     import csv, os, webbrowser
     from tkinter import messagebox
     from icecream import ic
     #from .fn_message import click_file_error
except Exception as err:
     ic(err)


def failed_browse(zone):
     my_location = os.getcwd()
     failover = ''
     print(my_location)
     ic('Start open in a browser all urls with status code > 499 for zone', zone)
     
     if zone == 'internal':
          failover = f'{my_location}\\FILES\\int-verified-list.csv'
          print(failover)
     elif zone == 'external':
          failover = f'{my_location}\\FILES\\ext-verified-list.csv'
          ic(failover)
     else:
          print('MISSING ZONE')
          #click_file_error()
          exit()

     try:   
          with open(failover, 'r') as csv_file:
               failed = csv.DictReader(csv_file)
               for st in failed:
                    status = int(st['STATUS CODE'])
                    page = st['URL']
                    if page == "URL":
                         pass
                    elif status >= 500:
                         print(f'Opening >>> {page} / {status}')
                         webbrowser.open(page)
                    else:
                         pass

     except Exception as err:
          ic(err)
          #click_file_error()
          
if __name__ == '__main__':
     failed_browse('internal')

