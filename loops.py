# for in loop

numbers = [1, 2, 3, 4, 5]
# dog = { "name": ("Pitbull", "Dobermann"), "Dangerous": True, 93: "Yes", "numbers" : [1, 2, 3, 4, 5] }

# for i in dog["numbers"]:
#   print(i)

sum = 0

for x in range(10):
  sum += x
  print(sum)

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

for index, (row_even, row_odd) in enumerate(zip(rows_even, rows_odd)):
    if index >= 6:
        break
    invoice_id = self.get_element('./td[2]', "xpath", driver=row_even).text
    self.secure_click('./td[8]/a', "xpath", driver=row_even)
    self.scroll_to(row_even)
    invoice = self.get_element('.//div[@class="col-xs-12"]/a[text()="Scarica in PDF"]', "xpath", driver=row_odd)
    self.secure_download(invoice, invoice_id, self.already_downloaded_invoices)
