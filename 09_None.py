'''
None.
1. None is a data type of python.
2. None is a keyword is used to define null value, or no value.
3. None is not same as 0, False, or an empty string.
4. The function without a return statement is known as void functions return None from the functions.
5. In None, first letter is always capital that's N.
6. Consider a function which do its work but has no return and print statement, so it would return nothing but if you use print statement before calling the function then it
   would return None.

   For example:
   Consider the list:
   l = [4,3,2,1]
   print(l.sort())
   Here sort function has no return statement, so here the output would be None, behind the scenes, the sort function has
   made the list sorted but couldn't return the sorted list, because of absence of return statement.
   Now, if you just write,
   print(l)
   then the output is [1,2,3,4] that's is sorted list, because the list was sorted by the function sort().

7. Make sure when you use a function without return statement, then fist call the function then just print the parameter by use of print statement
   which you have passed in the function.
   For example:
   l = [2,1]
   l.sort()
   print(l)
   output is [1,2]
8. None keyword is an object, and it is a data type of the class None Type.

9. Difference between None and Zero and empty strings in python.
   1. None means no value or null
   2. Zero does not mean no value, it means False.
   3. empty string also indicates False.

10. None keyword can be used as a placeholder for an object that we don't want to assign now.
    Ex:
    b = None
    This means there exists a variable b with no value.

11. 'NoneType' objects is not callable.
'''
b = None
print(b)

y= ""
print(y)
print(bool(y))
