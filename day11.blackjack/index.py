# cards 2 - 6 count the same as their values
# cards J, Q and K count as 10
# card Ace is 1 or 11
import random
from art import logo
print(logo)
print("Let's play blackjeck")
#initial list of cards
cards_list = [{
    "name":"2",
    "value":2,
    },
    {
    "name":"3",
    "value":3,
    },
    {
    "name":"4",
    "value":4,
    },
    {
    "name":"5",
    "value":5,
    },
    {
    "name":"6",
    "value":6,
    },
    {
    "name":"7",
    "value":7,
    },
    {
    "name":"8",
    "value":8,
    },
    {
    "name":"9",
    "value":9,
    },
    {
    "name":"10",
    "value":10,
    },
    {
    "name":"Jack",
    "value":10,
    },
    {
    "name":"Queen",
    "value":10,
    },
    {
    "name":"King",
    "value":10,
    },
    {
    "name":"Ace",
    "value":[1,11],
    }]
#remove the occurence of card or cards from card list 
#to avoid repetition 
def remove_used_cards(used_cards_list):
    for card in used_cards_list:
        if card in cards_list:
            cards_list.remove(card)

def pick_cards(count):
    #pick count amount of cards from cards list
    picked_cards = random.sample(cards_list, count)
    #remove chosen cards from list so that cards are always unique
    remove_used_cards(picked_cards)
    return picked_cards
#pick two cards for both the dealer and the user
dealer_cards = pick_cards(2)
user_cards = pick_cards(2)


def count_sum(cards, initial_sum = 0):
    sum = initial_sum
    add_ace = False
    for card in cards:
        #if cards have "Ace" 
        #count the total for the rest
        #and add 1 in case total can exceed 21
        #otherwise add 11
        if card["name"] == "Ace":
            add_ace = True
        else:
            sum += card["value"]
    if add_ace:
        if sum + 11 <= 21:
            sum += 11
        else:
            sum += 1
    return sum

def card_names(cards):
    names_to_reveal = []
    for card in cards:
        names_to_reveal.append(card["name"])
    return names_to_reveal

#stand is the value for user to stop taking cards
stand = False
#hit is the value for user to take more cards
hit = True

while hit:
    user_total = count_sum(user_cards)
    dealer_total = count_sum([dealer_cards[1]])
    print("Your cards", card_names(user_cards),
      "Total: ", user_total )

    print("Dealer cards", card_names([dealer_cards[1]]),
      "Total: ", dealer_total)
    if user_total == 21:
        hit = False
        print("Black Jack")
        print("You win!")
    elif count_sum(dealer_cards) == 21:
        hit = False
        print("Black Jack")
        print("Dealer wins!")
    elif user_total < 21:
        user_answer = input("Type 'y' for HIT and 'n' for STAND: ")
        if(user_answer == 'y'):
            card_to_add = pick_cards(1)
            user_cards += card_to_add
            user_total = count_sum(card_to_add, user_total)
        elif (user_answer) == "n":
            hit = False
            stand = True
        else:
            hit = False
            print("Invalid answer, game ends!")
            quit()
    else:
        print("You went over 21, You loose")
        hit = False
        stand = False
       
if stand:
    print(user_total)
    print(card_names(dealer_cards))
    dealer_total = count_sum(dealer_cards)
    while dealer_total < 17:
        card_to_add = pick_cards(1)
        dealer_cards += card_to_add
        dealer_total = count_sum(card_to_add, dealer_total)
        print(card_names(dealer_cards))
        if(dealer_total < 17):
            print(f"Dealer total: {dealer_total}")

    print(f"Dealer total: {dealer_total}")
    print(f"User total: {user_total}") 
    if dealer_total > 21 or dealer_total < user_total:
        print("You win")   
    elif dealer_total > user_total:
        print("You loose")
    else:
        print("Draw")



