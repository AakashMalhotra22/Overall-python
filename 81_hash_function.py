'''
Hashable: un mutable
unhashable: mutable
1. Hash function: 1. It is a mathematical function which converts an input value into a compressed numerical value
                  2. It converts only hashable objects(un mutable).
                  3. The values returns by the hash functions are called hash values or hash codes.
                  4. It can be used to check whether a object is mutable or not.
'''

#Example:
y =2
y1 = "ram"
y2 = 3.123
y3 =(1,2,3,4)
print(hash(y))
print(hash(y1))
print(hash(y2))
print(hash(y3))

print("")
try:
    print(hash([1,2,3,4]))
except:
    print("un mutable")