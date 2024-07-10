import random
n=int(input("Enter the number of friends who names you want to swap: "))
names=[input(f"Enter the name of friend {i+1}: ") for i in range(n)]
# names=["Sansi kabutar","Pand Dlsna","Lakahn Chaurasiya","Hig pig"]
print(names)

print("The jumbled names are ")

for i in range(n):
    rand=random.randint(0,n-1)
    name1=names[i-1].split()
    name2=names[rand].split()
    print(name1[0]," ",name2[1])