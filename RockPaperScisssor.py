import random
import math
class RockPaperScissor:
    def __init__(self):
        self.playerAction=""    
        self.computerAction=""
        self.playerScore=0
        self.computerScore=0
        self.Tie=0
        self.rounds=0
        self.actionDict={1:"Rock",2:"Paper",3:"Scissors"}

    def menu(self):
        print("1. Rock\n2. Paper\n3. Scissors")
    
    def start(self):
        self.menu()
        try:
            self.playerAction=int(input("Choose ur Action = "))
            if(self.playerAction>3 or self.playerAction<1):
                raise Exception
            self.computerAction=random.randint(1,3)
        except:
            print("You entered Invalid choice !\n")
            return "err"
    
    def result(self):
        player=self.playerAction
        computer=self.computerAction
        print(f"You = {self.actionDict[player]} , computer = {self.actionDict[computer]}")
        print("--------------------------")
        if player==1 and computer==2:
            self.computerScore+=1
            return "you Lose this round!"
        
        elif player==2 and computer==3:
            self.computerScore+=1
            return "you Lose this round!"
        
        elif player==3 and computer==1:
            self.computerScore+=1
            return "you Lose this round!"
        
        elif player==computer:
            self.Tie+=1
            return "Tie"
        else:
            self.playerScore+=1
            return "you win this round!"

    

game=RockPaperScissor()
score_to_win=0
try:
    game.rounds=int(input("Enter how many rounds u wanna play ="))
    score_to_win=math.ceil(game.rounds/2)

    print(f"You have to score {score_to_win} for win !")
    print(f"Note: If you both get winning score then it's tie !\n")
    print('-'*45)
except:
    print("You entered wrong type of value !")
else:
    tmp_round=game.rounds
    while game.rounds>0:

        if(game.start()=="err"):
            continue
        print(game.result()+'\n')
        game.rounds-=1
    
    print('-'*45)
    print(f"Total Rounds={tmp_round}")
    print('-'*45)
    print(f'|Your score ={game.playerScore} , computer score = {game.computerScore} ,Tie = {game.Tie}'.ljust(45)+'|')
    print('-'*45)
    
    if game.computerScore==score_to_win and game.playerScore==score_to_win:
        print("| It's a tie".ljust(45) + '|')
    elif game.playerScore >= score_to_win:
        print("| you won Game".ljust(45) + '|')
    else :
        print("| You lose Game".ljust(45) + '|')

    print('-'*45)