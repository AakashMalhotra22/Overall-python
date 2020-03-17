a = 10
def samething():
    global a

    a = 90
    print(a)
    a = 15
    print(a)

samething()

print(a)

print("")
print("")
print("")
print("")

d = 25

def aakash():
    x = globals()['d']
    globals()['d'] = 87
    print(globals()['d'])
    d = 177
    print(d)

aakash()
print(d)