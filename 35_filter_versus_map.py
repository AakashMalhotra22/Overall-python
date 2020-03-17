
#1
yf = list(filter(lambda a: a%2 ==0, [1,2,3,4,5,6])) # even function filter
print(yf)

ym = list(map(lambda a: a%2 ==0, [1,2,3,4,5,6]))# applies the operation on each element of list.
print(ym)

print("")

#2
yf = list(filter(lambda a: a%2, [1,2,3,4,5,6])) # odd function filter
print(yf)

ym = list(map(lambda a: a%2, [1,2,3,4,5,6]))# applies the operation on each element of list.
print(ym)

print("")

#3
yf = list(filter(lambda a: a+2, [1,2,3,4,5,6])) # Those values in the list which has that plus 2 exist
print(yf)

ym = list(map(lambda a: a+2, [1,2,3,4,5,6]))# applies the operation on each element of list.
print(ym)

print("")

#4
yf = list(filter(lambda a: a*a, [1,2,3,4,5,6])) # Those values in the list whose square exist.
print(yf)

ym = list(map(lambda a: a*a, [1,2,3,4,5,6]))# applies the operation on each element of list.
print(ym)
