'''
for else:
1. If there is no output from the for statement then it passes to else statement to give the output

'''

#Type-1'''
'''When we want all the numbers in the list which are divisible by 5.'''

nums = [12,15,18,21,26,30,35]

for i in nums:
    if i%5 ==0:
        print(i)

#Type-2
'''When we want only the first numbers in the list which are divisible by 5.'''

print("                                     ")
nums = [12,15,18,21,26,30,35]

for i in nums:
    if i%5 ==0:
        print(i)
        break
#Type-3 if the list doesnot have any number which is divisible by 5, then the output is nothing, but we want to print "not found"

nums = [9,16,9,21,26,31,12]

print("              ")
for i in nums:
    if i%5 ==0:
        print(i)
        break

else:
        print("not found")

