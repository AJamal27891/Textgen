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
import random
import mongoengine
import datetime
filename=''

class inputdata(mongoengine.Document):
    data_version = mongoengine.FloatField(1.0)
    entrydate = mongoengine.DateTimeField(default= datetime.datetime.now)
    id  = mongoengine.ObjectIdField()
    text = mongoengine.StringField(required=True)
    meta = {
    'db_alias':'core',
    'collections':'inputdata'
    }




def find_method():
    find_method.textbox = Entry(Input_Option_frame,width=30)
    # # if Methods_list.get(ANCHOR) == 'CSV Files':
    # #     filename  = askopenfilename(filetype=(("CSV Files","*.csv"),))
    # #     find_method.flabel = Label(Input_Option_frame,text=filename,wraplength=110)
    # #     find_method.flabel.place(x=100,y=10)
    # #     tv = ttk.Treeview(Preview_Option_frame)
    # #     tv.pack()
    # #     df = pd.read_csv(filename).to_numpy().tolist()
    # #     for r in df:
    # #         print(r)
    # #         try:
    # #             tv.insert("",END,r)
    # #         except :
    # #             pass
    # #     return Methods_list.get(ANCHOR), filename
    # elif Methods_list.get(ANCHOR) == 'Text Files':
    #     filename  = askopenfilename(filetype=(("CSV Files","*.csv"),))
    #     find_method.flabel = Label(Input_Option_frame,text=filename,wraplength=110)
    #     find_method.flabel.place(x=100,y=10)
    #     return Methods_list.get(ANCHOR), filename
    if Methods_list.get(ANCHOR) == 'Free Text':
        find_method.textbox.place(x=80,y=10)
        print('Free')
        return Methods_list.get(ANCHOR), find_method.textbox.get()
    elif Methods_list.get(ANCHOR) == 'Web':
        print('Web')

from Model.src.interactive_conditional_samples import interact_model
from OutputOptions import *
def sumbit():
    text = interact_model(texting=find_method.textbox.get(),nsamples=2,length=250, model_name='345M')
    return Label(Output_Option_frame,text=text,wraplength=500).place(x=10,y=10)



def clear():
    if Methods_list.get(ANCHOR) == 'CSV Files' or Methods_list.get(ANCHOR) == 'Text Files':
        f = find_method.flabel
    elif Methods_list.get(ANCHOR) == 'Free Text':
        f = find_method.textbox
    return f.destroy()
methods = ['CSV Files','Text Files','Free Text','Web']
Input_Option_frame = LabelFrame(root, text= ' Input Options ', relief=RIDGE,bg ='#708090',padx=5,pady=5,width=310, height=200,fg='#FFFAFA')
Preview_Option_frame = LabelFrame(root, text= ' Preview ', relief=RIDGE,bg ='#708090',padx=5,pady=5,width=400, height=200*3+10,fg='#FFFAFA')

Methods_list = Listbox(Input_Option_frame,width=10,bd=2)
Methods_list.config(height=len(methods))
Choose_Method_bt = Button(Input_Option_frame,text='Select',command = find_method,width=8)
Clear_Method_bt = Button(Input_Option_frame,text='Clear',command = clear,width=8)

sumbit_input = Button(Input_Option_frame,text='Submit',command= sumbit,bg='#89cd87',fg='white',font = ("Times New Roman", 10),highlightcolor='blue')
