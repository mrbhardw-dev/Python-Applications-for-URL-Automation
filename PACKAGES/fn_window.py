# INFORMATION / CONFIRMATION WINDOW

import os
import tkinter as tk
from tkinter import *

def check_window(callback):
    print('New Window callback function')
    new_window = tk.Toplevel()
    new_window.title("URL Verification tool")
    new_window.geometry('650x600+300+200')
    
    label = tk.Label(new_window, 
                     font=('Bookman Old Style', 12,),
                     anchor=CENTER,
                     justify=CENTER,
                     bd=1, padx=1, pady=1,
                     text=
                     "\n\n\nDepending on the number of urls to verify, the script may take\n some time to complete (15+ minutes), so be patient!\n\n"
                     "When performing some background tasks, the application may appear frozen,\n though that is not the case. You can follow"
                     " the progress in the terminal\n\n\nThe following tasks will be performed:\n\n"
                     "  Open and verify all URLs using WebDriver\n Collect URL status and additional information\n"
                     "  A DNS lookup to verify the current APP DNS record.\n Convert CSV report to EXCEL format\n"
                     "  Format EXCEL report\n\n\n")
    label.pack()
    close_button = tk.Button(new_window, text="Proceed", command=lambda: [new_window.destroy(), callback()])
    close_button.pack()