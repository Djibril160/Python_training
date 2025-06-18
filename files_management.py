"""
‘r’	open for reading (default)
‘w’	open for writing, truncating the file first
‘a’	open for writing, appending to the end of the file if it exists
and others
https://practical.learnpython.dev/05_practical_applications/40_working_with_files/
"""

import json
from pprint import pprint

with open("cities.json") as cities_file: # give a name to 'open file'
  cities_data = json.load(cities_file)
  pprint(cities_data)
  print(type(cities_data[0]))
