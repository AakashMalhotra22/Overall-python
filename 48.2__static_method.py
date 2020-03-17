'''
Static method:
1. It is used to do something different has no relation with the attributes of class.
syntax

class C:
   @staticmethod
   def fun(arg1,arg2,arg3,...)
        print(#something)

2. A static method can't access or modify class state and object state menas can't use class variables and intance variables.
3. They are utility type methods that take some parameters and work upon those parameters only.
4. A static method is a method which is bound to the class and not the object of the class.
5. You cannot call instance variables in it.
'''

#Example1:

class student():
    @staticmethod # This is required decorators, before static method.
    def info(a):
        print("This is student class",a)

s1 = student()
s1.info(4)

print("")

#Example2:
'''
You cannot use attributes of the class such as self.b in the static method, it would show an error.
'''


class student():

    def __init__(self,b):
        self.b = b

    @staticmethod
    def info(a):
        print("This is student class",a)# here you cannot use self.b

s1 = student(3)
s1.info(4)


#Example3
'''
A static method is a method which is bound to the class and not the object of the class.
'''


class student():
    @staticmethod
    def info(c): # here you can call this method without creating any object of the class.
        print("hi",c)

    def ram(self,a):# her you cannot call this method without creating any object/instance of the class
        print(a)

student.info(3)

#student.ram(3) This will show an error, because ram is an instance method, so to call it you have to create an instance/object.