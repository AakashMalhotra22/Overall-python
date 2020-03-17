def pow(a,b):
    print(a**b)


def smart(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

pow = smart(pow)

pow(2,3)



