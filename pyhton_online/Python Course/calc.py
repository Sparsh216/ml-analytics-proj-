class calculator:
    def square(self,num):
        return num**2
    def cube(self,num):
        return num**3
    def sqroot(self,num):
        return num**0.5
    @staticmethod
    def greet():
        print("Hello, Good afternoon")

num=calculator()
num.greet()
print(num.square(4),num.cube(4),num.sqroot(4))
