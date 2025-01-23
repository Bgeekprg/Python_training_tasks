import random

def roll_dice():
    return random.randint(1, 6)

while True:
    user_input = input("Press 1 to roll the dice or 0 to exit: ")
        
    if user_input == '1':
        dice_roll = roll_dice()
        print(f"The dice rolled: {dice_roll}")
    elif user_input == '0':
        print("Exiting the dice roll program.")
        break
    else:
        print("Invalid input. Please press 1 to roll the dice or 0 to exit.")
