'''
Special method __init__
1. It is used to create attributes(variables) of the class
2. By the help of this you can take parameters values from the user at the time of creating the class.

'''

class computer:
    def __init__(self,cpu,ram): #This self.cpu and self.ram now becomes the attributes of the class which you can use in other methods of the class or you can simply call them.
        self.cpu = cpu
        self.ram = ram
    def confi(self):  #This is method of the class.
        print("confi is" , self.cpu ,self.ram)

com1 = computer("i5", 16)
com2 = computer("i7", 100)
com1.confi()
com2.confi()

print("                  ")
print(com1.ram)
print(com2.ram)

print("")
# EXAMPLE -2


class Opt:
    def __init__(self,a,b):


        self.b = b
        self.a = a

    def add(self,c,d):
        self.c =c
        print(self.a+c+d)
    def sub(self):
        print(self.c-self.a)

y = Opt(0,4)
y.add(3,4)
y.sub()

print("")
# Example -3

class oper():
    def __init__(self,a):
        self.a = a

    def changer(self,b):
        self.a = b
        return self.a


y = oper(1)
print(y.a)
print(y.changer(3))
