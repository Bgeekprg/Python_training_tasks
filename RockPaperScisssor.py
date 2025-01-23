import random

class RockPaperScissor:
    def __init__(self):
        self.playerAction=""    
        self.computerAction=""
        self.actionDict={1:"Rock",2:"Paper",3:"Scissors"}

    def menu(self):
        print("1. Rock\n2. Paper\n3. Scissors")
    
    def start(self):
        self.menu()
        try:
            self.playerAction=int(input("Choose ur Action = "))
            if(self.playerAction>3):
                raise Exception
            self.computerAction=random.randint(1,3)
        except:
            print("You entered Invalid choice !")
            exit(0)
    
    def result(self):
        player=self.playerAction
        computer=self.computerAction
        print(f"You = {self.actionDict[player]} , computer = {self.actionDict[computer]}")
        print("--------------------------")
        if player==1 and computer==2:
            return "you Lose !"
        elif player==2 and computer==3:
            return "you Lose !"
        elif player==3 and computer==1:
            return "you Lose !"
        elif player==computer:
            return "Tie"
        else:
            return "you win !"

    

game=RockPaperScissor()
game.start()
print(game.result())