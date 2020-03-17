'''
Anonymous function lambda:
1. Another way to write function in python

syntax:
lambda a,b(variable names):a+b(variable operation)

'''
"Examples: Basic to advance"
#1.
f = lambda a : a*a
result = f(5)
print(result)

#2
g = lambda a,b : a+b # You can pass any number of arguments, bu the  expression should be one.
result = g(1,3)
print(result)

#3
aakash = lambda a,b,c,d: a+b-c*d

result = aakash(100,2,34,2)
print(result)

#4
greatest = (lambda a,b: a if a>b else b)
y = greatest(2,3)
print(y)