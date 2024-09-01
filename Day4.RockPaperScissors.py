import random


rockpaperscissors = [
"""
    _______
---'   ____)
      (_____)
      (_____) 
      (____)
---.__(___)""",
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""]



# Player Module

playerChoice = None
playerName = input("What is your player name?")

def player():
    global playerChoice

    print(f"Welcome {playerName}!")
    playerChoice = input("Rock, Paper, or Scissors\n").lower()
    if playerChoice == "rock":
        playerChoice = rockpaperscissors[0]
        print(playerChoice)
    elif playerChoice == "paper":
        playerChoice = rockpaperscissors[1]
        print(playerChoice)
    elif playerChoice == "scissors":
        playerChoice = rockpaperscissors[2]
        print(playerChoice)
    else:
        print("This is not a choice, try again.")
        player()



# CPU Module

cpurand = random.randint(0,2)
cpuChoice = None
def cpu():
    global cpuChoice

    cpuChoice = rockpaperscissors[cpurand]
    print(cpuChoice)



# Game Module

def game():
    if playerChoice == cpuChoice:
        print("ITS A DRAW!")
    elif playerChoice == rockpaperscissors[0] and cpuChoice != rockpaperscissors[1]:
        print(f"{playerName} Wins!")
    elif playerChoice == rockpaperscissors[1] and cpuChoice != rockpaperscissors[2]:
        print(f"{playerName} Wins!")
    elif playerChoice == rockpaperscissors[2] and cpuChoice != rockpaperscissors[0]:
        print(f"{playerName} Wins!")
    else:
        print("CPU Wins!")



# Game

player()
cpu()
game()

