'''
Generators:
0. Generators are used to get iterators without use of a iter and next methods,
1. Generators functions allows to declare a function that behaves like an iterator.
2. It allows to create an iterator in fast, easy and clean way.
3. Generators are special types of iterators.
4. There  are two ways to create the generators, first is by generator functions and second is generator comprehension.
5. Properties of generators:
   a. It looks like a function but uses the keyword yield instead of return.

   b. The use of yield that, when yield statement is hit, the program suspends function execution and returns the yielded
      value. When the program is suspended the state of that function is saved, so when you again call the function, the
      execution of function starts from the value where it was previously called off.

      In case of return keyword, when return statement is hit, the programs stops the execution of the function
      completely and returns out the value and in this case the state of function is not saved, so when you again call
      the function, the execution of function starts from the beginning and not from the value where it was previously
      called off.

   c. Generators are used to reduce the memory usage and make the code execute faster.

      1. Generators works by lazy evaluation means they work on demand means they do not store the result in the memory,
         rather than it generates the value at the time of calling by this it save cpu memory and computational resources.

         For example:
         If you are iterating through a loop say range(10 trillion), then it will not fetch all the value at one go, it
         will generate one value at a time, when it is needed.
         By this your code will run fast and uses less memory.

   d. What happens when you call __next__() method, past the end?

      StopIteration is a built in exception type, which is automatically raised once the generator stops yielding. It is
      the signal to the for loop to stop.

'''

# Examples-1

def topten():

    yield 1 #here yields are used to create convert this function into generator
    yield 2
    yield 3
    yield 4

values = topten()

print(type(values))
print(values)


# Two ways to call next value
print(values.__next__())
print(next(values))

# Looping
'''One more important property of generator is that, it starts the execution after that value where the execution was 
   previously left off, this is happening because of yield.'''
'''As here you have already called the value 1 and 2 from the iterator, now this loop will call only 3 and 4 value.'''

for i in values:
    print(i)

print("")

# Example-2
# Perfect squares

def SQUARE():

    n =1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

val = SQUARE()

print(next(val))
print(val.__next__())

for i in val:
    print(i)



