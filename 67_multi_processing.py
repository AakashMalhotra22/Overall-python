'''
Multi Processing:
1. Multi processing refers to the ability of the system to support more than one processor at the same time(concurrently).
   For example:
   Using Micrsoft word, vlc player, etc at the same time.

2. A multiprocessing can have:
   1. multiprocessor- i.e a computer with more than one processor.
   2. multi-core processor- single computing components with two or more independent actual processing units(called cores.)

3. In multiprocessing, each process runs independently and has its own memory space unlike multithreading.

4. It also helps the computer to operate faster.

5. In this all the programs runs in true parallel.
'''

#Examplle:

'''
In this, we will consider the second way to create threads.
'''
from multiprocessing import*
from time import*

def ram(n):
    for i in range(n):
        print("ram", end="")
        sleep(1)

def ji(n):
    for i in range(n):
        print("ji")
        sleep(1)

if __name__ =="__main__":#This is neccessary here.
    y1 = Process(target = ram, args = (3,))#This is the way of passing the argument.
    y2 = Process(target = ji, args = (3,))

    y1.start()
    sleep(0.1)
    y2.start()

    y1.join()# It will make sure, unless y1 is completed, current program will not start.
    y2.join()# It will make sure, unless y2 is completed, current program will not start.

    print("bye bye")# This is main method.
