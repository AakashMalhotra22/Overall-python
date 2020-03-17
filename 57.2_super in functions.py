'''
1. super feature can also be used to call methods not only the constructor.
2. syntax:
   super.function_name()

'''

class B():
    def __init__(self):  # Constructor
        print("in B init")
    def feature3(self):
        print("feature3 is working.")

    def feature4(self):
        print("feature4 is working.")


class C(B):
    def __init__(self):
        super().__init__()# It will call the constructor of A in accordance with method of method resolution order.
        print("in C init")
    def feat(self):
        super().feature3()


a1 = C()
a1.feat()

print(" ")
print(" ")
#Example 2:
class A:
    def __init__(self):
        print('tHIS IS ADDITION CLASS')

    def sum(self,a,b):
        print(a+b)

class B(A):
    def __init__(self):
        print("This is parent class.")

    def multiply(self,c,d):
        print(d*c)
        print("Also the sum of the numbers are: ")
        super().sum(c,d)


y = B()
y.multiply(3,4)

print("")
# Example 3:
'''Instead of super we can use the class name of parent class only'''

class A:
    def __init__(self):
        print('tHIS IS ADDITION CLASS')

    def sum(self,a,b):
        print(a+b)

class B(A):
    def __init__(self):
        print("This is parent class.")

    def multiply(self,c,d):
        print(d*c)
        print("Also the sum of the numbers are: ")
        A().sum(c,d)


y = B()
y.multiply(3,4)
