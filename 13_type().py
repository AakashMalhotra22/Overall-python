'''
type() function is used to check the datatype of the given object.
Example:
'''
print(type(2.3)) # float
print(type(2)) # int
print(type("ask")) # str
print(type([1,2])) # list
print(type({1:2,2:3})) # dict
print(type((1,2))) # tuple
print(type({1,2})) # set
print(type(True)) # bool
b = None
print(type(b)) #None
print(type(range(0,10)))