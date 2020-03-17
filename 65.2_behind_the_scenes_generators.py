# Understands the behind the scenes in generators.

def f1():
    for i in range(10000000000000000000000000000):
        yield i*i

y = f1()
'''
Now here the object of the f1 is created, nothing else is happened, it has not executed the function, it will execute the
function when you calls its value.
'''
print(next(y))
'''Now here it just loops through to get first i =0 and prints that value and suspends the function execution here, now when you
call the next value, then the execution of the function starts from i=0 only.'''

print(next(y))
'''Now, here it starts the function from where it was previously called off that is i =0 and again loop through it to give
i=1 and suspends the execution and when you call the next value, then hte execution of the function starts form i=1.'''


#This function is not storing the value in the memory, it is just generating the value when that valye is called.

'''
Why on writing print(y), it gives the address and location and not the value, this is because
1. Here y is the object of generator class, and in generator class the __str__ method is not defined, so when you write
   print(y), it just prints out the location and its value by default.
'''
print(y)

# Now consider a normal function

def f1():
    for i in range(100000000000):
        print(y)
'''If you create the object of this function, it would create a memory error, because as soon as you create the object of 
this function, it would just prints out all the value and uses a lot of memory.
'''


#2nd way

def f2():
    y = []
    for i in range(1000000000000000000000):
        y.append(i)

    return y
'''
y = f2()
print(y) 
This will give an error, as it will first store the value in the memory then returns it out.
'''
