"""Ceaser Cipher

This Python Script Encode or Decode A English text message according to ceasar 
cipher for a given shift number.
"""

import string
from art import logo


def ceasar(text: str, shift: int, direction="encode") -> str:
  """takes a English text to encode or decode, shift number and direction (i.e. encode
  or decode) and returns encoded or decoded text

  parameter
  ---------
  text: str,
  text to encode or decode
  shift: int,
  integer number of how many position you want to shift for each letter in the text
  direction: str, optional
  takes 'encode' or 'decode' as value. It none given, defaults to 'encode'
  """
  shifted_text = ""
  alphabet = string.ascii_lowercase # the lowercase 26 English alphabet

  if direction == "decode":
    shift *= -1

  for letter in text:
    if letter in alphabet:
      ix = (alphabet.index(letter) + shift) % 26
      shifted_text += alphabet[ix]
    else:
      shifted_text += letter
  print(f"Here's the {direction}d result: {shifted_text}") 


print(logo)
response = "yes"

while response == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction in {"encode", "decode"}:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  else:
    print(f"You have typed {direction}. Did you mean 'encode' or 'decode' ??")
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  if response == "no":
    print("Goodbye!")
