from art import logo
from random import randint

print(logo)
print("Let's play 'Guess the number between 1 and 100' game")
level = input("Choose a level: 'easy' or 'difficult'. Type 'e' for easy and 'd' for difficult: ")
game_num = randint(1,100)

if level == 'e':
    attempts = 10
elif level == "d":
    attempts = 5
else:
    print("Unknown level, game ends!")
    quit()
game_ends = False

def check_for_match(guessed_num):
    print(game_num)
    if guessed_num < game_num:
        print("Too low")
        return False
    elif guessed_num > game_num:
        print("Too high")
        return False
    else:
        print(f"You got it, the number was {game_num}")
        return True

while attempts and not game_ends:
    print(f"You have {attempts} remaining to guess the number.")
    guessed_num = int(input("Make a guess: "))
    game_ends = check_for_match(guessed_num)
    attempts -= 1
if not attempts and not game_ends:
    print("You ran out of attempts. Game ends. You loose (")