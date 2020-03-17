'''
In case of appending, the added line will be added  in the file.
In case of write, the whole material is replaced by the line.
'''

'''
In case of writing and appending, program first checks whether there is any file which they want to open, it there is
then it will do changes in it, otherwise it will create new file.
'''


# type-1

employee_file = open("write1.py", "a")

print(employee_file.readable())

employee_file.close()

#2nd type

employee_file = open("write1.py", "a")

employee_file.write("Toby - Human resources")

employee_file.close()


#3rd type

employee_file = open("write1.py", "a")

employee_file.write("\nRam - Done")

employee_file.close()


# 4th type write mode

employee_file = open("write2.py", "w")

employee_file.write("\nRam - Done")

employee_file.close()


# 6th write mode to create html file

employee_file = open("ram.html", "w")

employee_file.write("<p>This is html<p>")

employee_file.close()
