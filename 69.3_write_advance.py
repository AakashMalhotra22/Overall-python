y = open("l1.jpg","rb")# rb means in binary format

#Now to save this data of y in other file:

y2 = open("l4.jpg","wb")
for i in y:
  y2.write(i)