'''
reduce:
1. syntax:
   from functools import*
   reduce(function_name(x,y),iterator)

2. It takes first two values from the iterator apply the function to those values to obtain a new value then again apply the function between the obtained value and the third value
    and so on till the iterable gets exhausted and then return the final result.
    Example:
        iterator = [a,b,c,d]
        f1 = f(x,y)
        reduce(f1,iterator)
        step1: val1 = f1(a,b)
        step2 val2 = f1(val1,c)
        step3 val3 = f1(val2,d)
        return val3

'''

'''
Examples: Basic to advance
'''
from functools import reduce

#Example:1
nums = [0,1,2,3,4]
sum = reduce(lambda a,b:a+b , nums)
print(sum)

'''behind the scenes it first adds 0 and 1 to get 1 then add 1 and 2 get 3 then add 3 and 3 to get 6 and then 6 and 4 to add 10.'''

#Example 2
nums = [10,1,2,3,4]
sum = reduce(lambda a,b:a*b , nums)
print(sum)
