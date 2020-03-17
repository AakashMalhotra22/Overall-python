'''
Constructor and self
1. Heap memory:
   a. It is a memory where you will get all the objects.
   b. If you create two objects of a class then both the object will take have different Id's which means both the objects take different places in the heap memory.

2. Constructor:
   1. In python, there is a single type of constructor is available.
   2. Constructor are used to intilize member variable of the class.
   3. Constructor automatically called on class object creation.
   4. Using __init__ method, we can create constructor.
   5. syntax of the constructor  declaration
            def __init__(self, arg1, arg2, ... ):
               #body of the constructor
   6. There are two types of constructor in python:
      1. default constructor which takes no argument, its definition has only argument self which is reference to the instance being constructed and has syntax
                   def __init__(self):
                             #body of the constructor
      2. Parameterized constructor: It takes one or more than one arguments and has syntax
                            def __init__(self,arg1, arg2,...):
                                     #body of the constructor
'''

'''
Index:
1. Heap memory 
2. Constructor
'''

# Heap Memory:

class computer:# You can not make a class empty, if you want to do so, use pass.
    pass

c1 = computer()
print(id(c1)) # 7077520

c2 = computer() # 7937904
print(id(c2))

#Since, both the objects c1 and c2 are having different id, which means both the objects takes different spaces in hipe memory.
#Size of an object depends on number of variables and size of each variables.

print(" ")
print(" ")

'''
Constructor 
'''
class Computer:
    def __init__(self,a,b):# This is our constructor
        self.a = a
        self.b = b
        self.c = self.a + self.b
        print("This is the constructor")


c1 = Computer(2,3)
print(c1.c)
