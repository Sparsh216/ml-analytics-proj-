# name=input("Enter the name of the student: ")
# marks=float(input("Enter the marks of the student: "))
# number=float(input("Enter the phone numberof the student: "))

# print("The name of student is {0}, marks is {1}, phone number is {2}".format(name,marks,number))

# l=[str(i*7) for i in range(1,11)] 
# print("\n".join(l))
# lis=[54,5,6,8,85,65,75,55,5,4,8,3,7,9,2]
# div=lambda a:a%5==0
# print(list(filter(div,lis)))

from functools import reduce
l=[2,5,6,8,2,3]
print(reduce(max,l))