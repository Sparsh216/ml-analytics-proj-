from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("My Calculator")
root.configure(background="turquoise")
scval=StringVar()
scval.set("")
screen=Entry(root,textvar=scval,font="lucida 40 bold")
screen.pack(fill=X,pady=8,padx=5)
lis1=[9,8,7,6,5,4,3,2,1,0,00,"."]
lis2=["+","-","*","/","%","C","AC","="]
k=0
for j in range (int(len(lis1)/3+1)):
    f=Frame(root,bg="beige")
    for i in range(0,3):
        if k==len(lis1):
            break
        if lis1[k]==".":
            b=Button(f,text=lis1[k],padx=8,pady=8,font="lucida 23 bold",relief=SUNKEN)
            b.pack(side=LEFT,padx=10,pady=8)
            k=k+1
        else:
            b=Button(f,text=lis1[k],padx=8,pady=8,font="lucida 20 bold",relief=SUNKEN)
            b.pack(side=LEFT,padx=8,pady=8)
            k+=1
    f.pack(anchor="w",padx=5)
k=0
for j in range (int(len(lis2)/2)):
    f1=Frame(root,bg="beige")
    for i in range(0,2):
        if k==len(lis2):
            break
        else:
            b=Button(f,text=lis2[k],padx=8,pady=8,font="lucida 20 bold",relief=SUNKEN)
            b.pack(side=RIGHT,padx=8,pady=8)
            k+=1
    f1.pack(anchor="ne",padx=5,side=RIGHT)
root.mainloop()