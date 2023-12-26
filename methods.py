# methods

"""

len(name) Return the number of items in a container 
.upper()
.islower()
.lower()
.isupper()
.startswith()
.endswith()
.title() put all letter in capital letter and the rest if lower 
.replace() Return a copy with all occurrences of substring old replaced by new. ("old element", "new element")
.strip() removes or truncates the given characters from the beginning and the end of the original string
.split() 
  The split() method splits a string into a list
  string.split(separator, maxsplit)
  separator:	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
  maxsplit:	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
.find() 
  Method finds the first occurrence of the specified value
  Return the lowest index in the string where substring is found
  Returns -1 if the value is not found
.join()
  method takes all items in an iterable and joins them into one string.
  A string must be specified as the separator
.isalpha() checks if a string only contains characters and is not empty
.isdecimal() Return True if the string is a decimal string, False otherwise.
.isalnum() Return True if the string is an alpha-numeric string, False otherwise.

.append() add an item to a list 
.extend(["Seedorf", "Balotelli"]) add multiple items to a list 
.remove() remove an item 
.pop() remove the last item of the list
popitem() method removes the item that was last inserted into the dictionary
.insert(2, "Tesla") insert only ONE element at a specific index (index position, value)
items[1:1] = ["House", 1000000] => splice, add items at a specific index
.sort(key=str.lower) 
  Sort the list in ascending order, 
  key=str.lower is added otherwise, the elements with capital letter will come first
  it modify the list, if needed make a copy as below
  itemscopy = items[:]
  to not modify the list use : sorted(items, key=str.lower)
.get("key") Return the value for key if key is in the dictionary, else return None
.keys() to get the keys of a dicionnary
  to get a list add "list()" before the variable : print(list(dog.keys()))
.value() to get the values of a dicionnary
.items() to get the items of a dicionnary, made into a list
del var["key"] to delete a key:value in dictionnary


#SETS
.intersection() Return the intersection of two sets as a new set  
.union() Return the union of sets as a new set
.difference() Return the difference of two or more sets as a new set


"""