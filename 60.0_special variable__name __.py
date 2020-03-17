'''
Special variable __name__:
1.Let's consider you are working on a file name calc.py and if you write print(__name__) then it would give output as__main__ but if you import this file calc in other file and then
  run the code there then it would print calc.

2. Use of line if __name__ == "__main__"
   This ensures that your code will only run when you the run the code in main file only, not on the other file by importing this file.
'''

import calc


print("aakash says"+ __name__)# now here this __name__ means __main_.

print(__name__)