
n=int(input("Enter the number of foods you want to enter: "))
lis=[int(input("Elements of list: ")) for i in range(n)]
ls3=lis[:]
lis2=lis[:]
print(lis2[::-1])
lis.reverse()
print(lis)
for i in range(int(n/2)):
    ls3[i],ls3[n-i-1]=ls3[n-i-1],ls3[i]
print(ls3)
