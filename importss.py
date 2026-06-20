# Import functions
'''we gonna learn how does import function works'''


import math

result = math.sqrt(9)
print (result)

# also some specific functions can be called or even all of the functions from a module can be called

from math import sqrt, pi  # Only square and pi = 3.14 is imported
# or
from math import *         # The star imports all of the functions from the respective module
# or
from math import sqrt as i #  can be used a variable 
# or 
print(dir(math))