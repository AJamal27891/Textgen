from tkinter import *
from tkinter import messagebox
import os
from PIL import  ImageTk, Image
from main import *
from tkinter import ttk
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as tkMessageBox
import tkinter.simpledialog as tkSimpleDialog
from tkinter.simpledialog import Dialog
#from InputsOptions import *
import mongoengine
import  datetime
from ModelOptions import *

Output_Option_frame = LabelFrame(root, text= ' Output ', relief=RIDGE,bg ='#708090',padx=5,pady=5,width=310*2+10, height=200*2,fg='#FFFAFA')

class outputdata(mongoengine.Document):
    data_version = mongoengine.FloatField(default = 1.0)
    entrydate = mongoengine.DateTimeField(default= datetime.datetime.now)
    id = mongoengine.ObjectIdField()
    text = mongoengine.StringField()
    model = mongoengine.StringField()

    meta = {
    'db_alias':'core',
    'collections':'outputdata'
    }

from Model.src.interactive_conditional_samples import interact_model

output_text = interact_model()
