import random


name = input("Player tell me your name")
playerchoice = input("Choose Rock , Paper or Scissors")

aichoice = random.randint(1, 3)

if aichoice == 1:
    aichoice = "Rock"
elif aichoice == 2:
    aichoice = "Paper"
elif aichoice == 3:
    aichoice = "Scissors"

print(aichoice)

if playerchoice == "Rock" and aichoice == "Rock":
        print("Tie")

if playerchoice == "Rock" and aichoice == "Paper":
        print("aichoice won")

if playerchoice == "Rock" and aichoice == "Scissors":
        print(name,"won")

if playerchoice == "Paper" and aichoice == "Paper":
        print("Tie")

if playerchoice == "Paper" and aichoice == "Scissors":
        print("aichoise won")

if playerchoice == "Paper" and aichoice == "Rock":
        print(name,"won")

if playerchoice == "Scissors" and aichoice == "Scissors":
        print("Tie")

if playerchoice == "Scissors" and aichoice == "Rock":
        print("aichoise won")

if playerchoice == "Scissors" and aichoice == "Paper":
        print(name,"won")



