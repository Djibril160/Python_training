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

    def download_invoices_little_account(self):
        rows = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        rows_even = rows[::2] 
        rows_odd = rows[1::2]

        for index, (row_even, row_odd) in enumerate(zip(rows_even, rows_odd)):
            if index >= 6:
                break
            invoice_id = self.get_element('./td[2]', "xpath", driver=row_even).text
            self.secure_click('./td[8]/a', "xpath", driver=row_even)
            self.scroll_to(row_even)
            invoice = self.get_element('.//div[@class="col-xs-12"]/a[text()="Scarica in PDF"]', "xpath", driver=row_odd)
            self.secure_download(invoice, invoice_id, self.already_downloaded_invoices)
