'''
Class variable:
1. These are the variables which is shared between all instances of the class.
2. It is same for all the instances/objects of the class.
3. if you change it's value then the value will be changed for all the instances of the class.

4. You can call class variable  by use of classname.classvariablename only.
5. You can also call class variable by use of self.clasvariablename but it would only work if there is no attribute in the class with same name as class variable.
6. These are defined outside all the methods.
'''


class Car:
    wheels = 4 # This is class variable
    def __init__(self):
        self. mil = 10 # These are instance variable
        self.com = "BMW"


c1 = Car()
c2 = Car()
# Ways of calling class variables:
print(c1.wheels)
print(c2.wheels)
print(Car.wheels)
print('')
'''
Propeties:
1. You can change class variable for particular object or for all the objects of the class.
'''
# changing for object c1 only.

c1.wheels = 5 # Here it has not changed the value for c1.wheels it has created new attribute of c1 called wheels which has value 5.
print(c1.wheels)
print(c2.wheels)
print(Car.wheels)
print('')

# changing for  all the objects
Car.wheels = 1000
print(c1.wheels)# The value for c1.wheels will not change because it has been changed to 5 in above.
print(c2.wheels)
print("")
#Example 2:
'''
You can call class variable either by use of classname.classvariablename or self.classvariable name inside the class if the class has no attribute with same class variable name.
'''

class Car:
    wheels = 4 # This is class variable
    def __init__(self,a):
        self.a = 3

    def hello(self):
        print(self.wheels, Car.wheels)
        '''
        here self.wheels and Car.wheels have same value that's 4 but behind the scene it works like this,
        Car.wheels just checks whether there is any class variable name wheels, if there is print it.
        
        self.wheels first check the class Car has any attribute wheel if it has then it will return it other wise it would then check is there any class variable name wheel and
        if it is there then it returns its value.
        In this class there is no attribute name wheel that's why it moved to class variable. 
        '''

c1= Car(3)
c1.hello()


#Example4:

class Car:
    wheels = 4  # This is class variable

    def __init__(self, a):
        self.wheels=a

    def hello(self):
        print(self.wheels, Car.wheels)
        '''
        here self.wheels and Car.wheels have same value that's 4 but behind the scene it works like this,
        Car.wheels just checks whether there is any class variable name wheels, if there is print it.

        self.wheels first check the class Car has any attribute wheel if it has then it will return it other wise it would then check is there any class variable name wheel and
        if it is there then it returns its value.
        In this class there is a attribute name wheel that's it just returns 3. 
        '''


c1 = Car(3)
c1.hello()



print("")
print("")
print("")

class ram:
    jai = 1
    def __init__(self,a):
        self.ram = a

y = ram(100)
print(y.jai)
print(ram.jai)