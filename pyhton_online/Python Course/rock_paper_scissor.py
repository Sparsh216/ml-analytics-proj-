import random
def playgame(user,comp):
    if(user==comp):
        return 3
    else:
        if(user==1 and comp==3):
            return 0
        elif(user==1 and comp==2):
            return 1
        if(user==2 and comp==3):
            return 0
        elif(user==2 and comp==1):
            return 1 
        if(user==3 and comp==1):
            return 0
        elif(user==3 and comp==2):
            return 1             


print("*****************************\n")
print("*****************************\n")
print("Lets play rock paper scissor \n")
print("*****************************\n")
print("*****************************\n")

user=int(input(" Choose (1) for Rock, (2) for paper, or (3) for scissor "))
comp=random.randint(1,3)

answer=playgame(user,comp)
if(answer==1):
    print("Congo you won\n")
elif(answer==0):
    print("Computer won\n")
else:
    print("Its a tie\n\n")
print("You chose ",user)  
print("Computer chose ",comp)  



