'''
Multi threading:
1. When you divide a big task into multiple small parts then these small parts are called threads.
2. Multiple threading is defined as the ability of the processor to execute multiple threads at the same time
   (concurrently).
   Example:
   When you are using office word, then at the same time, typing function, grammar check function, spell check function
   takes place, these all are threads and the main thread is office word.
                                  Office_Word(Main Thread)
   a. typing function(Thread)  b. grammar check function(Thread)  c. spell check function(Thread)

3. All the threads and the main threads run in the same memory space unlike multi processing.
4. The use of multi threading is that the work load is distributed, and the program works faster.
   Ex: A chef(main_thread) is making a dish with the help of its assistance(threads).

5. You can check the thread in your computer in task manager.
6. More software you run at a time, more thread you will get.

7. Context Switching
   Now the twist is that, all the thread not run in parallel, but switching between the threads take place.
   first one thread runs, and once it stops, its state is saved and then another thread starts running, and then state
   is saved, and this switching takes place so frequently that all the threads appears to run parallel.
   This is known as context switching.

8. In multi threading, the threads seems to run concurrently but usually not run concurrently, threads just switch between
   each other.
   In multi processing, the programs run concurrently

9. Now, how does it works in coding:
   When you run a code, the code is run by a thread that is the "main thread".

  If you want to execute two codes, you can execute them in by two different threads.
  so there will be three threads
  main thread
  first thread
  second thread

'''
#Example-1
'''
Making two classes Threads
'''

from threading import* # it is required to import threading
from time import * # It is required to use sleep

class hello(Thread):
    def run(self):#Here you have to use run method for threads in the class.
      for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):# Here you have to use run method for threads in the class.

      for i in range(5):
              print("hi")
              sleep(1)


t1 = hello()
t2 = hi()

t1.start()# This start is actually calling the run method.
sleep(0.2)
t2.start()# This start is actually calling the run method.

t1.join()# This ensures that unless the t1 is completed executed, print("bye") will not excecute.
t2. join() # This ensues that unless the t2 is completed, print("bye") will not execute

print("bye")
'''
If you don't use sleep, then there is a probability that both the threads may collide means run at a same time, which
will cause unpredictable output.
'''