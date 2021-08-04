"""
This script generates a strong password containing letters, symbol and numbers.
Here the user is asked for how many letters, symbol and numbers he/she wants 
in his/her password and then builds a strong password.
"""

import random
import string

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# randomly selects letters, symbols and numbers
letters = random.sample(string.ascii_letters, n_letters)
symbols = random.sample(list_symbols, n_symbols)
numbers = random.sample(string.digits, n_numbers)

# then shuffle the whole list
result_list = letters + symbols + numbers
random.shuffle(result_list) # shuffle inplace

password = "".join(result_list)

print(f"Here is your password: {password}")

