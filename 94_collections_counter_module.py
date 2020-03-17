'''
1. Counter is one of the function of collections module.
2. Counter is dictionary subclass which counts hashable(unmuttable) objects.
3. The output is in the form of dictionary.
'''

from collections import Counter
#Counter:
'''
It counts the occurrences of hashable objects(un mutable objects) in the iterable data types such aslist/tuple/set/string/set. 
'''
#1
y = [1,2,2,3,2,1,2,3,1,2,3,12,2,1,3,1,2,23,1,2,2,21,23,211,211]
print(Counter(y))

#2
s= "ramdfsdfjksalk"
print(Counter(s))

#3
'''Count each word in a sentence.'''
y= "ram is good boy and he is known for his power."

word = y.split()
print(Counter(word))

print(2*'\n')
#Methods of Counter
'''
1. most_common()
'''

y =["ram", "ram", 'shyam', "ask", 'ram', "aakash"]
y1 = Counter(y)
print(y1.most_common(2))# It will tell 2 most coomon words in y