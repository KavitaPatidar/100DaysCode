print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()



t=name1.count("t")+name2.count("t")
r=name1.count("r")+name2.count("r")
u=name1.count("u")+name2.count("u")
e=name1.count("e")+name2.count("e")
true_score =t+r+u+e

l=name1.count("l")+name2.count("l")
o=name1.count("o")+name2.count("o")
v=name1.count("v")+name2.count("v")
e=name1.count("e")+name2.count("e")
love_score=l+o+v+e

score= int(str(true_score)+str(love_score))

if score<10 or score>90:
    print(f"Your score is {score} and you go together like coke and mentos.")
elif score<=50 and score>=40:
    print(f"Your score is {score} and you are alright together.")
else:
    print(f"Your score is {score}.")






