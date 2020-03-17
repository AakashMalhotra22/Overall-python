'''
Decorators in python:
1. It is a design pattern in python that allows a user to add new functionality to an existing function without modifying its structure.
2. These are called before the definition of a function, you want to decorate.
3. They use the @ operator and are then placed on top of the original function.
4. Mostly used in Django and flask for web developement.
'''

def smart(func):

    def inner(a,b):
             if a<b:
                 a,b = b,a
             func(a,b)
    return inner


@smart# This will pass the below shown function in smart function.
def div(a,b):
    print(a/b)

y = div(2,4)#here 2,4 parameters is passed to inner function in place of a,b

'''
What's happening behind the scenes.
1.@smart decorators passes the div function to smart function, now the smart function becomes.
  def smart(div):

    def inner(a,b):
             if a<b:
                 a,b = b,a
             div(a,b)
    return inner

2. Now when you write y = div(2,4), it means you are writing y =smart(div)(2,4) and this two parameters 2,4 are passed to the inner(a,b) function.
'''

#You can also use decorators like this.

def div(a,b):
    print(a/b)
y = smart(div)(2,4)#Here div parameter is passed to the smart function and (2,4) is passed to inner function
#or
y = smart(div)
y(2,4)