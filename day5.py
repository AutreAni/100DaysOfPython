#py password generator
import random
password = ""
questions = [
    "How many letters would you like in your password? ",
    "How many symbols would you like? ",
    "How many numbers would you like? "
    #f"Here is your password: {password}"
]

user_answers = []
for question in questions:
    answer = input(question)
    print(answer)
    user_answers.append(int(answer))

letters_length, numbers_length, symbols_length = user_answers
letters = []
for _ in range(letters_length):
    char_num = random.randint(65, 122)
    letters.append(chr(char_num))

numbers = []
for _ in range(numbers_length):
    char_num = random.randint(48, 57)
    numbers.append(chr(char_num))

symbols = []
for _ in range(symbols_length):
    char_num = random.randint(58, 65)
    symbols.append(chr(char_num))

password = numbers + letters + symbols
random.shuffle(password)
password = "".join(password)
print(password)