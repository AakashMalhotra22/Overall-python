
'''Type-1'''

#Way-1
print("####")
print("####")
print("####")
print("####")

#Way-2
print("                                                 ")
for i in range(4):
    print("#", end ="")
print("")
for i in range(4):
    print("#", end ="")
print("")
for i in range(4):
    print("#", end ="")
print("")
for i in range(4):
    print("#", end ="")


#Way -3
print("                      ")
print("                     ")

for i in range(4):
    print("")
    for i in range(4):
        print("#", end = "")



#Shortcut, use TAB button to add in a loop

''' Type-2 '''

#Print this type of pattern
#
##
###
####

#lWay-1

print("                    ")
print("                ")
r =1
while r <=4:
   print(r*"#")
   r += 1

#Way-2
print("                 ")
print("                 ")

for i in range(4):
    for j in range(i+1):
        print("#", end= "")
    print("")


'''Type -3'''
####
###
##
#


#Way -1
print("    ")

r = 4
while r>=0:
    print(r*"#", end = "")
    r-=1
#Way-2

print("          ")
print("          ")

for i in range(4):
    print(" ")
    for r in range(4-i):
        print("#", end = "")

#Way -3

print("           ")
print("           ")

for r in range(4,0,-1):
        print(r*"#", end = "")
        print("")
