import os
bidder_data={}
print("********* Welcome to silent Auction program ********")
end=False
def find_winners(bid):
    highest=0
    winner=""
    for bidder,value in bid.items():
        price=value
        if price>highest:
            highest=price
            winner=bidder
    print(f"winner is {winner} with a bid price of {highest}")
    print("_"*20)

while not end:
    name=input('what\'s your name? ')
    price=int(input('What\'s your bid: '))

    bidder_data[name]=price

    more_bidders=input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if more_bidders=='no':
        end=True
        find_winners(bidder_data)
        for bidder,price in bidder_data.items():
            print(f"bidder is {bidder}, price: {price}")
    elif more_bidders=='yes':
        os.system('cls')