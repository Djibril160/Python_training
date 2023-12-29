# Functions
# parameter is the value accepted by the function inside the function body
# argument is the value we pass to function when we call it
# a variable in a function is only available in the function

# Simple function without parameter
def hello():
  print("Hello !")

hello()


# function with a parameter
def Welcome(name, age):
  print("Welcome " + name + ", you are " + str(age) + " years old." ) 

Welcome("Djibril", 37)


# Fuction with default value
def goodbye(name="My friend"):
  print("Goodbye " + name)

goodbye()


# Function with return, after return, nothing is executed, except if in a if/else... 
# to see what's in the return statement, print the function
def sleep (name):
  if not name:
    return
  print("It's time to sleep " + name + " !")
  return name, 37, " Y-O"

sleep("Petit")
print(sleep("Bogoss"))


# Function nested with variable from the first function used in the nested function, with nonlocal before variable
# the nested function has to be called in the parent function
def count():
  count = 0

  def increment():
    nonlocal count # nonlocal allow to use a variable in the nested 
    count = count + 1
    print(count)

  increment() # call of function increment

count()


# Other example with counter 
def counter():
  count = 0

  def increment():
    nonlocal count # nonlocal allow to use a variable in the nested 
    count = count + 1
    return (count)

  return increment # call of function increment

increment = counter()
print(increment())
print(increment())
print(increment())



# lamdba function, also called anonymous functions
# a, b = parameters of functions

multiply = lambda a, b : a * b

print(f"Lambda function result is = {multiply(2, 10)}")


# LOOPS 2 types : while loops and for

# While loop
print("WHILE LOOP")
condition = True
while condition == True:
  print("Keep looping!")
  condition = False


shots = 5
while shots >= 0:
  print(f"You have {shots} shots left!")
  shots -= 1

print("Game over!")


# For loop 
print("FOR LOOP")
items =[1, 2, 3, 4]
for number in items:
  print(number)

# For loop with range defined 
for item in range(12):
  print(item)

# Index in for loop
players =["Gerrard", "Benzema", "Kanté", "Van Dikj"]
for index, top in enumerate(players):
  print(index, top)

# "continue" in for loop, skips the iteration in question
items = [1, 2, 3, 4]
for item in items:
  if item == 2:
    continue
  print(item)

# "break" in for loop, stop the iteration when condition is met
items = [1, 2, 3, 4]
for item in items:
  if item == 3:
    break
  print(item)


