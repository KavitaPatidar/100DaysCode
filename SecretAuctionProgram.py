from design import secret_auction_logo

print(secret_auction_logo)

print("Welcome to the Secret Auction Program")

bidder={}
def highest_bidder(bidder_dict):
    highest_bid=0
    for participant in bidder:
        bid=bidder[participant]
        if bid>highest_bid:
            highest_bid = bid
            winner= participant
    print(f"The winner is {winner} with the bid {highest_bid}.")

continue_bidding=True
while continue_bidding:
    participant= input("What is your name? ")
    bid_value = int(input("What's your bid? "))
    next_participant= input("Are there any other bidder? Type 'yes' or 'no'. ")
    bidder[participant]=bid_value

    if next_participant=="no":
        highest_bidder(bidder)
        continue_bidding=False



