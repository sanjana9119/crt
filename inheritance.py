'''
inheritance:acquiring properties from one class to another class 
Types of Inheritance:
1.single
2.multilevel 
3.multiple 
4.hierarchical
5.hybrid
#single inheritance
class a:
    def display(self):
        print("A display method")
class b(a):
    def display1(self):
        print("B display method")
B=b()
b.display()
b.display1()

#multilvel inheritance
class grandparent():
    def g_p(self):
        print("Land=20acres")
class parent(grandparent):
    def p(self):
        print("House:2")
class Child(parent):
    def c(self):
        print("car:Thar")
b=child()
b.p()
b.g_p()
b.c()
'''
#heirerchical inheritance
class a:
    def display(self):
        print("A display method")
class b(a):
    def display1(self):
        print("B display method")
class c(a):
    def display(self):
        print("c display method")
#multiple inheritance
class a:
    def display(self):
        print("A display method")
class b:
    def display1(self):
        print("B display method")
class c(a,b):
    def display(self):
        print("c display method")
#method resolution order -->MRO
#hybrid inheritance
