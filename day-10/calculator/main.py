"""This script contains a simple command line calculator program"""

from art import logo
from clear_screen import clear


# ---------------calculator function-----------------------
def add(n1: float, n2: float) -> float:
  """Takes two floating number and return their addition"""
  return n1 + n2

def subtract(n1: float, n2: float) -> float:
  """Takes two floating number and return their subtraction"""
  return n1 - n2

def multipliy(n1: float, n2: float)-> float:
  """Takes two floating number and return their multiplication""" 
  return n1 * n2

def divide(n1: float, n2: float) -> float:
  """Takes two floating number and return their division"""  
  return n1 / n2

# --------------calculator operations----------------------
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multipliy,
  "/" : divide
}


# -------------- main driver function ------------------
def calculator():
  """Runs the whole program as a driver function"""
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(f"{symbol}")

  response = 'y'

  while response == 'y':  
    operations_symbol = input("Pick an operation: ").strip()
    num2 = float(input("What's the next number?: ").strip())
    fun = operations[operations_symbol]
    answer = fun(num1, num2)
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    response = input(f"Type 'y' to continue calculating with {round(answer,2)}, "
                      "or type 'n' to start a new calculation or\n"
                      "type 'off' to shut off the calculator: ").strip()
    num1 = answer
    # to start a new calculation
    if response == "n":
      clear() # clear the command line screen
      calculator()

    # to shutoff the calculator
    if response == "off":
      clear() # clear the command line screen
      response = 'n'


calculator()
