'''
Iterators:
0. List, string, dict, tuple, sets and range objects are iterables and int, float, bool and None object are not iterables.
1. Iterators are the objects which are created on calling the iter method on iterables.
   Ex
   y = [1,2,3]- This is iterable object
   x = iter(y) - This is an iterator

2. The  trademark or most important property of iterator object is that they can call __next__ method.
3. list, string, dict, tuple, sets and range objects are not iterators, they all are iterables objects because they cannot
   call the __next__method.

4. The use of iterators are used to fetch one value at a time, or to fetch values one at a time.
5. One more important property of iterator is that, it starts the execution after that value where the execution
   was previously left off.

6. To create iter class, you need two method __iter__ method and __next__method, it can be induced in the class by use of
   operator overloading.
   __iter__ method is used to iterate through the loop, means to fetch values one at a time means if there is not an
   __iter__ method, then you cannot apply for loop to iterate through it.
   __next__ method is trademark of the iterator, without it, no functions of iterator will work means you neither can fetch
   values one by one nor you can fetch values one at a time.
'''

# Examples-1

l = [1,2,3,4]

#Two ways to create iterators

it = iter(l)
it = l.__iter__()

# Two ways to call the next method.

print(it.__next__())
print(next(it))

# Looping through an iterator,

'''One more important property of iterator is that, it starts the execution after that value where the execution was 
   previously left off.'''
'''As here you have already called the value 1 and 2 from the iterator, now this loop will call only 3 and 4 value.'''

for i in it:
    print(i)





print("")

# Example-2
'''When you are creating your own iterator class, you need to two methods, first is iterator method and next method'''

class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):# If you dont use this, you cannot loop through this class or simply you cannot use for loops, Without it you can use the next method
       return self  # here we can only write return self which means make the object an iterator.
    def __next__(self):# If you dont use this, you cannot use for loops and next method.


        if self.num <= 10:
               value = self.num
               self.num+=1
               return value
        else:
            raise StopIteration # this is same as break, but break applies in for loops case but there is no for loop, so
                                # here we are using stop Iteration.

t1 = topten()
print(iter(t1))# This will print the location.
print(t1.__next__())
print(next(t1))
for i in t1:
    print(i)

print("")
#Example-3
'''If you call the next method in an iterator, but there is no next value in the iterator, then it would show an error
   of stop iteration'''

y = iter([1])
print(next(y))# this will return 1
#print(next(y))# This will show an error, as there is no further value.




