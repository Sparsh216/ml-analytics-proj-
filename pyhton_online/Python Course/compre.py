n=int(input("Enter the number of items: "))
lis=[]
for i in range(n):
    lis.append(input(f"Enter item number {i}: "))
comp=input('''Input the type of comprehension you wasn "List", "Set", "Dictionary": ''')

if(comp=="List"):
    lis1=[i for i in lis]
    print(lis1)
elif(comp=="Set"):
    Set1={i for i in lis}
    print(Set1)
elif(comp=="Dictionary"):
    Dict1={i:f"item{i}" for i in lis}
    print(Dict1)
