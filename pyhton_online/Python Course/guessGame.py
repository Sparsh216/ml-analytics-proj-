import random

def guess(a,b):
    i=random.randint(a,b)
    print("Computer has choosen the number its your time to guess it\nlets see how many guess you will take")
    try:
        choice=-1
        counter=1
        while (choice!=i):
            choice=int(input(f"Choose a number between {a} and {b}: "))
            if(choice<i):
                print("Oops!, wrong number. Greater number please ")
            elif(choice>i):
                print("Oops!, wrong number. Smaller number please ")
            counter=counter+1
        return counter
    except:
        print("Wrong input, Rerun the game")


print ('''***************************************\n
Welcome to the guess game, Lets play!!!\n
***************************************\n''')
print("Enter the range of number in which you want to play the game")
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of a: "))
print("\n\nIts player 1 turn.\n\n")
counter1=guess(a,b)
print(f"Player 1 guessed the correct number in {counter1} guesses.\n")
print("\n\nIts player 2 turn.\n\n")
counter2=guess(a,b)
print(f"Player 2 guessed the correct number in {counter2} guesses.\n")

if(counter1<counter2):
    print("\nCongrats Player 1, You are the winner.\n")
elif(counter1>counter2):
    print("\nCongrats Player 2, You are the winner.\n")
else:
    print("\nWoah, its a tie.\n")


