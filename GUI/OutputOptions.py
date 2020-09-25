from tkinter import *
from tkinter import messagebox
import os
from PIL import  ImageTk, Image
from main import *
from tkinter import ttk
import pandas as pd
try:
    import Tkinter as tk
    import ttk
    from tkFileDialog import askopenfilename
    import tkMessageBox
    import tkSimpleDialog
    from tkSimpleDialog import Dialog
except ModuleNotFoundError:   # Python 3
    import tkinter as tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
    import tkinter.messagebox as tkMessageBox
    import tkinter.simpledialog as tkSimpleDialog
    from tkinter.simpledialog import Dialog

Output_Option_frame = LabelFrame(root, text= ' Output ', relief=RIDGE,bg ='#708090',padx=5,pady=5,width=310*2+10, height=200*2,fg='#FFFAFA')
