# Classes
"""
Les classes sont des "modèles" permettant de créer des objets notamment pour les projets orientés objets
Elles servent de plan ou de modèle à partir duquel les objets peuvent être créés. 
Une classe définit les attributs => variables et les méthodes => fonctions associés à ses objets

dans l'exemple ci dessous :
'class Premierleague:' : définit une classe nommée Premierleague

'__init__(self, team, player):' :
c'est une méthode appelée le constructeur. 
Elle est utilisée pour initialiser les attributs (variable) de l'objet lors de sa création. 
Self fait référence à l'instance de l'objet lui-même qu'il faut tjr mettre.

`self.team = team` et 'self.player = player':
ce sont des attributs (variables) de l'objet Premierleague qui sont initialisés à partir des valeurs passées lors de la création de l'objet.

'def description(self):' :
est une méthode (fonction) de la classe qui retourne une description de l'objet.

Pour créer un objet à partir de cette classe, on l'instancie de cette manière :
'salah = Premierleague("Liverpool", "Mohammed Salah")'

Maintenant, salah est un objet de type Premierleague avec les attributs team et player définis.
On peut accéder à ces attributs et appeler des méthodes associées à l'objet :
'print(salah.team)'
'print(salah.player)'

'print(salah.description())'

on peut faire hériter (inheritance) une classe d'une autre classe: 
celle qui hérite est l'enfant/sous-classe et peut hériter des attributs et des méthodes celle qui fait hérité appelée parente/super-classe

dans la sous classe: super().__init__(team, player) #Appel du constructeur de la classe parente avec super()

"""

# Premierleague = nom de la classe (parent ici)
class Premierleague:
  def __init__ (self, team, player):  # 
    self.team = team
    self.player = player
  
  def description(self):
    return f"{self.player} plays in {self.team} team"
  
salah = Premierleague("Liverpool", "Mohammed Salah")

print(salah.team)
print(salah.player)

print(salah.description())


#Classe FootballPlayer (enfant) qui hérite de Premierleague
class FootballPlayer(Premierleague):
  def __init__(self, team, player, position):
    super().__init__(team, player) #Appel du constructeur de la classe parente avec super()
    self.position = position

  def info(self):
    return f"{self.player} plays as a {self.position} for {self.team}"
  
arnold = FootballPlayer("Liverpool", "Alexander Arnold", "right defender")

print(arnold.info())