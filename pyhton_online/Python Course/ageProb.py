try:
    strage=(input("Enter your age or your birth year to check when you will be 100: "))
    age=int(strage)
    if(len(strage)==2 and age>0 and age<100):
        print("The year you will be hundread is: ",2020+(100-age))      
    elif(len(strage)==3 and age>100 ):
        print("You are already above 100")        
    elif(len(strage)==4 and age<2020):
        print("The year you will be hundread is: ",age+100)       
    elif(len(strage)==4 and age>2020 or len(strage)==3 and age<0):
        print("HAHA! Your are not born yet")
        exit()
    elif(len(strage)==4 and (2020-age)>150 or len(strage)==3 and age>150):
        print("You seem to be oldest person alive")
        exit()
    else:
        print("It does not seem to be a valid age or birth year")  
        exit()
except ValueError as e:
    print("Zokes on you, You should type a valid age")
    exit()
teller=input("Do you want to know your age at a purticular year? Type yes for it and no to exit: ")
if(teller =="yes"):
    print("Type the birth year and year in yyyy format")
    birye=int(input("Birth year: "))
    year=int(input("Year: "))
    print("Your age at this year will be",(year-birye))