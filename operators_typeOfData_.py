# variables : cannot starts with a number 
# to have differents statement on the same line, it must be seperated with semicolone ";"
name = "Djibril"; print(name)
age = 37.9 ; print(age)

print(f"type of variable age: {type(age)}")
print(f"Is name an instance of str ? {isinstance(name, str)}")
# print(type(name) == num)

# convert str to float
raliss_str = "2000000" # amount in str
raliss_int = float(raliss_str) #converted into number int
K_money = raliss_int/1000
print(type(K_money))
print(f"Money in banK {K_money}KEUR")

# divide and rounds down  
cake = 13
remain = cake // 3
print(f"rest cake {remain}")

# 