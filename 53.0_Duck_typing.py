'''
Duck typing:
1. The name d  uck typing comes from the phrase, if there is a bird, which looks like a duck and quacks like a duck then it is a duck,
2. It is a type system used in dynamic languages.
3. In this type or class of the object is less important then the method it defines.
4. By use of duck typing, we check for the presence of a given method or attribute instead of types of class or objects
   for example:
   If we have a object of any class and we want to call a method and a attribute by use of that object then at that time what matters is that  whether that object supports
   that method and attribute or not rather than that of which class object belongs.

   for example:
   we have a object y = list("ram"), and we want to call the method len(), then here what matters is whether the object y supports the len method or not rather than to which
   class type it belongs.
   Even if y = str("ram"), then also len() methods works because the object y supports method len().
   Now in case of y = 32, len() attribute would not work, it is not because it belongs to int class, it is because int class or object y of int class does not have len() method
'''

'''
Consider the examples:
'''
#Example 1:
class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("swim in sea.")

y1  = Bird()
y1.fly()# here this will work because y1 has attribute fly not because y1 belongs to class Bird.

y2 = Airplane()
y2.fly()#here this will work because y2 has attribute fly not because y2 belongs to class Airplane.

y3 = Fish()
#y3.fly() #here this will not work because y3 has no attribute fly not because y3 belongs to class Fish,
'''Do run the above code by removing the comment sign and read the error.'''
