'''
data hiding:
access specifier 
1.private(__)
2.public
3.protected(_)

class a:
    a=10
    _b=20
    __c=30
obj=a()
print(obj.a)
print(obj._b)
print(obj._a__c)
'''
#access and modify private members from class using methods 
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def credit(self,amount):
        self.__balance+=amount
    def debit(self,amount):
        self.__balance-=amount
    def display(self):
        print("Current balance:",self.__balance)
b=Bank(1000)
b.display()
b.credit(1500)
b.display()
b.debit(500)
b.display() 