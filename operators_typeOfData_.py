# variables : cannot starts with a number 
# to have differents statement on the same line, it must be seperated with semicolone ";"
name = "Djibril"; print(name)
age = 37.9 ; print(age)
num_shirt = 6


# data types
"""
bool : Booleans
str : Strings
numbers : 
  - int: whole (entier)
  - float: with decimal
  - complex: with a "real" part and "imaginary" part
""" 
print(f"type of variable age: {type(age)}")
print(f"type of variable N° maillot: {type(num_shirt)}")
print(f"Is name an instance of str ? {isinstance(name, str)}")
# print(type(name) == num)

# isinstance(), verifie le type de l'élément, et renvoie un bool
print("______________age est un int?_____________")
print(isinstance(age,int)) # False, c'est un float

# convert str to float
raliss_str = "2000000" # amount in str
raliss_int = float(raliss_str) #converted into number int
K_money = raliss_int/1000
print(type(K_money))
print(f"Money in banK {K_money}KEUR")

# absolute value (tout en positif)
value = -10
print(f"Absolute value of {value} = {abs(value)}")

# rounding value 
value2 = 2.49
print(f"arrondi de  {value2} = {round(value2)}")
# choose de decimal rounding
value3 = 2.49096
print(f"arrondi a 2 decimales de {value3} = {round(value3, 2)}")

# divide and rounds down  
cake = 13
remain = cake // 3
print(f"rest cake {remain}")

""" 
Boolean Operators 
"""

condition1 = True
condition2 = False

# "not" (has to be False) ==> return the opposite of the operand value 
opposite = not condition2 
print(f"opposite of conditions2 {opposite}") # return True

# "or" (one of them has to be true) ==> return value of first operand which is not False or Falsy, otherwise return the last operand
print(0 or 1) #0 is consider as false
print({} or False) # empty list or curly braket = falsy value
print(False or False or "c'est moi ;)!")  

""" 
"and" (both operands have to be true) ==> 
if the fisrt argument is False/Falsy, it returns that argument
if the first operand is True, "and" checks the second argument, otherwise return the last operand"""
print(0 and 1) 
print(1 and 0)
print("coucou" and [])


"""
"any()" Retourne True si au moins un élément de l’itérable est "truthy"
"all()" Retourne True si atous les  éléments de l’itérable sont "truthy"
"""

# any()
mots = ["lion", "tigre", "chat"]
print(any(len(m) > 4 for m in mots)) # True, tigre a 5 lettres

# all()
mots = ["lion", "tigre", "chat"]
print(all(len(m) > 4 for m in mots)) # False , il y a que tigre qui a plus de 4 lettres


"""
"is" return true if both  object are the same
"in" memory shift, if a value is in a list or sequence 
"""

name2 = "Ousmane"
print("us" in name2)

# ternary operator 
def is_adult(age):
  if age >= 18:
    return True
  else:
    return False
  
def is_adult2(age): 
  return True if age > 18 else False

