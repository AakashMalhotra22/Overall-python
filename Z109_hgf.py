class A:

    def __init__(self): # Constructor
        print("in A init")

class B(A):
    def __init__(self): # Constructor
        print("in B init")

a1 = B() # It is calling the constructor of B.
print("  ")
# IF you want to call the constructor of A inspite of having constructor in B. then use super.


class A:

    def __init__(self): # Constructor
        print("in A init")

class B(A):
    def __init__(self): # Constructor
        super().__init__()
        print("in B init")

a1 = B() # It is calling the constructor of A.
