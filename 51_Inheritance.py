'''
Inheritance:
1. This is the way to inherit one class in other or to inherit all the features of a class in other class.
2. The class which gets inherit in other class is called parent class or super class and the other class is called child class or sub class.
3. There are three types of inheritance.
   1. Single-level Inheritance
   2. Multi-level Inheritance
   3. Multiple Inheritance
'''

# Example-1 (Single-level-Inheritance)
'''
In this one class inherit the other class.
'''
class A:
    def feature1(self):
        print("feature1 is working")

class B(A):# Here we inherit all the feature of A in B, Here A is superclass/ Parent class of B or B is the sub class or child class of A

    def feature2(self):
        print("feature3 is working.")

a1 = A()
b1 = B()
b1.feature1()

#Example -2 (Multi-level-Inheritance)
print("")
'''
In this one class inherit the second class and the second class inherit the third class.
Means here first class is grandchild, second class child, and third class is parent

'''
class A1:
    def feature1(self):
        print('feature 1 is working.')
class A2(A1): #Here A2 gets all the features of A1
    def feature2(self):
        print("feature 2 is working. ")

class A3(A2):# Here A3 gets all the features of A2 which means it also gets the features of A1 as A2 inherits A1.
    def feature3(self):
        print("feature 3 is working.")

a3 = A3()
a3.feature1()
a3.feature2()
a3.feature3()

print("")
# Example-3
'''
Multiple Inheritance
1. In this a class inherits the properties of two different classes which may or may not be related to each other.
'''

class A:
    def feature1(self):
        print("feature 1 is working.")
class B():
    def feature2(self):
        print("feature 2 is working.")
class C(A,B):# Here C class inherits all the features of class A and Class B
    def feature3(self):
        print("feature 3 is working.")

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
