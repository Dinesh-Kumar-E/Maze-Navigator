import tkinter as tk
from tkinter.filedialog import askopenfilename

def get_path():
    
    '''This function opens a file explorer window to select any particular file
    form the directory which should be uploaded to git.
    The necessary functions below are used to extract the exact path of the directory
    arguments:  -> None
    returns :   -> Folder path of the dir to be uploaded to git'''
    
    tk.Tk().withdraw()

    loc = askopenfilename()

    print("Path : ",loc,"\n")
    
    return loc