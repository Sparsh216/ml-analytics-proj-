from tkinter import * 
def getval():
    print("Got the details")
root=Tk()
root.geometry("200x150")
Label(root,text="Submit form",fg="Black",font="Calibari 10 bold").grid(row=0,column=3)
username=Label(root,text="Username: ").grid(row=1,column=2)
password=Label(root,text="Password: ").grid(row=2,column=2)
user_value=StringVar()
pass_value=StringVar()
user_entry=Entry(root,textvariable=user_value)
pass_entry=Entry(root,textvariable=pass_value)
user_entry.grid(row=1,column=3)
pass_entry.grid(row=2,column=3)

Button(text="Submit Details",command=getval).grid(row=3,column=3)


root.mainloop()