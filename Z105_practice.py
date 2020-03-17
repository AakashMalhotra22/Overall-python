i = {1,2,3}

it = iter(i)

print(it.__next__())
print(it.__next__())
print(it.__next__())


class super3:

    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):

        if self.num < 4:
           values = self.num
           self.num +=1
           return values


        else:
            raise StopIteration



aaka = super3()

print(next(aaka))
print(next(aaka))

for i in aaka:
    print(i)
        