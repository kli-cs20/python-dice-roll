# Dice Roll Simulator

import random

n = 1
num = float(input("How many times would you like to roll? "))

while n <= num:
    # Roll a Dice
    randNum = random.randrange(1, 7)
    print(randNum)

    n += 1
