'''
break, continue and pass
1. break:    a. breaks out of the current closest enclosing loop.
             b. It will close the loop when the certain condition occurs.

2. continue: a. Go to the top of the closest enclosing loop.
             b. it skips the particular statement.
             c. If you dont want to print the output when this condition approaches.

3. pass      a. Does nothing at all
             b. means this is not valid, pass it to else without giving any output in if.

'''

available  = 4
x = int(input("How many candies do you want? "))

i =1
while i<=x:

    if i >= available:
        print("Out of stock")
        break

    print("Candy")
    i +=1

print("Get out")

#2. continue: It skip the statements, it does not close the loop.

# Ist way by use of continue.[Calculation of numbers from 0 to 10 which are not divisible by 3 and 5]
print("              ")

for i in range (1,11):

    if i%5 == 0 or i%3 == 0:
        continue
    print(i)

# 2nd way own style
print("              ")

for i in range (1,11):

    if i%5 != 0 and i%3 != 0:
        print(i)

# 3 pass: means this is not valid, pass it to else without giving any output in if.
print("              ")
for i in range(1,10):
    if i%2!= 0:
        pass
    else:
        print(i)

print(" ")
for i in range(10):
    pass
