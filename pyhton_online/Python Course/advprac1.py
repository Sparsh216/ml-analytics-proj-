# try:
#     with open('sample.txt','r') as f:
#         print(f.read())
#     with open('sample2.txt','r') as f:
#         print(f.read())
#     with open('sample3.txt','r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("program is completed and file3 was not found")
# lis=[1,32,43,False,'Sparsh',53,43]

# for index,item in enumerate(lis):
#     if index==2 or index==4 or index==6:
#         print(index+1 , item)

# n=int(input("Enter the number of which you want table"))     
# lis=[n*i for i in range(1,11)]   
# print(lis)

# a=int(input("Enter number 1: "))
# b=int(input("Enter number 2: "))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError :
#     print("Infinite")


n=int(input("Enter the number of which you want table"))     
lis=[n*i for i in range(1,11)]   
with open('sample2.txt','w') as f:
    f.write(str(lis))