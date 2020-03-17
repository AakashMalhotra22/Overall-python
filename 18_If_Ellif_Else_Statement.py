'''
There are three statements:
1) if,
2) elif
3) else:

Points:
1. This statements uses colons and indentation.
   Indentation: Certain number of white spaces are known as indentation:

2. The indentation system is crucial to python and is what sets it apat from other programming languages.
3. Indentation makes the code easier to read
'''

'''Basics to Advance'''

if True:
    print("Is right")
    print("bye")


if False:
    print("hello")

print("")
hungry = False

if hungry:
    print("Feed me")
else:
    print("I am not hungry")


print("")


#Nested if

x = 34
r = x%2
if r == 0:
    print("Even")
    if x >= 5:
        print("Good")
    else:
        print("NOT GOOD")
else:
    print("Odd")

# if (x==1): or if x==1: are same
