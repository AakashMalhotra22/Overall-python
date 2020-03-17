'''
functions:
1. Functions allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code.
Syntax of function:
def name_of_function():# here use of parenthesis is that it tells the ide tha this is not a variable and : is used to write multiple statments.
  triple quote
  Docstring explains function:
  triple quote
  print("Hello"+name)

name_of_function:

2. use of return keyword is that it allows us to assign the output of the function to a new variable.
'''

'''
Basic to advance
'''
#1 use of docstring

def name_function():
    '''
    DOCSTRING: INFORMATION ABOUT THE FUNCTION:
    INPUT: NO INPUT
    OUTPUT: HELLO..

    '''

    print("hello")

name_function()
help(name_function)
print("")

#2. More function examples
# : is used to write multiple statements.
def greet(): # greet is function name, round bracket is used to tell that the greet is not a variable, it is a function.
    print("hello")
    print("Good Morning")

greet()

def sum(num1, num2): # num1, num2 are two arguments of the function.
    print(num1+num2)

sum(1,2)

sum(3,15)

# Return Statement
def sum(num1, num2):
    return num1+num2

result = sum(3,4)
print(result)

# To return two values
def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(10,2)
print(result1, result2)
