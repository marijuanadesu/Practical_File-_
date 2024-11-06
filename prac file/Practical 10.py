#PRACTICAL 10
'''Write a random number generator that generates
 random numbers between 1 and 6 (simulates a dice).'''
import random

def roll_dice():
    return random.randint(1, 6)

# Roll the dice
result = roll_dice()
print("The dice rolled: ",result)
