'''
Comparison Operators:
1. ==
2. !=
3. >=
4. <=
5. <
6. >
Points to remember at the time of comparison operators.
1. == sign is used and not = sign because = is used for variable assignment.
2. Upper and lowercase matters at the time of comparison
   print('ask'=='Ask') output would be False.
3. Datatypes also matters, ex print('2'==2) is False.
4. 2.0 == 2 is true.
5. You can compare any datatypes.
6. Sequence matters at the time of comparison.
   print([1,2]==[2,1]) output is False.
'''

'''
Index
1. Basic use of operators.
2. Comparison between the datatypes.
3. Some other concepts.

'''


'''
1. Basic use of operators
'''

a =5
b = 6
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

print("")
'''
2. Comparison between the class object such as list, dict, tuple, range, string, sets, float, int, bool,None
'''

print([1,2]==[1,2]) # Comparing class list objects
print({1:'a', 2: 'b'}=={1:'a', 2: 'b'}) # Comparing the dict class object
print((1,2)==(1,2))# Comparing tuple class object
print({98,2}=={98,2}) # Comparing set class object
print("ask" == "aakash") #Comparing string class object.
print(range(0,10) == range(0,9)) # Comparing range class object


print("")
'''
3. Some other concepts
'''

print(2==[1,2])
print(3=="ask")
print("Ask" == "ask") # upper and lower case matters
print((1,2)==(2,1)) # sequence matters
print(1 == True)

print(" ")
print(1<2<3)
print(1>2<3)
print(1<3>2)
