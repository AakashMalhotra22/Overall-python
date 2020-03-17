'''
1. a,*b = iterable_object
   In this case, first value of the iterable_object will be taken by a and rest of the values will be stored in the list and
   that list will be equals to b.

2. This will not work in case of non-iterable objects like 'int', 'float',etc.

3. a,*b,c = iterable_object
   In this case, first value of the iterable_object will be allotted to a, c takes the last value and remaining values will be stored
   in the list and that will be equals to b.

'''

#1When iterable object is str

a,*b ="arm"
print(a)
print(b)

print("")
#2 When iterable object is list


a,*b =[1,2,3]
print(a)
print(b)

print("")
#3 When iterable object is tuple

a,*b =(1,2,3)
print(a)
print(b)

print("")
#4 When iterable object is dict
a,*b = {'a':2,'b':3, "c":4}
print(a)
print(b)

print("")
#5 When iterable object is set
a,*b = {1,2,3,3,4}
print(a)
print(b)

print("")
#6 When iterable object is range
a,*b = range(10)
print(a)
print(b)

print()
#7 More

a,*b,c ="ramesh"
print(a)
print(b)
print(c)