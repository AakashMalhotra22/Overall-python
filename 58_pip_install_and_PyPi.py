'''
1. PyPI is a repository for open-source third-party Python packages.
2. By installing python from python.org or through distribution you also installed pip.
3. pip is a simple way to download packages at your command line directly from the PyPi repository.
4. The location where you will find your all the packages is at C:\Users\india\AppData\Local\Programs\Python\Python37-32\Lib\site-packages

'''

#Steps to import third party libraries in your computer:
'''
1. Go to command prompt and write #pip install requests# and press enter, this will allows you to request information
   from the website online.
   This will check whether all the conditions are satisfied or not, if all the conditions are satisfied for downloading
   packages, it would give output as all the conditions are satisfied, else it would download some stuff from internet.

2. Now write #pip install library name# and press Enter.
   For example, if a want to install colorama then i will write pip install colorama and press enter.
 
'''

'''
#pip also has version, so if you want to download the current version just write in command prompt.
 python -m pip install --upgrade pip
'''

#some external packages name and uses.

'''colorama-for color output'''
from colorama import *
print(Fore.RED +"some red text")
print(Fore.GREEN+"some green text")

'''openpyxl - for excel sheets'''
from openpyxl import *
