from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) +" - Notepad")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))

def exitFile():
    root.destroy()

def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")

def help():
    showinfo("Notepad","Notepad by Sparsh Bamrara")

if __name__== '__main__':
    root=Tk()
    root.title("Notepad")
    root.geometry("733x646")

    textarea=Text(root,font="calibary 12")
    file=None   
    textarea.pack(expand=True,fill=BOTH)


    #creating a menubar
    menbar=Menu(root,tearoff=0)

    #Addition of file menu in the menu bar
    filemenu=Menu(menbar,tearoff=0)
    filemenu.add_command(label="New",command=newFile)
    filemenu.add_command(label="Open",command=openFile)
    filemenu.add_command(label="Save",command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=exitFile)
    menbar.add_cascade(label="File",menu=filemenu)

    #Addition of edit menu in the menu bar
    editmenu=Menu(menbar,tearoff=0)
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    filemenu.add_separator()
    menbar.add_cascade(label="Edit",menu=editmenu)

    #Addition of help menu in the menu bar
    helpmenu=Menu(menbar,tearoff=0)
    helpmenu.add_command(label="About",command=help)
    menbar.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=menbar)#showing the menu by this command


    #Adding scroll Bar(Y)
    scroll1=Scrollbar(textarea)
    scroll1.pack(side=RIGHT,fill=Y)
    scroll1.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll1.set)

    root.mainloop()