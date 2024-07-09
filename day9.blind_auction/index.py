# to clear print(chr(27) + "[2J")
from art import hammer
print(hammer)
print("Welcome to the secret auction program")
bids = {}
can_continue = ""
while not can_continue == "no":
    name = input("What is your name?\n")
    bid = input("What is your bid\n")
    if "$" in bid:
        bid = bid.split("$")[1]
    bid = int(bid)
    bids[name] = bid
    can_continue = input("Are there any bidders? Type 'yes' or 'no'\n")

max_bid = {
    "bid": 0
}
for key in bids:
    bid = bids[key]
    if bid > max_bid["bid"]:
        max_bid= {
            "name": key,
            "bid": bid
        }
print(f"The winner in this auction is {max_bid["name"]} with the bid ${max_bid["bid"]}")
