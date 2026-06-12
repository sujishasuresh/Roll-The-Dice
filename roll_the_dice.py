# Roll the Dice Simulator
# A simple Python program that simulates rolling dice.
# Features:
# - Roll any number of dice
# - Session roll counter
# - Input validation

import random as r

count=0
while True:
    roll_die=[]
    ch=input("Roll the dice? (y/n): ")
    if ch=="y" or ch=="Y":
        try:
            dice=int(input("How many dice you want to roll? : "))
            if dice<=0:
                print("Please enter a positive number!")
            else:
                count+=1
                for i in range(dice):
                    die=r.randint(1,6)
                    roll_die.append(die)
                print(tuple(roll_die))
                print(f"You have rolled the dice {count} times")
        except ValueError:
            print("Please enter a valid number!")
        
    elif ch=="n" or ch=="N":
        
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")

