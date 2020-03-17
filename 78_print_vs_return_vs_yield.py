#Print()
'''
1. Print is a function, not a statement.
2. Syntax is:
   print()
3. It does not affect the computer function.
4. In this output cannot be used further.
   for example:
   y = (2+2) and output is 4, now you cannot use this output further.
5. print() function can be used in for loops, function, classes or anywhere.

'''
#return
'''
1. return is a keyword but the statement in which return keyword is used is return statement.
   Ex:
   def f1():
      return "ram" #Here this is return statement which uses return keyword.

2. A return statement is used to end the execution of the function call and returns the result to the caller.
   For example:
   y = f1()
   Here y is the caller and the result which is "ram" is returned to the caller.

'''
'''
3. If the return statement is without any expression, then the special keyword None is returned.
   Ex:
'''
def f():
    return

y = f()
print(y)

'''
4. Return cannot be used outside the function.
5. The statements after the return statements are not executed.
   Ex:
'''
def f1():
    return 12
    print("hello")# This will not be executed.
y = f1()
print(y)

'''
6. The value which is returned can be used as an argument and can be passed to another function, stored as a variable 
   and just can printed for the benefit of users.
   Ex:
   def f1():
     return "ram"
   y = f1()
   Now, the value is stored in y, now you can use the returned value(i.e ram) anywhere.
'''
'''
7. If you written more than value in a return statement, then the output is in tuple.
   Ex:
'''
def f():
    return "ram",[1,23,2,3]

y =f()
print(y)
# You can also written single values,
for i in y:
    print(i)

# Another way:
a,b = f()
print(a)
print(b)
'''
8. In case of return keyword, when return statement is hit, the programs stops the execution of the function
   completely and returns out the value and in this case the state of function is not saved, so when you again call
   the function, the execution of function starts from the beginning and not from the value where it was previously
   called off.
   Ex:
'''

def f2():
    for i in range(3):
        return i

y2 = f2()
#Now here the object of f2 is created
print(y2)
'''Now here it just loops through to get first i =0 and prints that value and stops the function execution completely, 
  now when you write print(y2) again, then the execution of the function starts again from the beginning of the function and
  not from where it was left off(i.e at i=0)'''

print(y2)# here the output is 0 because execution of the function starts from the beginning.





#yield:
'''
1. yield is keyword in python.
2. The use of yield keyword is that, when yield statement is hit, the program suspends function execution and returns the
   yielded value. When the program is suspended the state of that function is saved, so when you again call the function, 
   the execution of function starts from the value where it was previously called off.
   For example:
'''

def f1():
    for i in range(3):
        yield i
y =f1()
'''
Now here the object of the f1 is created, nothing else is happened, it has not executed the function, it will execute the
function when you calls its value.
'''
print(next(y))
'''Now here it just loops through to get first i =0 and prints that value and suspends the function execution here, now when you
call the next value, then the execution of the function starts from i=0 only.'''

print(next(y))
'''Now, here it starts the function from where it was previously called off that is i =0 and again loop through it to give
i=1 and suspends the execution and when you call the next value, then the execution of the function starts form i=1.'''


#This function is not storing the value in the memory, it is just generating the value when that valye is called.


