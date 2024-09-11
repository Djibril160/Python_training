# for in loop

numbers = [1, 2, 3, 4, 5]
# dog = { "name": ("Pitbull", "Dobermann"), "Dangerous": True, 93: "Yes", "numbers" : [1, 2, 3, 4, 5] }

# for i in dog["numbers"]:
#   print(i)

sum = 0

for x in range(10):
  sum += x
  print("sum in range = ",sum)

# loop with : 
# index limit  
# zip


rows = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
rows_even = rows[::2] 
# [::2] utilise une opération de découpage de liste pour sélectionner chaque deuxième élément de la liste rows. Voici comment cela fonctionne :
# rows : C'est la liste à partir de laquelle vous souhaitez sélectionner les éléments.
# [::2] : C'est la syntaxe de découpage de liste.
# Le premier : indique que vous allez spécifier le début et la fin de la tranche,
# le deuxième : spécifie le pas, c'est-à-dire le nombre d'éléments à sauter entre chaque élément sélectionné.

rows_odd = rows[1::2]
# ici idem que là haut, sauf qu'on commence à l'index 1 
"""
for index, (row_even, row_odd) in enumerate(zip(rows_even, rows_odd)):
    if index >= 6:
        break
    invoice_id = self.get_element('./td[2]', "xpath", driver=row_even).text
    self.secure_click('./td[8]/a', "xpath", driver=row_even)
    self.scroll_to(row_even)
    invoice = self.get_element('.//div[@class="col-xs-12"]/a[text()="Scarica in PDF"]', "xpath", driver=row_odd)
    self.secure_download(invoice, invoice_id, self.already_downloaded_invoices)
"""
"""
Dans cette boucle, enumerate() est utilisé pour obtenir à la fois l'indice index et les paires de row_even et row_odd. 
La boucle s'exécute jusqu'à ce que index atteigne la valeur 6, 
auquel cas elle s'arrête en utilisant l'instruction break, ce qui limite le nombre d'itérations à 6. 
Cela permet de traiter les six premières paires de row_even et row_odd
"""

################################  WHILE LOOP ####################################################

counter = 0.0
while counter <= 1.0:
  print("counter => ", counter)
  counter += 0.25

################################  list comprehension ####################################################
# redefine a list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# create a list
account_rows = self.get_element('//select[@id="accountSelector"]/option', "xpath", index="*")
accounts = [account.text[0:7] for account in account_rows]

# accounts = ['3019690', '3041087', '3062396', '3083766']
