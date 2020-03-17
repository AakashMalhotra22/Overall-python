'''
1. Constructor in inheritance.
2. super method:
   1.It is used to call the constructor or method of the super class in the function of the current class.
   2. It's syntax is:
       super().functionname
       Ex: super().__init__()
           super().feature1()
   You can also use the name of parent class instead of super, for example: if B is parent class of A
       It's syntax is:
       B().functionname
       Ex: B().__init__()
           B().feature1()

3. MRO- If you inheritant two classes then  in a class and both have same function, then the class which inheritance first will be preferred.
   Ex:
   class C(A,B): # Here A will be preferred
   class C(B,A) # here B will be preferred.



'''

'''
Consider all the examples
'''

#Example 1:

class A:

    def __init__(self): # Constructor
        print("in A init")

class B(A):
    pass

a1 = B() # It is calling the constructor of A.
'''Since, we dont have any constructor in B, that's why it is calling constructor of A otherwise, it will not call, as shown in next
example.'''

print("")
#Example 2:

class A:

    def __init__(self): # Constructor
        print("in A init")

class B(A):
    def __init__(self): # Constructor
        print("in B init")

a1 = B() # It is calling the constructor of B.


print("  ")
#Example3:

# IF you want to call the constructor of A inspite of having constructor in B. then use super.
class A:
    def __init__(self): # Constructor
        print("in A init")

class B(A):
    def __init__(self): # Constructor
        super().__init__()# here you can also use A().__init__()
        print("in B init")

a1 = B() # It is calling the constructor of A.

''' When you call super then it will first call constructor of Super class first then call init of sub class.'''



print("    ")

#Example 4:

class A:
    def __init__(self):  # Constructor
        print("in A init")

class B():
    def __init__(self):  # Constructor
        print("in B init")


class C(A,B ):
    def __init__(self):
        super().__init__()# It will call the constructor of A in accordance with method of method resolution order,# here you can also use A().__init__()
        print("in C init")

a1 = C()

'''MRO first finds the constructor of itself, then prefer order, here as C inheritant A first then B, so in accordance to MRO, function A will be called first.'''

# This MRO also follows for methods/ functions, if two class have same function then it will prefer order which is coming first.


print("")
#Example 5:

class A:
    def __init__(self):
        print("in A init")

class B(A):
    def __init__(self):
        print("in B init")

class C(B):
    def __init__(self):
        print("in C init")
        super().__init__()# here you can also use A().__init__()

c = C()


print("")
#Example 6:

class A:
    def __init__(self):
        print("in A init")

class B(A):
    def __init__(self):
        print("in B init")
        super().__init__()

class C(B):
    def __init__(self):
        print("in C init")
        super().__init__()

c = C()

