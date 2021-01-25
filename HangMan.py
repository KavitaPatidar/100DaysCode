import random
from design import word_list, logo, stages

print(logo)
word= random.choice(word_list)
print(word)
display=[]

for letter in word:
    # or display+= "_"
    display.append("_")
# print(display)
guess_continue= True
lives=6

while guess_continue:
    guess= input("guess a letter: ").lower()


    if guess in display:
        print(f"You have already guessed {guess}.")

    for n in range(len(word)):
        letter=word[n]
        if guess==letter:
            display[n]=guess

    print(f"{' '.join(display)}")

    if not guess in word:
        lives-=1
        print(f"Wrong guess. Now you have {lives} life rest.")

    if lives==0:
        print(f"The right word was {word}.")
        print("You lose!")
        guess_continue= False

    if not "_" in display:
        print("You won!")
        guess_continue= False

    print(stages[lives])


