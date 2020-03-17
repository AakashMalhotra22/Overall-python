'''
regular expressions:
1. search(a,b) #for searching the whether the first argument lies in second string or not.
2. split(a,b) # The string b is split through the string a.
3. findall(a,b) # It will find all the elements a in b.
4.

'''
from re import*

# Checking for patterns
'''
It wil check whether the first argument lies in the second argument or not.
'''

print(search("ram", "ram is a boy"))
print(search("ram", "shyam"))

print()

patterns = ['term1', 'term2']
text = "This has term1 but not the other term"

for i in patterns:
    print("checking for '%s' element in the string '%s'."%(i,text))

    if search(i,text):
        print("Match is found.\n")
    else:
        print("Match is not found. \n")



y1 = 'ahuja'
y2 = 'this is tanu ahuja'
z = (search(y1,y2))

print(z.start())# starting index of common element.
print(z.end()) # ending index of common element.

print(1*"\n")

#2
'''
split method
'''

y1 = "@"
y2  ="aakashmalhotra28632@gmail.com"

print(split(y1,y2))
print()
#3
'''findall- gives you list of all the matches'''
print(findall("ram", "ram ram ram ram 1, ram ji is a god."))
print()

