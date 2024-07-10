import re
str='''krishna.bamrara@gmail.com
Sparsh.bamrara@gmail.com'''
patt=re.compile(r'\S+@\S+')
matches=patt.findall(str)
print(matches)
with open ("emails.txt","a") as f:
    j=1
    for i in matches:
        f.write(f"Email {j} is: {i}\n")
        j=j+1
