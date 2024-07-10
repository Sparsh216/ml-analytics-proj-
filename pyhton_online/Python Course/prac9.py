# class c2dvec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
    
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j" 
# class c3dvec(c2dvec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap=k
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j+{self.kcap}k" 

# d2=c2dvec(5,6)
# d3=c3dvec(5,6,7)
# print(d2)
# print(d3)

class Employee:
    salary=50000
    inc=1000
    @property
    def salaryAfterInc(self):
        return self.salary+self.inc
    @salaryAfterInc.setter
    def salaryAfterInc(self,sss):
        self.inc=sss-self.salary
incro=Employee()
incro.salaryAfterInc=60000
print(incro.salaryAfterInc)
print(incro.inc)