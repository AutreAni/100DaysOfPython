import random
from art import HANGMANPICS
from art import words
from art import logo

print(logo)
initial_score = 0
random_word = random.choice(words)
print(random_word)
blanks = ["-"for _ in random_word]
guessed_letters = []
while initial_score < 7 and "-" in blanks:
    print(" ".join(blanks))
    user_answer = input("Guess a letter:\n")
    print(chr(27) + "[2J")
    indices = []
    if user_answer.lower() in guessed_letters:
        print("You already guessed that letter before.")
        
        continue
    for index,char in enumerate(random_word):
        if user_answer.lower() == char:
            indices.append(index)
    if len(indices):
        for char in indices:
            blanks[char] = user_answer
        print("Good guess")
        if not "-" in blanks:
            print("Final word:", " ".join(blanks))
            print("You win")
    else:
        print(HANGMANPICS[initial_score])
        initial_score += 1
        if initial_score == 7:
            print("You loose")
    guessed_letters.append(user_answer)