"""
import random
# rock ,paper ,scissor 

print("rock ...")
print("paper...")
print("scissor...")

p1= input("please enter your choice :")

turn_choice=["rock","paper","scissor"]

turn=random.randint(0,2)
p2=turn_choice[turn]
print("comp choice "+ p2)
if p1 == "rock":
    if p2 == "paper":
        print("Comp wins")
    
    elif p2 == "scissor":
        print("player wins")

if p1 == "paper":
    if p2 == "scissor":
        print("Comp wins")

    elif p2 == "rock":
        print("Player wins")


if p1 == "scissor":
    if p2 == "paper":
        print("Player wins")

    elif p2 == "rock":
        print("Comp wins")

"""