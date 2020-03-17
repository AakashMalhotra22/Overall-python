'''
yield keyword:
  The use of yield that, when yield statement is hit, the program suspends function execution and returns the yielded
  value. When the program is suspended the state of that function is saved, so when you again call the function, the
  execution of function starts from the value where it was previously called off.

return keyword:
   In case of return keyword, when return statement is hit, the programs stops the execution of the function
   completely and returns out the value and in this case the state of function is not saved, so when you again call
   the function, the execution of function starts from the beginning and not from the value where it was previously
   called off.

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