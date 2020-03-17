#Array: It is a type of list but having same type of elements, either string, number or bullien.

#signed means all the values from negative to positive.
# unsigned means all the values from 0 to positive.

'''
Type code  |    C Type       |Python Type          |Min.size in bytes
  'h'        signed short       int                     2
  'H'        unsigned short     int                     2
  'i'         signed int        int                     2
  'I'         unsigned int      int                     2
  'l'         signed long       int                     4
  'L'         unsigned long     int                     4
  'f'          float            float                   8
  'd'          double           float                   8
  'b'         signed char        int                    1
  'B'         unsigned char      int                    1
  'u'         Py_UNICODE        unicode character       2


'''

#2. Operations
from array import*

vals = array('i', [5,6,4,3])

print(vals)

print(vals.buffer_info())
print(vals.typecode)

vals.reverse()
print(vals)

print(vals[0])

for i in range(4):
    print(vals[i])

for i in vals:
    print(i)


print("               ")

#3. unicode - unique code

ram = array('u', ['i','e','s'])

print(ram)

#4. New array formation:
print("                ")

r = array('i', [3,4,5,6])

newarray = array(r.typecode, [a for a in r])
print(newarray)

newarray1 = array(r.typecode, [a*a for a in r])
print(newarray1)

i = 0
while i<= len(newarray):
        print(newarray[i-1])
        i += 1
