'''
While loops:
1. While loops will continue to execute a block of code while some condition remains True.
   For example:
   while my pool is not full, keep filling my pool with water.

2. Three important things in while loop.
   1. Intialization or variable
   2. condition
   3. Increment or decrement

3. Syntax of a while loop
   while some_boolean_condition:
         do something

4. while else
   while some_boolean_condition:
         do something
   else:
         do something different
'''

'''
Basics to advance
'''

# 1.

i = 1          # Intialization variable
while i<=5:    # condition
   print("aakash", i)
   i+=1        # Increament

print(" ")

#2. While else

x = 0
while x<5:
    print(f"The current value is {x}")
    x+=1
else:
    print(f"{x} is not less than 5")

print("")


#3 Nested while loops
#1
i = 1
j = 1
while i <=5:
    print('aakash')

    while j<=5:
        print("don")
        j+=1
    i += 1

#You can write the condition of first while loop in case of nested while loops in the end.
#2
print("                                                      ")
i = 1
j = 1
while i <=5:
    print(' aakash', end ="")

    while j<=5:
        print(" don", end = "")
        j+=1
    i += 1

print("")
print("  ")
#3 The condition of nested loops should be in nested loop only
i = 1
j = 1
while i <=5:
    print(' aakash', end ="")
    i+=1
    while j<=5:
        print(" don", end = "")
        j+=1
    print("")

print("      ")
print("      ")

#4

i = 1

while i <=5:
    print('aakash', end ="")
    i+=1
    j = 1
    while j<=5:
        print(" don", end = "")
        j+=1
    print("")
