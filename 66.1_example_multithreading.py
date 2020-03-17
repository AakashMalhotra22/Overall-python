'''
In this, we will consider the second way to create threads.
'''
from threading import*
from time import*

def ram(n):
    for i in range(n):
        print("ram", end="")
        sleep(1)

def ji(n):
    for i in range(n):
        print("ji")
        sleep(1)

y1 = Thread(target = ram, args = (3,))#This is the way of passing the argument.
y2 = Thread(target = ji, args = (3,))

y1.start()
sleep(0.1)
y2.start()

y1.join()
y2.join()

print("bye bye")# This is main method.