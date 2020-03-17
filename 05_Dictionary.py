'''
Dictionaries:
1. Dictionary is a mapping of unique and hashable keys to values.
2. Dictionaries are mutable and unordered collection of key-value pairs.
3. Unordered collection of values means that it cannot be sliced, indexed and sorted unlike lists and strings.
4. In dictionaries the objects are retrieved by the key names not by the index number that means you need not to learn the index positions.
5. These are iterables.
6. dictionaries are unordered so if you iterate through it by use of for loops, then the order in the output may be different as the order in the input.
'''

'''
Index
1. Ways to create dictionaries.
2. Basics operations on dictionaries.
3. Nested dictionaries.
4. Errors in dictionaries.
5. Dictionaries comprehesion
'''


#Ways to create dictionaries
'''
There are two ways to create the dictionaries:
1. By use of curly braces and writing the keys and values.
2. By use of dict() method
   a. List, strings, tuples, sets cannot be converted into the dictionaries directly.
   b. int, float, None cannot be converted into the dictionary because they are not iterable.
'''

print(" ")
#Ist way
r = {"navin":"Iphone", "aakash": "samsung"}
print(r)

#2nd way

y = dict(a= 8, b =7)
print(y)

y2 = dict({"m":8, "n":7} )
print(y2)

print(" ")

# 3rd way:
y = [1,2,3]
z = [4,5,6]
print(dict(zip(y,z)))

print(" ")

'''
Methods in dictionaries
'''

#1.
r = {"navin":"Iphone", "aakash": "samsung"}

print(r) # return the dictionary
print(r.keys()) # give all the keys
print(r.values()) # give all the values
print(r["navin"]) # calling the value through its key.
print("")
print(r.get("navin"))
print(r.get("dda", "not a valid key")) # The use .get is that if that key is not present in that then it would print "not a valid key".

print("")

#2 Add value to dictionary

y = {"phone": "nokia", "cycle": "atlas", "love": "mom"}


y["childhood"] = "pados" # since there is no key named 'childhood", it would create new key named childhood.

print(y)
print("")
#3 Remove the value and its key.

del y["phone"]

print(y)
print("")
#4check the length

print(len(y))
print("")

#4 Print all key and values

for key, val in y.items():
    print(key , "=" ,val)
print("")

'''3. Flexiblity of dicitionary and nested dictionaries'''

d = {"k1":123, "k2": [1,2,3], "k3" : dict(a=3, b =4), "k4":{1:"aakash", "r2": "ram"}}
print(d)

print(" ")
print(d["k2"][2])
print(d["k4"]["r2"])
print(d["k4"][1])



'''4. Errors in dictionaries'''
'''
1. Key Error
                  1. It means key does not exist.
                  2. Python raises this error whenever a dict() object is requested (using the format a = dict[key])
                     and the key is not in the dict.
                  3. It generally means you have put the wrong key which does not exist and now python cannot get the value
                      for that key from the dictionary.
                  Example:
                  a = {"name": "ram"}
                  print(a[0]) and since 0 is not a key in the dictionary so it will give key word error.

                  4. key word error means or comes when you try to call a dictionary object using a key which does not exist.
                  



'''
print("")

'''
5. Dictionaries comprehension:
'''


y = {x:x*x for x in range(0,3)}
print(y)

z = {k:y for k,y in zip([1,2,3], range(0,3))}
print(z)
