from tkinter import *

root=Tk()
root.geometry("768x234")
f=Frame(root, borderwidth=6, bg="red", relief=SUNKEN)
f.pack(side=LEFT)
b1=Button(text="button 1",fg="green",bd=4)
b1.pack(side=BOTTOM,anchor="sw")
b2=Button(text="button 2")
b2.pack(side=BOTTOM)
b3=Button(text="button 3")
b3.pack(side=BOTTOM)
b4=Button( text="button 4",bd=4)
b4.pack(side=BOTTOM)

root.mainloop()