'''
There are three types of Methods
1. Class Method
2. Static Method
3. Instance Method

'''
'''
Instance Method:
1. Instance method opearates on an object/instance and has access to its instance variables.
2. It can modify the class state as well as object state means, it can use both class variables and instance variables as well as modify them.
3. It is  bound to the object of the class means you cannot call a instance method without creating a object of the class.
4. It is not bound to the class variable that means you can use it without creating any class variable.
'''

class student():
    school = "Aakash"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self): # This is instance method/function
        return (self.m1+self.m2+self.m3)/3



s1 = student(1,2,3)# m1, m2 and m3 are instance variable.
s2 = student(4,5,6)

print(s1.average())
print(s2.average())

print("   ")
'''Instance method are of two types:
1. Accessor Methods - for getting the values.
2. Mutators Methods - for setting the values.

'''

print(s1.m1)# This is accessor, as you are getting the valuess.
s1.m1 = 100 # this is mutators, as you are setting the values.
print(s1.m1)

"One more example of accessors and mutators are:"

class student():
    school = "Aakash"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self): # This is instance method/function
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self, value):
             self.m1 = value
print("  ")
s1 = student(1,2,3)
print(s1.get_m1())


'''In above examples, m1, m2,m3 are instance variable, which can be used with instance method'''



