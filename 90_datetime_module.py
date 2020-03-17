'''
datetime module:
Three important functions
1. datetime
2. date
3. time
'''

from datetime import *

#1 datetime
y = datetime(2020,3,17,8,23,12)#order y-m-date-hour-min-sec

#further options
print(y)
print(y.time())
print(y.date())
print(y.hour)
print(y.minute)

print("")
#Replacing:
print(y.replace(year=2021))

print("")
#Calling today
print(y.today())


print(1*'\n')

#2 for only date

y = date(2019,1,12)
print(y)
print(y.day)
print(y.month)

#for replace
print(y.replace(year=2020))

#for today
print(y.today())







print(1*"\n")
#3 for only time

y = time(20,1,12)#order- hour,minute,second
print(y)
print(y.second)
print(y.minute)
print(y.hour)

print("")
#Other functions of time
print(y.resolution)
print(y.min) #to print min time possible
print(y.max) #to print max time possible

