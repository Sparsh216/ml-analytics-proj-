# f=open('sample.txt')
# t=f.read()
# if 'twinkle' in t:
#     print("yes twinkle is in sample")
# print(t)
# f.close()



# def game():
#     return 84


# scorehi=game()
# with open('hiscore.txt') as f:
#     score=(f.read())
# if(score==''):
#    with open("hiscore.txt",'w') as f:
#         f.write(str(scorehi)) 
# elif(scorehi>int(score)):
#     with open("hiscore.txt",'w') as f:
#         f.write(str(scorehi))


with open('sample.txt') as f:
    content=f.read()
content=content.replace('donkey','twinkle')
with open('sample.txt','w') as f:
    f.write(content)