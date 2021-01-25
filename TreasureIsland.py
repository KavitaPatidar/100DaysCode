print("Welcome to Treasure Island. Your mission is to find Treasure.")

step1= input("where do you want ot go? left or right? \n").lower()

if step1=="left":
    step2= input("You are in the middle of river. Do you want to swim or wait?\n ")
    if step2=="wait":
        step3=input("You arrived at the island unharmed. There is a house with 3 doors. Red, Yellow and Blue. Which door do you want to go?\n").lower()
        if step3=="yellow":
            print("you win!")
        elif step3=="blue":
            print("you are at fire door. Game Over")
        elif step3=="red":
            print("Game Over")
        else:
            print("you entered wrong input. Game Over ")
    else:
        print("Game Over.")
else:
    print("Game Over.")

