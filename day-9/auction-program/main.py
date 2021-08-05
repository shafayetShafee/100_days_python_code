"""
A simple program that simulates a very simple auction program.
"""

from clear_screen import clear
from art import logo


def response_checker(response: str) -> str:
  """Checks if the response is exactly 'yes' or 'no' and keep asking
  untill got the response clearly"""

  while response not in {'yes', 'no'}:
    response = input("Please type 'yes' or 'no'\n")
  return response


print(logo)
print("Welcome to the secret auction program.")
response = "yes"
bid_dict = {} # dictionary to save the bidder name as key and bidding value as value

while response == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid? $"))
  bid_dict[name] = bid
  response = input("Are there any other bidders? Type 'yes' or 'no'\n")
  response = response_checker(response)
  if response == "yes":
    clear()


bid_winner = [
  [key, value]  for key, value in bid_dict.items() if value == max(bid_dict.values())
]

print(f"The winner is {bid_winner[0][0]} with a bid of ${bid_winner[0][1]}")
