from random import randint
from art import logo
from art import vs
from data import data
import sys
import os

#Get the parent directory path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from clear_screen import clear_screen

"""
1.get the data(two objects from list), randomly pick 2 for first cycle
    show the data with
    "name" "description" from "country"
2.ask the user to guess which one has more followers
3.  1.if the user guessed correctly compare new randomly selected
object with the previous winner object
    2.if the user guessed it wrong finish the game and show the score
    You scored: score
    Keep playing or exit game?
4.  1.in case of 3.1 keep repeating step 3.1 until guessed incorrectly (step 3.2)
    2.in case of 3.2 
       1. either exit game
       2. restart the game
"""


def play_game():
    print(logo)
    selected = []

    def select_random():
        while True:
            random_index = randint(0, len(data) - 1)
            if random_index in selected:
                continue
            selected.append(random_index)
            break
        return data[random_index]

    player1 = select_random()
    player2 = select_random()

    def check_answer(answer):
        answer = answer.upper()
        if player1["follower_count"] > player2["follower_count"]:
            return answer == "A"
        else:
            return answer == "B"

    user_guess = True

    score = 0
    while user_guess:
        print(f'Compare A: {player1["name"]}, a {player1["description"]} from {player1["country"]}')
        print(vs)
        print(f'Against B: {player2["name"]}, a {player2["description"]} from {player2["country"]}')
        user_answer = input("Who has more followers? Type 'A' or 'B': ")
        user_guess = check_answer(user_answer)
        if not user_guess:
            print("Wrong answer!")
            print(f"You scored: {score}")
            keep_playing = input(f"Type 'y' to keep playing or 'n' to exit the game: ")
            if keep_playing == "y":
                clear_screen()
                play_game()
        else:
            clear_screen()
            score += 1
            print(f"You're right! Current score: {score}.")
            player1 = player2
            player2 = select_random()


play_game()
