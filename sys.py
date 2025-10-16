import sys

# gives the name of file and others arguments given in the terminal
# with command -> python sys.py 123 abc  
# if you want to skip the file name, you can slice it arguments = sys.argv[1:]
arguments = sys.argv
print(f"We received these arguments {arguments}") 

print(f"We're currenctly running of a {sys.platform} machine")

