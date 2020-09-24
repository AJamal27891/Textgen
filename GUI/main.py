from tkinter import *
import os
from PIL import  ImageTk, Image

root = Tk()
root.config(bg='white')
imagedir = os.listdir(r'icon/')
icon = [i for i in imagedir if i.endswith('.ico')][0]
iconedir= os.path.join(r'icon/'+icon)
