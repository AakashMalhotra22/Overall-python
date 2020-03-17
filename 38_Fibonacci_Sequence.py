

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2, n):
       c = a+b
       a = b
       b = c
       print(c)

fib(int(input("Tell the length of the fibonacci sequence: ")))
print("  ")
# if you want the first number only:

def fib(n):
    a = 0
    b = 1
    if n == 1:
       print(a)

    else:
      print(a)
      print(b)

      for i in range(2, n):
         c = a+b
         a = b
         b =c
         print(c)

fib(int(input("Tell the length of the fibonacci sequence: ")))


# To avoid negative numbers:
def fib(n):
    a = 0
    b = 1
    if n == 1:
       print(a)

    elif n == 0:
        pass

    elif n< 0:
        print("Invalid input.")



    else:
      print(a)
      print(b)

      for i in range(2, n):
         c = a+b
         a = b
         b =c
         print(c)

fib(int(input("Tell the length of the fibonacci sequence: ")))

