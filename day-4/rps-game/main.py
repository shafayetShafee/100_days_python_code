"""Rock-Paper-Scissor game

This script contains simple rock-paper-scissor game which runs the game only 
once (without any loop)
"""

import random
import rps

print("Welcome to Rock, Paper Scissor game")
# 0 for rock , 1 for paper, 2 for scissors
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2) # choosing a computer choice randomly
ascii_rps = [rps.rock, rps.paper, rps.scissors]

# 1st indices for player and nested indices for computer choice.
decision = [["d", "l", "w"], ["w", "d", "l"], ["l", "w", "d"]]

# output_dict contains the game output according to the result key
output_dict = {"d":"It's Draw", "l": "You Lost", "w": "You Won!"}

result = decision[player][computer] # game result


print(ascii_rps[player]) # prints the ascii art according to player choice
print("Computer Chose:")
print(ascii_rps[computer]) # prints the ascii art according to computer choice
print(output_dict[result]) # prints the game output


