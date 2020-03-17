'''Two most common ways of tuple unpacking'''
#Example-1

y = (1,2,3)
(r, a, m) =y

print(r)
print(a)
print(m)
'''
In tuple unpacking, make sure that numbers of variables must be equal to the number of variables on the left.
'''
print()
#Example-2
'''
By use of *args
'''
a,*b,c =(1,2,3,4,5)
print(a)
print(b)
print(c)
print()
#or
a,b,*c =(1,2,3,4,5)
print(a)
print(b)
print(c)
