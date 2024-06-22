import os, socket, tkinter as tk
from time import sleep
from icecream import ic
from tkinter import *
from tkinter import filedialog
from datetime import datetime
from icecream import ic
from PACKAGES.utils import *
from PACKAGES.url_verification import verify_urls


def app_root():
    """
    Returns the absolute path of the current working directory.
    """
    current_directory = os.getcwd()
    loc = os.path.abspath(current_directory)
    return loc


def int_path_check():
    """
    Initiates the internal URL verification process.
    """
    print('Internal verification script')
    check_window(verify_urls, 'internal')
    tk.mainloop()
    

def ext_path_check():
    """
    Initiates the external URL verification process.
    """
    print('External verification script')
    check_window(verify_urls, 'external')
    tk.mainloop()


def url_report():
    """
    Opens the generated URL verification report.
    """
    print('Open report script')
    file_check = f'{reports_location}app-report.xlsx'
    
    if os.path.exists(file_check):
        os.system(f'start excel "{file_check}"')
    else:
        click_file_error()
        click_file_error()


def repo_archive():
    print('Open report repository tool')
    file_path = filedialog.askopenfilename(initialdir=reports_location,
                                           title='Select a file to open',
                                           filetypes = (('All files', '*.*'),('text files', '*.txt')))
    if file_path == '':
        pass
    else:
        file = os.system(f'start excel "{file_path}"')


def files_folder():
    print('Open files location tool')
    file_path = filedialog.askopenfilename(initialdir=files_location,
                                           title='Select a file to open',
                                           filetypes = (('All files', '*.*'),('text files', '*.txt')))
    print(file_path)
    if file_path == '':
        pass
    else:
        file = os.system(f'start excel "{file_path}"')


def failed_checks():
    ic('Processing ailed urls')
    zone = 'internal'
    failed_browse(zone)


def list_url():
    print('Open source urls file - ema-prod-app.xlsx')
    file_path= f'{files_location}ema-prod-app.xlsx'
    if os.path.exists(file_path):
        os.system(f'start excel "{file_path}"')
    else:
        with open(file_path, "w") as file:
            file.write('LIST ALL URLS BELOW')
            os.system(f'start excel "{file_path}"')


def help_open():
    ic('Help not available yet')
    pass
    


def about_open():
    ic('About not available yet')
    pass


# ++++++ BEGIN +++++

print('#'*150)
print('# URL Verification automation tool - Begin!')
print('#'*150)
WIDTH = 600
HEIGHT = 500
my_location = ema_root()
files_location = f'{my_location}\\FILES\\'
packages_location = f'{my_location}\\PACKAGES\\'
reports_location = f'{my_location}\\REPORT\\'
current_date = datetime.now().strftime('%Y%m%d')

ic(current_date, my_location)

window = Tk()
canvas = Canvas(window, width= WIDTH, height=HEIGHT)
canvas.pack()
bar = Menu(window)
window.config(menu=bar)
window.title("EUROPEAN MEDICINES AGENCY")
win_icon = PhotoImage(file= files_location + 'z_ema.png')
window.iconphoto(True, win_icon)

label_text = Label(window,
                   font=('Times New Roman', 12),
                   text="\n     URL Verification Automation Tool     \n \nfor Windows\n"
                    "\n \n \n European Medicines Agency"
                    "\n 2023",
                   anchor=CENTER,
                   justify=CENTER,
                   relief=RAISED,
                   bd=1, padx=1, pady=1,
                   compound=TOP,
                   image=win_icon)
label_text.place(x=170, y=100)
menu_pic = PhotoImage(file= files_location + 'z_mario.png')

menu_app = Menu(bar, tearoff=0, font=('Georgia', 12))
bar.add_cascade(label='APPLICATIONS', menu=menu_app)
menu_app.add_command(label='Internal URL Check', command=int_path_check)
menu_app.add_command(label='External URL Check', command=ext_path_check)
menu_app.add_separator()
menu_app.add_command(label='Exit', command=quit, image=menu_pic, compound='left')

menu_open = Menu(bar, tearoff=0, font=('Georgia', 12))
bar.add_cascade(label='REPORTS', menu=menu_open)
#menu_open.add_command(label='DNS Lookup Report', command=open_dns)
menu_open.add_command(label='URL Check Report', command=url_report)
menu_open.add_separator()
menu_open.add_command(label='Reports Repository', command=repo_archive)
menu_open.add_command(label='Files Folder', command=files_folder)
menu_open.add_separator()
menu_open.add_command(label='Browse Failed URLs', command=failed_checks)

menu_list = Menu(bar, tearoff=0, font=('Georgia', 12))
bar.add_cascade(label='URL SOURCE LIST', menu=menu_list)
menu_list.add_command(label='Edit Source list', command=list_url)

menu_help = Menu(bar, tearoff=0, font=('Georgia', 12))
bar.add_cascade(label='HELP', menu=menu_help)
menu_help.add_command(label='Help', command=help_open)
menu_help.add_command(label='About', command=about_open)

window.mainloop()