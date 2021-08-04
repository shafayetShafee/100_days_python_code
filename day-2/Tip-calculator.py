"""
It calculates a certain amount of tips (10%, 12%, 15%) of total bill
"""

print("Welcome to the tip calculator")

# getting user input
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# calculate the percentage tips
pay_per_person = (total_bill / people) * (1 + (tip / 100))
print(f"Each person should pay: ${pay_per_person:.2f}")