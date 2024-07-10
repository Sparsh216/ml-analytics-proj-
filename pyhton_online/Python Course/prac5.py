# l1=["Sparsh","Harry","Sohan","Rahul","Raju"]

# for item in l1:
#     if(item.startswith("S")):
#         print(item)

# ta=int(input("Enter the number of which you want table: "))
# i=0
# while i<=10:
#     print(f"{ta}X{i}={ta*i}")
#     i+=1

s=1
sp=4

for i in range(3):
    for j in range(sp):
        print(" ", end="")
    for k in range(s):
        print("*", end="")
    sp=sp-1
    s=s+2    
    print(end="\n")

