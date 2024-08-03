import random
import pyttsx3

engine = pyttsx3.init()

computer = random.choice([-1, 0, 1])

print("| WELCOME TO THE STONE ,PAPER ,SCISSOR GAME |")
engine.say("WELCOME TO THE STONE ,PAPER ,SCISSOR GAME")
engine.runAndWait()

engine.say("Enter your choice s for Stone, p for Paper, r for scissor")
engine.runAndWait()
youstr = input("Enter your choice (s for Stone, p for Paper, r for scissor):")



youDict = {"s": 1, "p": -1, "r": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissor"}
you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

#  The below logic is written on the basis of the value of computer - you

if(computer == you):
    print("Its a draw")
    engine.say("Its a draw")

else:
    if((computer - you) == -1 or  (computer - you) == 2 ):
        print("You Win")
        engine.say("You Win!")
    else:
        print("You lose!")
        engine.say("You lose!")
    engine.runAndWait()    
