'''
Class Method:
0. syntax
    Class C:
    @clasmethod
    def func(cls,arg1, arg2, arg3,...)# here in place of cls you can use anything, it would not create any difference, you can even use self but it may confuse you.
         #perform operation


1. It use it first you have to call class method decorator by writing @classmethod:
   Let's not use @classmethod line, then your code looks like

   def info(cls):
      print(cls.school)
   Now, here python will treat it as normal function, in which cls is used in case of self and it works normally.

2. You can pass as many as parameters inside this class method.
3. It only accepts class variable not instance variables which are created by use of __init__ method.
4. On changing the  value of class variable for particular object/instance, the value of the same class variable which is used inside the class method will not change.
5. On changing the  value of class variable for whole class, the value of the same class variable which is used inside the class method will also change.

6. A class method is a method which is bound to the class and not the object of the class but the instance method is bound to the object of the class.
   For example:
   You can call the class method of a class without creating any object of the class
   But you cannot call the instance method of a class without creating any object of the class.

7. It has access to the state of the class as it takes a class parameter that points to the class and not the object instance.
8. It can modify a class state that would apply across all the instances of the class.
   For example:
   It can modify a class variable which will be applicable to all the instances.
   Means if you change the class variable by use of class method then it would affect all the instance method in which the class variable is used.

9. It is not neccessary that to call a class method, you should have class variable.
'''
# Example1:
class student():
    school = "Aakash" # This is class variable

    @classmethod # This is required decorators before the class method.
    def info(cls):
        return cls.school

s1 = student()
print(s1.school)
print(s1.info())

print("")

# Example 2:
'''
You can use more than one parameter in class method
'''


class student():
    school = "Ram"

    @classmethod
    def info(cls, c):
        print(cls.school, c,)

s1 = student()
print(s1.school)
(s1.info(4))

print("")

# Example 3:
'''
Unlike other methods, you cannot use attributes of class which are created by use of __init__ method (self.a and self.b) inside the class method, it would show an error
'''


class student():
    school = "Ram"
    def __init__(self,a,b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls, c):
        print(cls.school, c)# Unlike other methods, you cannot use attributes of class(self.a and self.b) inside this method it would show an error

s1 = student(2,3)
print(s1.school)
s1.info(4)
print("")



#Example 4:
'''
On changing the class variable for particular instance/object, the variable which is used inside the class method will not change.
'''

class student():
    school = "R1"
    def __init__(self,a,b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls, c):
        print(cls.school, c)

s1 = student(2,3)
print(s1.school)
s1.info(40)
s1.school = "Aakash" # changing the class variable
print(s1.school)
s1.info(40)# The value of the variable inside the class method does not change.
print("")


#Example 5:
'''
On changing the class variable for whole student class , the variable which is used inside the class method will also change.
'''

class student():
    school = "R1"
    def __init__(self,a,b):
        self.a = a
        self.b = b

    @classmethod
    def info(cls, c):
        print(cls.school, c,)

s1 = student(2,3)
print(s1.school)
s1.info(40)
student.school = "Aakash" # changing the class variable
print(s1.school)
s1.info(40)# The value of the variable inside the class method does not change.
print("")



#Example 6:
'''
Let's not use the decorator @classmethod
'''


class student():
    school = "R1"
    def __init__(self,a):
        self.a = a


    def info(cls,c):
        print(cls.school,c,cls.a)# As it is a normal method, you can use the attributes of the class.

s1 = student(2)
s1.info(3)# It works because it just treats the cls as self
#student.info(3,4) will not work


print("")

#Example 7:
'''
A class method is a method which is bound to the class and not the object of the class.
'''

class student():
    school = "R1"

    @classmethod
    def info(cls,c): # here you can call this method without creating any object of the class.
        print(cls.school,c)

    def ram(self,a):# her you cannot call this method without creating any object/instance of the class
        print(a)

student.info(3)

#student.ram(3) This will show an error, because ram is an instance method, so to call it you have to create an instance/object.


print(" ")

#Example 8:
'''
It is not neccessary that to call a class method, you should have class variable.
'''
class student():

    @classmethod
    def info(cls,c):
        print(c)
y = student()
student.info(3)
y.info(3)
