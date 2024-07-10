n=int(input("Enter how many numbers you want to enter: "))
lis=[int(input("Elements of list: ")) for i in range(n)]
lis2=[]
for item in lis:
    var=True
    num=int(item)+1
    if(num<=10):
        lis2.append(num)
    while(var):
        n1=num
        n2=num
        rev=0
        while(n1!=0):
            rem=n1%10
            rev=rev*10+rem
            n1=n1//10
        if(n2==rev):
            print(f"The next pallindrome of {item} is: {rev} ")
            var=False
            lis2.append(rev)
        num=num+1
print(lis2)
