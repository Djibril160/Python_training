
"""
try/except
elles viennent de la class Exception
si une exception est raised, le reste du code n'est pas exécuté, ça arrete le script
"""

user_age = "haha"
try:
  int(user_age)
except ValueError:
  print(f"no way, {user_age} is not a valid number")

num = 2
d = {1:1}
try:
  int(num)
  print(int(num))
  d[user_age]
except (ValueError, KeyError, NameError):
  print("holy shit! not good")

# giving a name to the error, ici bad_number
  
rr = "1000cc"
try:
  int(rr)
except ValueError as bad_number:
  print("éh non, c'est pas bon, regarde le pb mon pti", bad_number)


# you should start from the more specific to le less, for ex: here the more specific is ZeroDivisionError but we started with ArithmeticError
# so ArithmeticError will be executed first, as ZeroDivisionError is child of ArithmeticError, we will have peinted "math error"
# we should start with ZeroDivisionError
# issubclass(ZeroDivisionError, ArithmeticError) ==> True
def division_by_py(num):
  try:
    result =  3.14 / num
    return result
  except ArithmeticError:
    print("math error")
  except ZeroDivisionError:
    print("you cannot divide by zero dude")

test = division_by_py(0)


# Create your own Exception
# as they are from the class Exception, we have to give as arg Exception

class MauvaisNumException(Exception):
  pass

# raise MauvaisNumException() # to use it


class TestErrorDjibson(Exception):
  
  def __init__(self, value):
    message = f"you have put a very bad value: {value}"
    super().__init__(message)

my_value = 1000

# if my_value > 5:
#   raise TestErrorDjibson(my_value) # output: TestErrorDjibson: you have put a very bad value: 1000


class GitHubApi(Exception):
  def __init__(self, status_code):
    if status_code == 403:
      message = "Rate limit reached"
    else:
      message = f"the status code is: {status_code} "

    super().__init__(message)



# raise GitHubApi(403) # output : GitHubApi: Rate limit reached



