'''
file Handling:
1. It is used to open a file from one file and to do changes in it.
2. There are three basic function available in it.
   a. read  b. write  c. append d. read and write

3. The three modes are:

   reading mode- Denoted by r, means only read the file, dont want to do the changes.
   writing mode-  denoted by w, means you can change the file.
   appending mode- denoted by a, means you can append some changes, but cant do changes.
   reading and writing- denoted by r+, provide all powers of reading and writing
'''

'''
Reading files
Few functions:
1. print(y1.read())    2. print(y1.readable())  3. print(y1.readline())   4. print(y1.readlines())

'''

#Example-1

y1 = open("read1.py", "r")# This is open and takes two argument-file name and mode.

print(y1.readable()) # To check whether the file is readable or not.

y1.close() # This is use to close the file, and make sure you close the file after opening, it avoids chances of error.

print("")
#Example-2

y2 = open("read1.py", "r")

print(y2.read())# prints out what is written in it.

y2.close()

print("")
# Example-3

y3 = open("read1.py", "r")

print(y3.readline())# print out first line of the other file.
print(y3.readline())#print out the second line of the other file with one line gap.
y3.close()

print("")
# Example-4

y4 = open("read1.py", "r")

print(y4.readlines()) # prints out all the code in one list.

y4.close()

print("")
# Example-5

y5 = open("read1.py", "r")

print(y5.readlines()[1])# prints out the first line of the other file.

y5.close()

print("")
print("")
print("")
# Example-6

y6 = open("read1.py", "r")

for i in y6:
    print(i)

y6.close()
