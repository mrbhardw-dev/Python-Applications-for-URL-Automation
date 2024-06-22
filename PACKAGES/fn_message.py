# FUNCTION TO GENERATE MESSAGE WINDOWS

from tkinter import messagebox


def click_file_error():
    infobox = messagebox.showwarning(title='ERROR', message='File does not exist')


def error(err):
    infobox = messagebox.showerror(title='Application Error', 
                                   message='This application encountered an execution erro \n{err}')
    

def dns_error():
    infobox = messagebox.showwarning(title='DNS FILE NOT CREATED', message='Please run first a DNS lookup in Applications menu / DNS Lookup')
    

def fqdn_check():
    infobox = messagebox.showerror(title='MISSING CSV FILE', message='List of FQDN does not exist, run first the URL PATH CHECK option')
    

def generate_report():
    infobox = messagebox.showinfo(title='REPORT GENERATED SUCCESSFULLY', message='All checks completed. Report has been generated\n'
                                  'Open it through the Reports menu')
    

def err_file(f_name, f_path):
    infobox = messagebox.showerror(title='ERROR OPENING FILE', 
                                   message=f'\nCan not find {f_name} \nVerify if file exists in {f_path}')


def selection_box():
    infobox = messagebox.showinfo(title='NO SELECTION DETECTED', message='Please select one of the zones!', icon='info')

