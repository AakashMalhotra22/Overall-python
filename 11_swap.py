a = 5
b = 6

a = b
b = a

print(a)
print(b)

#1 By use of third variable

a = 4
b = 5
temp = a
a = b
b = temp

print(a)
print(b)
#Demerit of this method is you are wasting one extra variable.

#2 By use of formula

a = 7
b = 6

a = a +b  # 13
b = a -b  # 7
a = a - b # 6

print(a)
print(b)

#Demerit of #2 is that you are wasting one extra bit


#3 By use of excort symbol or cap symbol
'''Advantages:It doesnot use extra variable and extra bit.
'''
a = 8
b =9
a = a^b
b = a^b
a = a^b

print(a)
print(b)

#4 Two rotation, Stack, rot two.

x = 3
y =4

x,y = y,x # These things do not work in two different lines, but do wok in one line

print(x)
print(y)