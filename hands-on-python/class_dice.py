# Create a class called Dice that has attribute sides (the number of sides on the dice). Add a method roll that generates
# a random number between 1 and the number of sides on the dice

# import random module to generate random number
import random
# Create a class called Dice that has attribute sides (the number of sides on the dice).
class Dice:
    def __init__(self, sides):
        self.sides = sides
    # Add a method roll that generates a random number between 1 and the number of sides on the dice
    # use randint method from random module to generate random number
    def roll(self):
        return random.randint(1, self.sides)

# Create an instance of the Dice class and call the roll method.
dice = Dice(6)
# print the result of rolling the dice
print(f"The result of rolling the dice is: {dice.roll()}")
