import math


def prime_checker(number: int) -> None:
  """Given a number checks if that number is prime number"""
  flag = True

  if number > 1:
    if number == 2:
      flag = True
    elif number > 2 and number % 2 == 0:
      flag = False
    else:
      max_div = math.floor(math.sqrt(number))
      for i in range(3, 1+max_div, 2):
        if number % i == 0:
          flag = False
          break
  else:
    flag = False

  if flag:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
          


n = int(input("Check this number: "))
prime_checker(number=n)
