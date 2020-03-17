# Summarize in one line.
'''
try:
   #do something.
except:
    # error then print this.
'''
'''
Errors:
1. Types of Error:
    a. Compile Error: 1. When you do syntax mistakes. These are called syntactical Errors
                      2. Easy to find errors.

    b. Logical Error: 1. When you don't get correct output, for example you give 2+2, and you get 3. This is logical errors.
                      2. Occurs because of wrong logic.
                      2. Easy to find errors.

    c. Run time:      1. When you don't get output, in spite of your output gets compiled and also there are no logical errors,
                        Ex: divide by zero
                      2. These types of errors are done by users as you are getting input from users
                      3. Difficult to find.

2. To deal with the errors you can use try,except and finally.

3. Syntax
      try:
        #write your code
     except:
        #write here what to print when you get an error
     else:
         #if you don't get an error then the statement which you are writing in the else will be print, otherwise if you
          get an error then it would not print.
     finally:
          #it would print out what finally you want to print at the end.
In the above syntax, you have to write try: and except:, else: and finally: can be skipped.
'''
'''
Examples:
'''
# Example1
a = 2
b=0
try:
    print(a/b)
except Exception:
    print("Hey, you cannot divide a number by zero.")

else:# this will only be executed when there is no error.
    print("bye")

finally:
    print("here code ends.")

print("")

# Example 2:
'''
 When you also want to find the error.
'''

a = 3
b =0

try:
    print(a/b)
except Exception as e:
    print("Hey, you cannot divide a number by zero.", e)

else:
    print("bye")

finally:
    print("here code ends.")

print(" ")

#Example-3
'''
try and except are necessary, else and finally can be skipped.
'''
p = "a"
try:
    print(2+p)
except:
    print(4)

print("")

#Example-4

try:
    k = int(input("Enter a number: "))
    print(k)
except ValueError as e:# It would only be executed if there is only value error.
    print("Invalid input,", e)

except Exception:
    print("Something went wrong...")

finally:
    print("Here code ends.")
print(" ")


#Example-5
'''
Always, make try and except block for each line of code you doubt can be wrong.
'''

def func():
    n = 'sakjfajsf'
    try:
        print(2+n)# I am in doubt that it may be wrong.
        print("ram")# This line of code would not execute if the above code line has an error, so its better to write it separately.
    except:
         print("koi nhi aage bhdo.")

    print("ram")
    print("3+4")
    #In above two codes of line, i am sure that it would not be wrong, so i have not used try and except in above case.

func()
