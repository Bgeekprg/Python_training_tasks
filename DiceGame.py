import random


def roll_dice():
    return random.randint(1, 6)


def start_game():
    print("-------- Dice Game -------")
    input("Press Enter to roll the dice...(Player 1)")

    player1_roll = roll_dice()
    print(f"player1 rolled a {player1_roll}!\n")
    
    input("Press Enter to roll the dice...(Player 2)")
    player2_roll = roll_dice()
    print(f"player2 rolled a {player2_roll}!\n")

    print("----------------------------")
    if player1_roll > player2_roll:
        print("player1 win!")
    elif player1_roll < player2_roll:
        print("player2 wins!")
    else:
        print("It's a tie!")




start_game()
choice=input("\n You want to play Again (y/Y) ")
while(choice.upper()=="Y"):
    start_game()
    choice=input("\n You want to play Again (y/Y) ")

