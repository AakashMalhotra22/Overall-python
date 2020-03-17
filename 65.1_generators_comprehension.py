'''
Generators comprehension:
1. One other way to create generators is by use of generator comprehension.
   syntax
   (x for x in iterable_object )

'''

y = (x*x for x in [1,2,3,4])
print(type(y))
print(y)# it will print the location and address of generators.

#Calling next values
print(next(y))
print(y.__next__())

#Looping
for i in y:
    print(i)