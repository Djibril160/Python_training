from enum import Enum

# variables : cannot starts with a number 
# create a constante :
""" 
1- import Enum : 
  from enum import Enum
2- code as below : 
  class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    SLEEPING = "KO"
  """
print("######################################### Strings ########################################")
# String is immutable, you can't change the characters in a string, you can read/find it 

"Djibril"
'Djibril'

name = "Djibril"
print(name)
phrase = "Djibril" + " is my name" 
phrase2 = name + " is my name"
name += " is my name"
print(name) 
# get the character of a specific index string
print(f"get the character of index 2 (starting from 0): {name[2]}") 
# get the character of a specific index -1 => last character and going back
print(f"get the character of index -2 (avant dernier caractère = -1): {name[-2]}") 

#sliceing: 
#the start at first index, last element is ending before index given
print(name[0:4])
# if blank start = starts from bigining
print(name[:10])
# if blank end = take to the end
print(name[11:])

# escaping charater adding backquote in a string with backslash
quality = "l\"exellence\"" 
quality2 = ' Bogosse"'
print(quality + quality2)


# multi line string with """..."""
print("""Djibril is
      
      myyyy

      naaaaame!
      
      """)

# String methods 
print("Djibril".upper())
print("SOUKOUNA".lower())
print("dJIbril soUkOuna".title()) # title() put all letter in capital letter and the rest if lower 
print("dJIbril soUkOuna".replace("dJIbril", "Ousmane")) # Return a copy with all occurrences of substring old replaced by new.
print("  no whitespace     ".strip()) # removes or truncates the given characters from the beginning and the end of the original string
print("My name is slim Shady".split()) # method splits a string into a list
myTuple = ("John", "Peter", "Vicky")

x = " ".join(myTuple)
print(x)

my_list = ["h", "e", "l", "l", "o", "!"]
la_hass = (", ").join(my_list[:4]).replace(", ","")
print(la_hass)

print("Djibril".startswith("D")) # check if a string starts with a specific character
print("444".isalnum()) # Return True if the string is an alpha-numeric string, False otherwise.
print("444".isdecimal() ) # Return True if the string is a decimal string, False otherwise.
print("00444".find("4") ) # Return the lowest index in the string where substring is found, possible 
print(len(name))



# convert type of data 
#str to float
raliss_str = "2000000" # amount in str
raliss_int = int(raliss_str) #converted into number int
K_money = raliss_int/1000
print(type(K_money))
print(f"Money in banK {K_money}KEUR")

# number to string
age2 = str(39)
print(type(age2))

# condition if/elif/else
age = 18

if age >= 18:
  print("you are an adult")
elif age > 12:
  print("you are a teenager")
elif age > 1:
  print("you are a child")
else:
  print("you are a baby")

#condition statements
condition = False
name = "Djibril"

if condition == True:
  print("The condition")
  print("was True")
elif name == "Pierre":
  print("Hello Pierrot")
elif name == "Djibril":
  print("Hello Djibson")
else:
  print("I don't know you")


# access a value in a dictionary (object in JS) 
choix = {"player": "rock", "computer": "paper"}
p_choix = choix["computer"]

print(p_choix)


################################################ Booleans ################################################
# number are consider as True EXECPT 0 
# if a string, list or dictionary are empty => consider as False 
# empty list, tuple, set, and dic are == False
# None = False

True 
False

done = True

if done:
  print("yes") 
else:
  print("no")

book_1_read = True
book_2_read = False

# any return True if any element of the list True
read_any_book = any([book_1_read, book_2_read])
print(f"Did he read any book ? {read_any_book}")

# all return True if All element of the list True
read_all_books = all([book_1_read, book_2_read])
print(f"Did he read all books ? {read_all_books}")


# create a list constante :
""" 
1- import Enum : 
  from enum import Enum
2- code as below : 
  class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    SLEEPING = "KO"
  """
class State(Enum):
    address = "1 allée des Gentianes"
    zip_code = 94510
    SLEEPING = "KO"

# to get the number of element 
print(len(State)) 

# to access a data
print(State.zip_code.value)

# to get the list
print(list(State))
