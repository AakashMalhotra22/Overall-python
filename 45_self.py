'''
self in classes
1. self represents the instance of the class.
2. By use of self keyword we can access the attributes and methods of the class in python.
3. self  acts as a pointer which helps the methods of the class to tell them to which instance/object, you have to operate.
4. We use self by convention, it is not mendatory to use self, you can use anything in place of self, like aakash but it should be letters not numbers or list or anything.
   Reason:
   We only require something to represent the instance of the class, it does not matter who is representing the class of method, it can be self, or any other name
'''

'''
Point1 explanation:
self represents the instance of the class.
'''

class computer:
    def __init__(self,name,age): # This self represents the instance of the class
        self.name = name
        self.age = age
    def update(self):
        self.age = 12

c1 = computer("ram", 24)
''' 
Here self in the class represents the instance c1 of the class
Now self.name represents c1.name in the class, self.age represents the c1.age in the class.
n 
'''
'''
Explanation of Point 2 and Point 3:
By use of self keyword we can access the attributes and methods of the class in python.
self  acts as a pointer which helps the methods of the class to tell them to which instance/object, you have to operate.
'''
class computer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def update(self):
        self.age = 12

c1 = computer("ram", 24)
c2 = computer("shyam", 24)
print(c1.age)
print (c2.age)
print("")
c1.update()
'''This is the use of self, you have not told update, which object c1 or c2 should be used to execute commands, but what self will do
it will take c1 to execute commands because you have written c1.update'''
print(c1.age)
print(c2.age)


print("")
'''
Example 3:
We use self by convention, it is not mendatory to use self, you can use anything in place of self, like aakash or anything
'''
class Ram:
    def __init__(aakash, y):# here aakash is repersenting the instance of class Ram
        aakash.y = y
    def love(aakash):
        print("jai shri ram")

aak = Ram(2)
print(aak.y)
aak.love()