'''
Method Overloading
1. When you have two  method with same name inside a class but have different arguments.
   for example
   class student:
       def aver(self,a,b):
               print((a+b)/2)
       def aver(self,a,b,c): # This will be given preference because it comes at the last
               print((a+b+c)/3)

2. Python does not support method overloading, if you create a object of class student and call the aver method, then the method which is defined at the last in the class
   will be called.
'''

#Example 1:

class student:
    def aver(self, a, b):
        print((a + b) / 2)

    def aver(self, a, b, c):  # This will  be given preference
        print((a + b + c) / 3)
y = student()
y.aver(3,4,5)
#y.aver(3,4)# This would show an error


# Example 2:
'''
You can do method overloading by None keyword
'''

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def add(self,a=None,b=None, c=None):

        s = 0

        if a!=None and b!=None and c!=None:
            s = (a+b+c)

        elif a!=None and b!=None:
            s = (a+b)

        else:
            s = a
        return s
s1 = student(23, 34)
print(s1.add(2,4))

print("  ")

#Example 3

'''
Method overloading by use of *args
'''

class student:
    def sum(self,a,*args):
        c =a
        for i in args:
            c+=i
        print(c)

y = student()
y.sum(1,2,4,5,6,7)# now here you can pass any number of arguments.