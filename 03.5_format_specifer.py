'''
%s is a format specifier, quite same as string formatting.
syntax:
print("ram is %s boy." %(object you want to replace by %s)


'''

#1

x =10
print("ram is %s" % x)
print('ram is "%s"' % x)

#2
x = [1,2,3,4,5]
y = [5,6,7,8]
z ="bye"

print("ram is %s"%x)
print("ram is %s"%x,y,z)

print("")
#3
print("Aakash is %s boy."%"strong")