import random


def get_choices():
  player_choice = input("Enter a choice (Steven Gerrard, Ronaldinho, Zidane: ")
  options = ["Steven Gerrard", "Ronaldinho", "Zidane"]
  computer_choice = random.choice(options)
  choices =  { "player": player_choice, "computer": computer_choice }
  return choices

def check_win(player, computer):
  print("you chose " + player + ", computer chose " + computer)
  # f-string allow to add variable in a string
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "Steven Gerrrard" and computer == "Zidane": 
    return "Steven Gerrard smashes Zidane! You win."
 
  elif player == "Steven Gerrrard" and computer == "Ronaldinho": 
    return "Ronaldinho smashes Steven Gerrard! You lose."

 # autre méthode :
  #if player == computer:
    #return "It's a tie!"
  # elif player == "Steven Gerrrard":
    #if computer == "Zidane": 
      #return "Steven Gerrard smashes Zidane! You win."
    # else:
      #return "next on the line please"
  


get_choices()

# check_win("Steven Gerrard", "Ronaldinho")




# condition if/elif/else
age = 18

if age >= 18:
  print("you are an adult")
elif age > 12:
  print("you are a teenager")
elif age > 1:
  print("you are a child")
else:
  print("you are a baby")
  

# dictionary acces
  
  choices = {"player": "rock", "computer": "paper"}
  p_choice = choices["computer"]

  print(p_choice)