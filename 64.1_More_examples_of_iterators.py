'''Examples of creating iterators by use of class'''

# 1.

class toptensquare:

    def __init__(self):
        self.m1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.m1<=10:
            v = self.m1*self.m1
            self.m1+=1
            return (v)
        else:
            raise StopIteration

it = toptensquare()
print(it.__next__())
for i in it:
    print(i)

print('')
#2.

class userinfo:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __iter__(self):
        return self
    def __next__(self):

        if self.m1<=100:
            value = self.m1 +self.m2
            self.m1+= 10
            return value
        else:
            raise StopIteration

it = userinfo(5,2)

for i in it:
    print(i)