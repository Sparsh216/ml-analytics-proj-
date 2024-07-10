from tkinter import *
import random
from timeit import default_timer 
import difflib

root=Tk()
root.title('Typing test')
root.geometry("700x500")
root.resizable(height=FALSE,width=FALSE)
root.configure(background="grey70")
start=0
sentence=["Sarah and Ira drove to the store.",
"Jenny and I opened all the gifts.",
"The cat and dog ate.",
"My parents and I went to a movie.",
"Mrs. Juarez and Mr. Smith are dancing gracefully.",
"Samantha, Elizabeth, and Joan are on the committee.",
"The ham, green beans, mashed potatoes, and corn are gluten-free.",
"The paper and pencil sat idle on the desk."]
sent=random.choice(sentence)

Label(root,text="Lets check your typing speed",font="arial 20 bold",relief=SUNKEN,bd=10,fg="grey10",bg="lightpink").pack(side=TOP,anchor=N,pady=5)

Label(root,text="Your text is : ",font="arial 15 bold",anchor=NW,bg="beige",bd=5).pack(pady=10)

Label(root,text=sent,font="arial 8 bold",bd=10,bg="beige").pack()

Label(root,text="Type here ",font="arial 12 bold",bd=5,bg="beige").pack(pady=10)

textarea=Text(root,font="calibary 12",height=5,width=60,bg="white")
textarea.pack(pady=10) 

def play():
    global start
    start=default_timer()
    print(start)

def check():
    global start
    print(start)
    print(sent)
    entered=textarea.get(1.0,END)
    print(entered)
    end=  default_timer()
    time= round(end-start,2)
    speed=round(len(sent.split())*60/time,2)
    if entered==sent:
        Msg1 ="Time= " + str(time) + ' seconds'
        Msg2=" Accuracy= 100% "
        Msg3= " Speed= " + str(speed) + 'wpm' 
    else:
        accuracy=difflib.SequenceMatcher(None,sent,entered).ratio()
        accuracy=str(round(accuracy*100,2))
        Msg1 ="Time= "+ str(time) + ' seconds'
        Msg2=" Accuracy= " + accuracy + '%'
        Msg3= " Speed= " + str(speed) + ' wpm' #words per minute 
    Label(root, font = ('arial', 8, 'bold'), text = Msg1).pack()
 
    Label(root, font = ('arial', 8, 'bold'), text = Msg2).pack()
 
    Label(root, font = ('arial', 8, 'bold'), text = Msg3).pack()

Label(root,text="Click on start typing when ready\n and click on check when done.",font="arial 10 bold",bg="beige").pack(pady=10)

btn=Button(root,text="Start Typing",font="calibary 8 bold",relief=SUNKEN,bg="Dodgerblue",command=play,bd=5).pack(side=LEFT,ipadx=100,padx=5)
entered=play()
btn=Button(root,text="Check",font="calibary 8 bold",relief=SUNKEN,bg="Dodgerblue",command=check,bd=5).pack(side=RIGHT,ipadx=100,padx=5)

root.mainloop()