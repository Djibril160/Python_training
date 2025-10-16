import os

my_folder = os.getcwd() #cwd = current working directory
print(f"here are the files in my folder: {my_folder}") # renvoie qu'un fichier

# loop to see all files
with os.scandir(my_folder) as folder:
  for entry in folder:
    print(f"- file is {entry.name} in folder")

