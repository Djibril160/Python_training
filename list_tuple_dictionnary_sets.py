######################################## Lists ########################################
"""
can take any type of value as long as it's separated with a comma (,)
"""
players = ["Gerrard", "Zidane", 6, 10, True, False]

players[2] = "Ronaldinho"

print(f"this is the lis of players {players}")
print("Gerrard" in players) #check 
print(players[-5])
print(f"list of 3 first players is {players[:3]}")
print(len(players))
players.append("Mané")
print(players)
players.extend(["Seedorf", "Balotelli"]) # or 
players += ["Djibril", "Ousmane"]
print(players)
players.remove(True)
print(players)
players.pop()
print(players)


items = ["ball", "laptop", "Cybertruck", "911"]

items.insert(2, "Tesla")
print(items)
items[1:1] = ["House", "1000000"]
print(items)
itemscopy = items[:]
items.sort(key=str.lower) # it modify the list, if needed make a copy as above
# print(sorted(items, key=str.lower)) to not modify the list but make a copy
print(items)
print(itemscopy)


######################################### Tuples ########################################

"""
a Tuple is multiple group of list which can't be changed 
"""

names = ("Koumba", "Diabé", "Idris", "Younous") # can be done without parentheses
print(names.index("Idris")) 
print(names[0])
print(len(names))
print("Djibril" in names)
print(type(names))


# Dictionnaries => { key:value } pair
"""
key : can be string, n°, tuple
"""

dog = { "name": ("Pitbull", "Dobermann"), "Dangerous": True, 93: "Yes" }
print(dog)
print(dog["name"]) # to access value
# or 
print(f"Is the dog in 93 ? {dog.get(93)}")
print(dog.get("age", "not mentionned")) # a default value can be specify if not found in the dictionnary
dog["Dangerous"] = False # change the value 
print(dog)
dog["favorite food"] = "Meat" # add an Item in a doctionnary
dog.pop(93)
print(f"After pop key 93 {dog}")
print(dog.popitem()) # removes last item added line
print("colors" in dog) # if the key colors is in the dictionnary
print(list(dog.keys()))
del dog["name"]


# Sets : ensemble (set) is a collection of uniques elemenet non ordored (pas d'index), which can contains only one same element
"""
- in curly brackets{}
- seperated by coma ","
- useful to eliminate duplicate

""" 

# eliminate duplicate from a list
my_list = [1, 2, 2, 3, 4, 4, 5, 5]
my_set = set(my_list)
print(my_set)

# operations 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
union = set1.union(set2)
difference = set1.difference(set2)

print(intersection)  # display : {3, 4}
print(union)         # display : {1, 2, 3, 4, 5, 6}
print(difference)    # display : {1, 2}


