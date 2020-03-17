'''
for loops:
1. These are used to iterate through the iterator.
2. It can be applied only on the objects of the iterables.
3. Example of iterable objects: str, list, dict, tuple, set, range
4. Examples of non-iterable objects: int, float, boolean, None

  syntax of for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
      print(item_name)

5. dictionaries are unordered so if you iterate through it by use of for loops, then the order in the output may be different as the order in the input.
'''

'''
Basics to advance:
'''

#1. list

x = ["navin", 23, True]

for i in x:
    print(i)
print("")

#2. strings

y = "Navin"

for i in y:
    print(i)

print("")

#3. range

for i in range(len(x)):
    print(i)

print("")

for i in range(1,10,2):
    print(i)
print("")
for i in range(1,10):
    print(i)

print('')# use of end
for i in range(11,20,1):
    print(i, end ="")

print("")
print("")
for i in range(1,21):
    if i%5 == 0:
        print(i)
print("")


#4 Even odd function

l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

print('')

# 5
l = [1,2,3,4,5,6,7,8,9,10]
list_sum =0
for i in l:
    list_sum = list_sum + i
print(list_sum)

print("")
# 6

l = [1,2,3,4,5,6,7,8,9,10]
list_sum =0
for i in l:
    list_sum = list_sum + i
    print(list_sum)

print("")


#7 tuple iteration

tup = (1,2,3)

for item in tup:
    print(item)

print("")

#8 tuple unpackaging

l = [(1,2), (3,4), (5,6)]
for a,b in l:
    print(a)
    print(b)
print("")

#9. dictionary

d = {"k":1, "k2":2}
for item in d:
    print(item)
print("")

for item in d.items():
    print(item)

print("")
for key, item in d.items():
    print(key)
    print(item)

