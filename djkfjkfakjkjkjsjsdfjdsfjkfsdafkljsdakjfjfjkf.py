'''
%s- All datatypes.
%r- All datatypes, but return as it is, like in case of string, output contains colons.
%d - All numbers but output is in whole numbers.
%f- All numbers but output is in floating points to 6 decimal places

'''

#1 string:
print("ram is a %s boy"% ("ram"))
print("ram is a %r boy"% ("ram"))
#print("ram is a %f boy"% ("ram")) - Error
#print("ram is a %d boy"% ("ram")) - Erro

print("")

#2 int numbers:
print("ram has %s boy"% (12))
print("ram has %r boy"% (12))
print("ram has %f boy"% (12))
print("ram has %d boy"% (12))

print()
#3 float
print("ram has %s boy"% (12.12))
print("ram has %r boy"% (12.12))
print("ram has %f boy"% (12.12112))
print("ram has %d boy"% (12.1221))

print()
#4 complex
print("ram has %s boy"% (2+3j))
print("ram has %r boy"% (2+3j))
#print("ram has %f boy"% (2+3j)) - Error cant convert complex to float.
#print("ram has %d boy"% (2+3j)) - Error only take numbers

print()
#5 list
print("ram has %s boy"% ([1,2,3,4]))
print("ram has %r boy"% ([1,2,3,4]))
#print("ram has %f boy"% (2+3j)) - Error
#print("ram has %d boy"% (2+3j)) - Error


print()
#6 dict
print("ram has %s boy"% ({'a':2,'b':2}))
print("ram has %r boy"% ({'a':2,'b':2}))
#print("ram has %f boy"% (2+3j)) - Error
#print("ram has %d boy"% (2+3j)) - Error


print()
#7 tuple


#print("ram has %s boy"% ((1,2,3))) - error - cant pass so many arguments
#print("ram has %r boy"% ((1,2,3))) -error - cant pass so many argument
#print("ram has %f boy"% (2+3j)) - Error
#print("ram has %d boy"% (2+3j)) - Error


print()
#8 set

print("ram has %s boy"% ({1,2,3}))
print("ram has %r boy"% ({1,2,3}))
#print("ram has %f boy"% (2+3j)) - Error
#print("ram has %d boy"% (2+3j)) - Error

print()
#9 bool

print("ram has %s boy"% (False))
print("ram has %r boy"% (False))
print("ram has %f boy"% (False))
print("ram has %d boy"% (False))

print()
#10 range

print("ram has %s boy"% (range(0,10)))
print("ram has %r boy"% (range(0,10)))
#print("ram has %f boy"% (range(0,10)))-Error
#print("ram has %d boy"% (range(0,10)))-Error
