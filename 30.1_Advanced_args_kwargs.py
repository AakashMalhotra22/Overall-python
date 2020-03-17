def myfunc(*arg,**kwargs):
   print(arg)
   print(kwargs)
   print(f"I would like to {arg[0]} {kwargs['fruit']}")

myfunc(1,2,3,4, fruit = "apple")