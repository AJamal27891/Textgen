from tkinter import *
import os
from PIL import  ImageTk, Image
import  sys
sys.path.insert(0, r'GUI/')
sys.path.insert(0, r'Model/')
from GUI  import ModelOptions
from GUI  import main
from GUI import InputsOptions
from main import *
from ModelOptions import *
from InputsOptions import  *
from OutputOptions import *
from Preview import *

root.title('Text generator')
root.geometry("1080x650")

root.iconbitmap(iconedir)
statusbar.pack(side=BOTTOM,fill=X)

#Model frame

Model_Option_frame.place(x=10,y=10)
menue_label.place(x=5 , y= 10 )
Size_label.place(x=5,y=50)
Sampel_label.place(x=5,y=100)
model_option_menu.current(0)
model_option_menu.place(x=150,y=10)
SampelSize.set(250)
Select_Sampel_Size.place(x=150,y=50)
NumberOfSampels.set(1)
Select_number_sampels.place(x=150,y=100)
bt_ok.place(x=120,y=150)

# Input Frame
Input_Option_frame.place(x=330,y=10)
Methods_list.place(x=10,y=10)
for i in methods:
    Methods_list.insert(END,str(i))
Choose_Method_bt.place(x=10,y=85)
Clear_Method_bt.place(x=10,y=110)
sumbit_input.place(x=120,y=150)

#Preview input
Preview_Option_frame.place(x=650,y=10)
# output Frame
Output_Option_frame.place(x=10,y=220)


root.mainloop()
