class Complex:
    def __init__(self,i,j):
        self.real=i
        self.imaginary=j
    def __add__(self,n):
        return Complex(self.real+n.real, self.imaginary+n.imaginary)
    def __mul__(self,n):
        mulreal=self.real*n.real-self.imaginary*n.imaginary
        mulimage=self.real*n.imaginary+self.imaginary*n.real
        return Complex(mulreal,mulimage)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=Complex(3,2)
c2=Complex(1,7)
print(c1+c2)
print(c1*c2)