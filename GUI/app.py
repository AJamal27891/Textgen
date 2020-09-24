from tkinter import *
import os
from PIL import  ImageTk, Image
from ModelOptions import *
from main import *
from InputsOptions import *

root.title('Text generator')
root.geometry("1080x750")

root.iconbitmap(iconedir)


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
Choose_Method_bt.place(x=10,y=80)
Clear_Method_bt.place(x=10,y=100)
sumbit_input.place(x=120,y=150)





root.mainloop()
