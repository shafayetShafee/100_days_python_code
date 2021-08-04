"""Treasure Island Game

This script runs a simple treasure island game, where in each stage, user is 
asked about his decision. The game ends with user choosing a spcific colored door.
"""

from ascii_art import treasure_ascii

print(treasure_ascii)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if(direction.lower() != "left"):
  print("Fall into a hole.\nGame Over")
else:
  swim = input("You came to a lake. Ther is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
  if(swim.lower() != "wait"):
    print("Attacked by trout.\nGame Over")
  else:
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
    if (door == "yellow"):
      print("You win!")
    elif (door == "red"):
      print("Burned By Fire\nGame Over")
    elif (door == "blue"):
      print("Eaten By Beasts\nGame Over")
    else:
      print("Game Over")
