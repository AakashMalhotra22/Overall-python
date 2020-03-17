t = [0,1,2]
t.extend([])
print(t)
t.append([[]])
print(t)
print(len(t))


s = "bed and breakfast"
print(s.find('bed')==False)


y = [3,2,1]
print(sorted(y))
print((y.pop()))
print(y)

y = tuple("rsj")
y = tuple([1,2,3])
y = tuple({'a':2, 'b':3})
y = tuple({1,2,3})
print(y)



y = ("a", 2, False, 3.2, "2", None)
print(y)


y = (4,1,2,3)

print(y[1:3])










s = {1,2,3,2}
print(s)
print(len(s))
