'''
Modules:
1. You can create your own modules.
2. To call your own created modules, make sure the module file or module package you are calling must be saved in the
   same folder as your file.

3. Module file- This is a single python file.
   Module packages- This is a single folder consists of many python files.
4. There are three ways to import modules:
   1. from module_name import function_name
        OR
      from package_name import module_name

   2. from module_name import*
      Here * is used to import all the functions from the file
   3. import module_name
'''
#Examples:
'''
i have created a folder sirf which is stored in the same location and also some files.
'''
from sirf import calca #calling package
import calc # calling module
