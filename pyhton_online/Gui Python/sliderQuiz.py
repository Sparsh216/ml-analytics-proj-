from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x300")
root.title("slider Feedback")
def feed():
    with open("feed.txt","a") as f:
        f.write(f"Rating is {myslider1.get()}\n")
    tmsg.showinfo("FeedBack","Thank you for submitting the feed back")
Label(root,text="Coustomer Feedback Scale",fg="blue").pack()
myslider1=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=5)
Button(root,text="Submit",command=feed).pack()
myslider1.pack()
root.mainloop()