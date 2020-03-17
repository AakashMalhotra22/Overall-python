#id: Every object in python has its address which can find my using id(), for this press print(id(10))

num = 5
print(id(num))

name = "navin"
print(id(name))

a =10
b = a
print(id(a))
print(id(b))

print(id(10))

k = 10
print(id(k))

a = 9
print(id(a))
print(id(b))

b =8
print(id(b))

#Garbage collection: Whenever you have a data in your memory which is not used, it will be garbage collection later.

#Constants in python, to write constants whose values are fixed like pi = 3.14, but in python, you can change the value,so can avoid
# the changes but show your intentions by typing variable in uppercase which indicates it is fixed don't change it.

PI = 3.14
print(PI)


