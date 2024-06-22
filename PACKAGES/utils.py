import os
from tkinter import messagebox


def click_file_error():
    messagebox.showwarning(title='ERROR', message='File does not exist')


def error(err):
    messagebox.showerror(title='Application Error', 
                         message=f'This application encountered an execution error:\n{err}')
    

def dns_error():
    messagebox.showwarning(title='DNS FILE NOT CREATED', message='Please run a DNS lookup first from the Applications menu')
    

def fqdn_check():
    messagebox.showerror(title='MISSING CSV FILE', message='List of URLs does not exist, run the URL PATH CHECK option first')
    

def generate_report():
    messagebox.showinfo(title='REPORT GENERATED SUCCESSFULLY', message='All checks completed. Report has been generated\n'
                                                                      'Open it through the Reports menu')
    

def err_file(f_name, f_path):
    messagebox.showerror(title='ERROR OPENING FILE', 
                         message=f'\nCannot find {f_name} \nVerify if the file exists in {f_path}')


def selection_box():
    messagebox.showinfo(title='NO SELECTION DETECTED', message='Please select one of the zones!', icon='info')


def app_root():
    current_directory = os.getcwd()
    loc = os.path.abspath(current_directory)
    return loc
