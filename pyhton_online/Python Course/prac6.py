# print("Hello world")

# def tempconver(temp):
#     return (temp*1.8+32)


# t=int(input("Enter the temp in degree: "))
# print("The temperature in Fahrenite is ",tempconver(t))

def sumrecur(n):
    if(n==0):
        return 0
    else:
        return n+sumrecur(n-1)


t=int(input("Enter the number: "))
print("The sum of first n natural number is: ",sumrecur(t))