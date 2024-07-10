# print("This is practice 2")

# f1=input("Enter fruit 1")
# f2=input("Enter fruit 2")
# f3=input("Enter fruit 3")
# f4=input("Enter fruit 4")
# f5=input("Enter fruit 5")
# f6=input("Enter fruit 6")
# f7=input("Enter fruit 7")
# l1=[f1,f2,f3,f4,f5,f6,f7]
# print(l1)

# l1=[12,56,86,55,7,23,48]
# l1.sort()
# print(l1)

# t1=(0,150,5,0,54,0,854,5,48,2)
# print(t1.count(0))
# list1 = [1, 2, 3, 4, 5]
# list2 = [123, 234, 456]
# d = {'a': [], 'b': []}
# d['a'].append(list1)
# d['a'].append(list2)
# print d['a']
a=int(input())
lis=[]
for i in range(a):
    lis.append(str(input()))
print(len(set(lis)))
