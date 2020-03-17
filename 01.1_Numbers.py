'''
Numbers: These store numerical information and come in two forms.
1. Integers- 1. These are whole numbers.
             2. These are denoted by int

2. Floating Point numbers- 1. These are numbers with decimal.
                           2. These are donated by float.

There is also one more type but not included in it, that's complex number.

3. Complex number form

Here iota is represented by j, such as 2+3j, 4j,etc.

'''









'''
Index
1. type and conversion.
2. Simple operations in numbers to advance and few points related to it.
3. Inbuilt functions in numbers and how to add more.
4. Increment in numbers
5. Comparison operators in numbers.
6. Points related to numbers
'''










'''
1. Checking the types of numbers and converting into one another.
'''

# To check whether the number is int, float, complex or something else, use type function

print(type(2))
print(type(2.3))
print(type(2+3j))

# The output means 2 is the object of class int, 2.3 is the object of class float and 2+3j in object of class complex.

print(" ")

# Conversion into the other numbers.

print(float(2)) # it will convert object 2 which is of class int into the object 2.0 of class float.
print(int(2.3)) # it will convert the object 2.3 which of class float into the object 2 of class int on basis of rouding off.
print(complex(2,3)) # it will convert the object (2,3) into the object 2+3j which is object of complex number class.

#You can also convert the numbers in string, boolean, etc.

print(str(2))
print(bool(3))

print(" ")
print(" ")






'''
2. Simple Operations in Numbers.
'''

# Simple operation can be used such as +,-,/,//,*,**(for power), %(Addition modulo).

print(2+2)

print(8%4)
print(4/2)

# here we got 2.0 not 2 because it give us float which means floating point representation, in which "." used after numbers.
# if you divide 5 by 2 then you want 2.5 not 2 so it convert this int into float to give you 2.5 as output then 2.0
# if you want answer in integer than use double slash.

print(5//2)


#Use of multiple operations on the basis of BODMAS or PEDMAS rule.

print(8+9-10)
print(8+2-7+(0+30-12))

# Power function(**)
print(2**12)

# Mod operator: Apply Addition Modulo and gives the remainder
print(10%3)


'''A few more points in numbers.
1. If you apply any operation but not division in numbers then you will get the output in the same form of numbers as your input.
   For example:
   print(2+3-2%4)
   Output is 3 not 3.0 because your input is not in float then your output will also not in float.

2. If you apply division operation between the numbers then the answer would be in float only and to avoid that you have to use the operator (//).
   print(4/2)
   Output is 2.0 not 2  


3. If you apply operation between numbers in which some are in float and some are in int, then output would be in float. 
    
'''
'''
PEDMAS
In Python operations are solved with use of PEDMAS rule.

1. P- Parenthesis
2. E - Exponent
3. D - Division
4. M - Multiplication
5. A - Addition
6. S  - Subtraction

Exceptions: 

1. Here /,//,*,% have same precedence which means if you use these operations between the numbers, then operations would be applied in the order from left to right.
   For example:
   print(3*7//5*10%4)
   It would be executed from left to right because in the question, the question have same order precedence.
   3*7=21 is executed first, because it appears to be there first.
   Then 21//5 =4
   Then 4*10 = 40
   Then 40%4 = 0 is the output 
   
   Example 2:
   print(3*7//5*10%4**2)
   In this question we have following operators ** and *,//
   In this question first 4**2 = 16 will be solved on the basis of PEDMAS then the operations will be executed from left to right order.
   Ouput is as,
   3*7//5*10%16
   Then 40*16 = 8, (Left to right order)

2. If a operation repeats more than once then the order of evaluation from left to right for all but for power(**), the order is from right to left.
   For example:
   print(2//4//2)
   Output will be calculated as, since operation is division then order is from left to right.
   First 2//4 =0.5
   Then 0.5//2 = 0.25 is the ouput. 
   
   Example 2:
   print(2**1**2)
   Output will be calculated as, since operation is power then order is from right to left.
   First 1**2 = 1
   Then 2**1 = 2
   2**(1**2) = 2**(1) = 2, right to left order, first (1**2) is solved.

'''

print("  ")
print("  ")

'''
3. In built functions in numbers.
'''

print(round(2.32)) # it will round to the nearest integer that is 2.
#In rounding off, you can also assign till how many digits after decimal you want to round off.

print(round(2.321,2)) # answer is 2.32
print(round(2.321,1)) # answer is 2.3

# There are many other mathematical operators are such as absolute, and to use all you can import math modulus as,
from math import*


print("          ")
print(sin(2))
print(sqrt(3))


print("  ")
print("  ")

'''
4. Increments in Numbers:
'''

# 1st way
a = 1
a = a+1
print(a)

# Second way

b = 2
b+=1
print(b)

# You can also use other sort of increment such as multiplicative or subtractive increment like a*=1, a-=1.

print("     ")
print("     ")

'''
5. Comparision operators in number.
'''

# There are total 8 operators those are, ==, !=, <, <=, >, >=.
# Answer would be in True and False

a = 2
b = 3

print(a ==b) # it will yield answer in True and False
print(a !=b)
print(a <=b)
print(a >=b)
print(a <b)
print(a >b)

print("   ")

'''
6. Points about Numbers:
'''

'''
1. Complex numbers cannot be converted into other numbers.
2. int, float and bool objects are not iterable.
3. Iterable means that the elements in them can be iterated over.
4. If you try to iterate through int, float then it will show the error, int/ float object are not iterable.
5.


'''


















