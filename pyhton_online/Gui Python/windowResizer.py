from tkinter import *
def resize():
    width_value = wid.get()
    height_value = hei.get()
    root.geometry(f"{width_value}x{height_value}")

root=Tk()
screen_width=600
screen_height=400
root.geometry(f"{screen_width}x{screen_height}")
f0=Frame(root, width=400,height=30)
Label(f0,text="Window Resizer",font="calibari 30 bold").grid()
f0.grid(row=0,column=1)
f1=Frame(root, width=400,height=50)
Label(f1,text="Enter the width of window you want: ",fg="green").grid(row=2,column=0)
f1.grid(row=2,column=0)
wid=IntVar()
wid_entry=Entry(root,textvariable=wid).grid(row=2,column=1)
f2=Frame(root, width=400,height=600)
Label(f2,text="Enter the height of window you want: ",fg="green").grid(row=0,column=0)
f2.grid(row=3,column=0)
hei=IntVar()
hei_entry=Entry(root,textvariable=hei).grid(row=3,column=1)
Button(text="Apply", command=resize, pady=2, font="comicsansms 11").grid(column=1)


root.mainloop()

