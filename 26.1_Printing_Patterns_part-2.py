# 7 colm and 6 rows
for row in range(6):
     if row == 0:
         print(" ** ** ")
     elif row ==1:
         print("*  *  *")
     elif row ==2:
         print("*     *")
     elif row == 3:
         print(" *   * ")
     elif row ==4:
         print("  * *  ")
     else:
        print("   *   ")

# Second Method:
print("")

for row in range(6):
    for col in range(7):
        if (row == 0 and col%3!= 0) or (row ==1 and col%3 == 0) or (row- col ==2) or (col + row == 8):
            print("_", end = "")
        else:
            print(" ", end = "")
    print()