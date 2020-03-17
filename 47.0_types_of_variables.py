'''
There are two types of variables.
1. Instance variable:
2. class variables:
'''

'''
Instance Variables:
1. Instance variables are owned by instances of the class.
2. This means for each objects or instance of a class, the instance variables are different.
3. Instance variables are defined within the special __init__()method.
4. It can be changed for a particular instance and not for all the instances at one go like by writing Name_Of_Class.instance_variable_name = something
5. Variables at instance level is referred to as instance variables
'''

#Example 1:
'''
1. Instance variables are defined within the special __init__()method.
2. It can be changed for particular instances and not for all the instances at one time
'''

class Car:
    def __init__(self):
        self. mil = 10 # This is instance variable
        self.com = "BMW"# This is instnace variable

c1 = Car()
c2 = Car()

c1.mil = 8
print(c1.mil)
print(c2.mil)

# You cannot change the instance variables for all the instances of the class at one go like this.
Car.mil = 100# Now this has not changed the c1.mil value and c2.mil values but it has created a new class variable mil whose value is 100.
print(c1.mil)
print(c2.mil)

print(" ")

#Example-2
#  This means for each objects or instance of a class, the instance variables are different.

class Car:
    def __init__(self,a,b):
        self. a = a # This is instance variable
        self.b = b # This is instance variable


y1 = Car(3,2)#  Now here this instance has its own instance variables.
y2 = Car(5,6) # Now here this instance has its own instance variables.
print(y1.a)
print(y2.a)