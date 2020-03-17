'''
Scope: The range or limit of a variable in till which they are defined is called scope.
For example, the scope of the a =5 inside the function is only up to function only, while the variable: a=10 can be used anywhere.

There are two types of variables,
1. Local variable: These are present inside the function.
2. Global variable: Which are present outside the function.



Scope of a particular variable is defined by use of LEGB rule:

This is the order which python follow for using the value of a variable,
For example: python wants to use the value in a function then
L: Local: First it checks whether is any local variable in the function named a and if it is there then it would be given first preference.
E: Enclosing: If local variable absent, then python would check whether there is a variable in enclosing function and if it is there then it would be given the preference.
G: Global: If there is also no variable in enclosing function, then python would check whether there is a global variable and if it is there then it would  be given the preference.
B: Built-in: If non of the above variables are present then python would check is there any in-built function or names pre-assigned and if there is then it would be used.
'''

'''
Examples:
'''

a = 10 # This is Global Variable.
print("Outside",a)

def something():
    a = 5 # This is local variable
    b = 6# This is local variable.
    print("Inside", a,b)


something()

# Some points.
'''1. You can use global variable inside the function, if local variable is absent.'''
print("  ")
c = 5
def some():
    print("Inside",c)

some()

print("outside", c)

'''2.But if there is a local variable, inside the function, then the local variable will be given preference.'''
print(" ")
c = 5
def some():
    c =10
    print("Inside",c)

some()

print("outside", c)
print("")
'''
if there is enclosing variable, then
'''
b= 10
def greet():
    b = 7 # here as b is a variable in the enclosing function thus,it would be given preference over global variable.
    def say():
        print("hello", b)

    say()

greet()
print('')





'''3.To make a local variable, you need to write it explicitly'''
print(" ")

d =100
def same():
    global d
    d = 14
    print("Inside", d)

same()
print("outside",d)


'''
Globals: To use both local and global variables, inside the python.
We use the concept of globals.
'''
print(" ")
print("  ")
p = 10
print(id(p))
def samething():
    p = 8
    x = globals()['p']# if you will not use the square brackets, then it will give all the global variables.
    print(id(x))
    print(x)
    print("inside", p)
    globals()['p'] = 12
    print(globals()['p'])



samething()

print("outside", p)
#Thus we have a local variable p and global variable p inside the same function.

'''
You cannot set parameter as global variable:
                                                   Ex:
                                                   a = 9
                                                   def hi(a)
                                                     global a # This is wrong as a is parameter so you cannnot change it's value.
                                                     a = 7
                                                     print(a)
                                                   hi(a)

'''
