import random
print("== Infinity Dice 🎲 ==")
print()
sides = int(input("How many sides?: "))
play_again = "yes"

def roll_dice(sides):
  print("You rolled", random.randint(1, sides))
while play_again == "yes":
  roll_dice(sides)
  play_again = input("Roll again? ")