import math

# import the function from the file in folder 
"""
if it's in a folder you have to create within the folder of modules a file name "__init__.py" to tell Python that the folder contains modules
to call a function of the file you have to do 
from lib.module_dog (name of folder + file) import "bark"
"""
from modules.module_dog import bark


# call the function of the file
bark()


print(math.sqrt(16))