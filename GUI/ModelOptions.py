from tkinter import *
from tkinter import messagebox
import os
from PIL import  ImageTk, Image
from main import *
from tkinter import ttk


def mop():
    model = ModelSize.get()
    sampel_size = Select_Sampel_Size.get()
    n_samples= Select_number_sampels.get()
    response = messagebox.askokcancel(title='Model attributes',message='model size : {}\n Sample size : {} \n Number of sampels: {}'.format(model,sampel_size,n_samples))
    print(response)




Model_Option_frame = LabelFrame(root, text= ' Model Options ', relief=SUNKEN,bg ='#a0d2eb',padx=5,pady=5,width=310, height=200)
ModelSize = StringVar(Model_Option_frame)
SampelSize = IntVar(Model_Option_frame)
NumberOfSampels = IntVar(Model_Option_frame)

menue_label  = ttk.Label(Model_Option_frame, text = "Select Model :",font = ("Times New Roman", 10),background='white')
Size_label  = ttk.Label(Model_Option_frame, text = "Enter text size :",font = ("Times New Roman", 10),background='white')
Sampel_label  = ttk.Label(Model_Option_frame, text = "Enter sampel number :",font = ("Times New Roman", 10),background='white')


model_option_menu = ttk.Combobox(Model_Option_frame,  textvariable = ModelSize)
model_option_menu['values'] = ('Small generator','Medium generator','Large generator','Extra large generator')
bt_ok = Button(Model_Option_frame,text='Submit',command= mop,bg='green',fg='white',font = ("Times New Roman", 10),highlightcolor='blue')
Select_Sampel_Size = Entry(Model_Option_frame,text='Sampel size')
Select_number_sampels = Entry(Model_Option_frame,text='number of samples')
