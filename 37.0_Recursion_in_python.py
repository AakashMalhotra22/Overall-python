# Use of same function inside a function is known as recurssion.
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

i =0
def greed():
    global i # by using of global, the value of i will change for everthing, not for this, thus when again this fn executed, the value will be different.
    i += 1

    print("hello",i)

    greed()

greed()

