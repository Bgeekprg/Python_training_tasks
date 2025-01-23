from random import *

class NumberGuess:
    def __init__(self):
        self.secret_number = None
        self.low = None
        self.high = None

    # generating a secret number for the user to guess
    def generateSecretNumber(self):
        self.low = int(input("Enter starting point = "))
        self.high = int(input("Enter ending point = "))
        self.secret_number = randint(self.low, self.high)
    
    # checks the guessed number is correct or not
    def guessNumber(self, guessed_number):
        if guessed_number == self.secret_number:
            return True
        elif guessed_number > self.secret_number:
            print("Try Again! Your guess is too high.\n")
            return False
        else:
            print("Try Again! Your guess is too low.\n")
            return False

print("------- Number Guessing Game -------")
print("You have 7 chances. Let's play!\n")

game = NumberGuess()
game.generateSecretNumber()

# Number of chances given to the user
chances = 0
max_chances = 7  
flag = False


while chances < max_chances:
    print(f"Chance ({chances + 1}/{max_chances})")
    
    try:
        guessed_number = int(input(f"Guess a number between {game.low} and {game.high}: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Check if the guessed number is correct
    if game.guessNumber(guessed_number):
        print("Congratulations! You guessed the correct number!")
        flag = True
        break
    
    chances += 1

# If the game ends without a correct guess
if not flag:
    print(f"Sorry, you lose! The correct number was {game.secret_number}.")
