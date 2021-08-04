"""
This script runs the hangman game in command line where the user asked to guess
a letter of an English word, if he/she successes then he/she has to guess the
next letter of that word. But if he/she fails then lose a life and proceeds to
hang.
"""

import random
from clear_screen import clear
from hangman_arts import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list) # choose a word randomly from the word list
# print(chosen_word)
dashes = list("_" * len(chosen_word))
lives = 6 # total lives

print(logo)

while dashes.count("_") > 0 and lives > 0:
  guess = input("Guess a letter: ").lower()

  if guess in dashes:
    clear()
    print(f"You have already guessed {guess}")

  for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
        dashes[i] = guess

  if guess not in chosen_word:
    print(f"You guessed {guess}. That's not in the word. You lose a life.")
    lives -= 1
  
  print(f"{' '.join(dashes)}")
  print(stages[lives])

if lives > 0:
  print("You Win!")
else:
  print("You Lost!")








  
