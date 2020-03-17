#There are two types  of arguments:
#1. Formal argument
#2. Actual Argument

#Example

def person(name, age):# Here name and age are formal arguments.
    print(name)
    print(age)

person("Aakash", 23) #here Aakash and 23 are actual arguments.

'''There are four types of Actual Arguments.
1. Position Argument.
2. Keyword argument
3. Default Argument
4. Variable length Argument
'''

# 1. Position

def person(name, age):
    print(name)
    print(age)


person("Aakash", 23)  #Here Aakash goes in place of name and 23 will go in place of age,if you change the position, the result will
# also change.


print("")
#2. keyword argument
#In this we assign the values

def person(name, age):
    print(name)
    print(age)


person(age = 28, name = "ram")
print("")
#3 Default:

def person(name, age=18): # In this we have assigned a default value to age,
    print(name)
    print(age)


person("Aakash") # Here I have not written age, so it will by default take 18as age.
person("ram", 20) # In this I have taken the age, it will choose 20 over 18 as age.

print("")



print("")
#4 Variable list Argument

def sum(a,b):
    c = a+b
    print(c)

sum(5,6) #Here you can only add 2 numbers, but we want to add many values, to do use we use variable list argument.

#
def sum(a,*b): # this * means, b can have many values
    print(b) # it would be in form of tuple
    c = a

    for i in b:
        c = c+i
    print(c)

sum(5,6,3,4,5) # Here a is 5 and b is 6,3,4,5.

