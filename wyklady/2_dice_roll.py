import random

def dice_roll(x):
    sum_of_dices = 0
    for n in range(x):
        diceroll = random.randrange(1,7) # taking random number from range <1,6>
        print("Dice rolled: ",diceroll)
        sum_of_dices += diceroll # adding the roll to sum of rolls
    return sum_of_dices
    
how_many_rolls = 5

print("Sum of dices:", dice_roll(how_many_rolls))  