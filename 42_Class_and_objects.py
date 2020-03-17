'''
Classes:
1. Class are used to create objects.
2. Class consists of the attributes - variables, and behaviour- methods(Function)
3. Instance represents a particular object created from the class.

'''
'''
Index
1. Basics
2. How to create an empty class:
'''
'''
Basics
'''
class Computer():
    def config(self):
        print("i5, 16gb, 1TB")

a = "8" # Here a is object/instance of type/class string
b = 7 # here b is object/ instance # of type/class int
print(type(a))

com1 = Computer()# This means com1 is a variable of tye/class computer which belongs to module main(means class and object).
com2 = Computer()

print(type(com1))
Computer.config(com1)
Computer.config(com2)
print("  ")
com1.config() #These are used normally
com2.config()


print(" ")


'''
Creating an empty class:
  a. Use pass to create an empty class.
'''


class Aakash:
    pass
