'''Advance example of default keyword'''

b = [10,20]

def sum(a,c =b): # here the default value of c is [10,20] and it would not change even you write b = [1,2] even after the function.
    y = 0
    for i in c:
        y+=i
    print(a+y)


b = [1,2]

sum(10)
print('')
# same example for int


b = 2

def sum(a,c =b): # here the default value of c is  2 and it would not change even you write b = 20 even after the function.

    print(a+c)


b = 30

sum(10)
