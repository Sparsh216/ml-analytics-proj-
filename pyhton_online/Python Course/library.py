from os import remove


class Library:
    books=[]
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    
    def availableBooks(self):
        for i,books in enumerate(self.books):
            print((i+1),"\t",books)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please handle it safely and return it on time")
            self.books.remove(bookName) 
            return True
        else:
            print("Sorry this book is either not available or have been issued to someone else. Please wait until the book is returened")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed reading it ")

           
class Student:
    StudentDict={}
    def __init__(self,nameList):
        self.StudentDict=nameList

    def studentDetail(self,name):
        if name in self.StudentDict:
            print("History books issued to you are: ", self.StudentDict[name])
            return True
        else :
            print("No such student found")
            return False

    def reqBook(self):
        self.book=input("Enter the name of the book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book=input("Enter the name of the book you want to return or donate: ")
        return self.book


if __name__ == "__main__":
    LibraryBooks=Library(["Python","Machine Learning","Web Devlopement","Game Developement"])
    Studict={"Sparsh":[],"Sumoksh":[],"Yash":[],"Abhishek":[]}
    StudentName=Student(Studict)
    print(" *****Welcome To The Library***** ")
    # LibraryBooks.availableBooks()
    # StudentName.studentDetail("SHruti")
    custName=""
    customer=0
    while True:
        print("Press 1 if you are an old customer \nPress 2 if you are want to add your name\nPress 3 to exit")
        customer=int(input("Enter your choice: "))
        if customer == 1:
            custName=input("Enter your name: ")
            det=StudentName.studentDetail(custName)
            if det==True:
                break
        elif customer == 2:
            custName=input("Enter your name: ")
            Studict.update({custName:[]})
            break
        elif customer == 3:
            exit()
        else:
            print("Oops!, wrong choice")

    while True:
        print("Enter 1 to see the available books")
        print("Enter 2 borrow books")
        print("Enter 3 to return/donate books")
        print("Enter 4 to exit")
        a=int(input("Enter your choice: "))
        if a == 1:
            LibraryBooks.availableBooks()
        elif a == 2:
            bk=StudentName.reqBook()
            val=LibraryBooks.borrowBook(bk)
            if val==True:
                Studict[custName].append(bk)
            elif val==False:
                break
        elif a == 3:
            bk=StudentName.returnBook()
            LibraryBooks.returnBook(bk)

        elif a == 4:
            print("Thanks for comming to our library, Have a nice day")
            exit()
        else:
            print("Oops!, wrong choice")
