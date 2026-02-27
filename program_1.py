

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.
import random

def randDice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice_sum = num1 + num2
    return dice_sum

rolls = []
for i in range(100):
    rolls.append(randDice())

average = sum(rolls) / len(rolls)
print (f'{average:.2f}')

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.