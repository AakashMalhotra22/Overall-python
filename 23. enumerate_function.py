'''
enumerate function:
1. It takes any iterable object and returns the index position and the element at that index position
'''

'''basic to advance'''

#1.

name = "Aakash"
for item in enumerate(name):
    print(item)
#Here enumerate prints the index position and the alphabet at that index position in the form of tuple.
print(" ")

#2.
for index, letter in enumerate(name):
    print(f"{index} \n{letter}\n")

#Here enumerate prints the index position and the alphabet at that index position in the form of tuple.
print(" ")

