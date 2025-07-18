# Classes
"""
Les classes sont des "modèles" permettant de créer des objets notamment pour les projets orientés objets
Elles servent de plan ou de modèle à partir duquel les objets peuvent être créés. 
Une classe définit les attributs => variables et les méthodes => fonctions associés à ses objets

class = plan (blueprint) de la classe pour créer des instances ()
instance = ce sont les elements qui viennent de la class par ex: "salah"


dans l'exemple ci dessous :
'class Premierleague:' : définit une classe nommée Premierleague

'def __init__(self, team, player):' :
c'est une méthode appelée le constructeur / initializer 
Elle est utilisée pour initialiser les attributs (variable) de l'objet lors de sa création. 
"Self" fait référence à l'instance de l'objet lui-même qu'il faut tjr mettre.

`self.team = team` et 'self.player = player':
ce sont des attributs (variables) de l'objet Premierleague qui sont initialisés à partir des valeurs passées lors de la création de l'objet.

'def description(self):' :
  est une méthode (fonction) de la classe qui retourne une description de l'objet.
  la methode prend toujour "self" en argument

Pour créer un objet à partir de cette classe, on l'instancie de cette manière :
'salah = Premierleague("Liverpool", "Mohammed Salah")'
cela va créer une instance qui se nomme "salah" avec les variable "team = Liverpool" et "player = Mohammed Salah"

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
  def __init__ (self, team, player, position):
    # 3 attributes here: position, player, team
    self.team = team
    self.player = player
    self.position = position
  
  def description(self):
    return f"{self.player} plays for {self.team} as {self.position}"
  
# Objet :
salah = Premierleague("Liverpool", "Mohammed Salah", "striker")

print(f"printing team of player: {salah.team}")
print(f"printing name: {salah.player}")

print(salah.description())


#Classe FootballPlayer (enfant) qui hérite de Premierleague
class FootballPlayer(Premierleague):
  gender = "male"
  def __init__(self, team, player, position, value):
    super().__init__(team, player, position) #Appel du constructeur de la classe parente avec super()
    self.value = value

  def info(self):
    return f"{self.player} plays as a {self.position} for {self.team}"
  
  @classmethod
  def player_gender(cls):
    return cls.gender
  
arnold = FootballPlayer("Liverpool", "Alexander Arnold", "right defender", 9929920)

print(arnold.info())
arnold.gender = "woman"

print(f"This player is {arnold.gender}")



"""
Un '@classmethod' est une méthode qui est liée à la classe elle-même et non à une instance spécifique de la classe.

Elle reçoit cls comme premier argument (au lieu de self pour une méthode d’instance).

Elle peut accéder et modifier les attributs de classe, mais pas les attributs propres aux instances individuelles.

"""
