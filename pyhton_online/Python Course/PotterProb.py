n=int(input("Enter the number of apples that Harry have: "))
mn=int(input("Enter minimum number of students: "))
mx=int(input("Enter maximum number of students: "))
if(mx>mn):
    for i in range(mn,mx+1):
        if(n%i==0):
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")
if(mx==mn):
    if(n%mn==0):
        print(f"This is not a range and {i} is a divisor of {n}")
    else:
        print(f"This is not a range and {i} is not a divisor of {n}")
if(mn>mx):
    print("This is not a valid range")

