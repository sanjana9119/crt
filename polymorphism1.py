'''
polymorphism:
poly=means
morphism=forms
types of polymorphism :
1.compile time 
    1.function overloading-->multiple function 
    2.operator overloading
2.runtime 
    1.method overriding
'''
'''
print(10+20)
print("abc"+"xyz")
#funtion method overloading

def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c
def add(a,b,c,d):
    return a+b+c+d
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

#python doesnot support function overloading directly we can achieve this using variable length arguments(using*)
def add (*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
''' 
#operator overloading 
class A():
    def __init__(self,x):
        self.x=x
    def __lt__(self,val):
        return self.x+val.x
a=A(10)
b=A(20)
print(a+b)

class B