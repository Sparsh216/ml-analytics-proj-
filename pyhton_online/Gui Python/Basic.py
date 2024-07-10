from tkinter import *
from PIL import Image , ImageTk
import os
root=Tk()

root.geometry('733x434')
root.minsize(733,434)
root.maxsize(733,434)
lis=os.listdir()
for item in lis:
    if item.endswith(".JPG"):
        image=Image.open(item)
        photo=ImageTk.PhotoImage(image)
        lab=Label(text="Welcome to the first pyscreen",image=photo).pack()

root.mainloop()