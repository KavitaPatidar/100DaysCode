import random
from design import blackjack_logo

def start_game():
    # start = input("Do you want to play a game of blackjack? Type 'y' or 'n'\n").lower()
    # if start =="y":
    print(blackjack_logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards=[]
    computer_cards=[]


    user_cards= random.sample(cards, 2)
    user_current_score =  user_cards[0]+ user_cards[1]
    print(f"   Your score: {user_cards}, current score: {user_current_score}")

    computer_cards= random.sample(cards, 2)
    computer_current_score =  computer_cards[0]+ computer_cards[1]
    print(f"   Computer's first card: {computer_cards[0]}")

    play_continue= True
    while play_continue:
        if user_current_score<21:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
            # new_card = []
            if continue_game =="y" and user_current_score > 21:
                new_card = random.sample(cards, 1)
                user_cards = user_cards+new_card
                user_current_score= user_current_score + int(new_card[0])

                computer_new_card = random.sample(cards, 1)
                computer_cards = computer_cards + computer_new_card
                computer_current_score= computer_current_score + int(computer_new_card[0])

                print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                print ("You went over, you lose")
            elif continue_game =="y" and user_current_score <= 21:
                new_card = random.sample(cards, 1)
                user_cards = user_cards+new_card
                user_current_score= user_current_score + int(new_card[0])

                computer_new_card = random.sample(cards, 1)
                computer_cards = computer_cards + computer_new_card
                computer_current_score= computer_current_score + int(computer_new_card[0])

                print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's first card: {computer_cards[0]}")

            else:
                if user_current_score == computer_current_score:
                    print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                    print ("Draw")
                    play_continue = False

                elif user_current_score > 21:
                    print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                    print("You went over, you lose")
                    play_continue = False
                elif user_current_score<=21 and user_current_score >computer_current_score:
                    print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                    print ("You win")
                    play_continue = False
                elif user_current_score<=21 and computer_current_score >21:
                    print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                    print ("You win")
                    play_continue = False
                else:
                    print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
                    print ("You lose")
                    play_continue = False

        elif user_current_score==21:
            print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
            print ("Win with blackjack.")
            play_continue = False

        else:
            print(f"   Your final hand: {user_cards}, final score: {user_current_score} \n  Computer's final hand: {computer_cards}, final score: {computer_current_score}")
            print("You went over, you lose")
            play_continue = False

while input("Do you want to play a game of blackjack? Type 'y' or 'n':\n")=="y":
    start_game()
