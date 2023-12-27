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


# LOOPS 2 types : while loops and for

condition = True
while condition == True:
  print("Keep looping!")
  condition = False