'''
Inner class:
1. In case of inner class, you can create the object outside the inner class means in the main class or outside of all the classes.
2. Object of inner class are also stored in different memory.
'''

#Example 1
class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self. laptop() # This is the object of the inner class.
        '''if you not use parenthesis here with laptop then you have to use parenthesis at the time of calling them.'''

    class laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"
        def show(self):
            print(self.brand,self.cpu)


s1 = student("Aakash", 12)

# Way-1
'''
First creating the object of outer class, then calling the inner class considering it as a function of the created object as laptop() is one of the object of the class student
'''
print(s1.lap.brand)
print(s1.laptop().brand)
s1.lap.show()
s1.laptop().show()

print("")


# Way-2
'''
Creating the object of the inner class in the outer class then using it.
'''

lap1 = s1.lap
print(lap1.brand)
lap1.show()
'''
or
'''
lap1 = s1.laptop()
print(lap1.brand)
lap1.show()

print("")

# Way-3
'''
Creating the object of inner class outside both the class.
'''

s2 = student.laptop()
print(s2.brand)
s2.show()
print("")
print("Example-2")
print("")
#Example 2:
'''
Everything is same, just a difference of parenthesis in laptop
'''

class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self. laptop # This is the object of the inner class.


    class laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8"
        def show(self):
            print(self.brand,self.cpu)


s1 = student("Aakash", 12)

# Way-1
'''
First creating the object of outer class, then calling the inner class considering it as a function of the created object as laptop() is one of the object of the class student
'''
print(s1.lap().brand)
print(s1.laptop().brand)
s1.lap().show()
s1.laptop().show()

print("")


# Way-2
'''
Creating the object of the inner class in the outer class then using it.
'''

lap1 = s1.lap()
print(lap1.brand)
lap1.show()
'''
or
'''
lap1 = s1.laptop()
print(lap1.brand)
lap1.show()

print("")

# Way-3
'''
Creating the object of inner class outside both the class.
'''

s2 = student.laptop()
print(s2.brand)
s2.show()
