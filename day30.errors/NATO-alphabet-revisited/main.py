import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = { row.letter: row.code for (index, row) in data.iterrows()}

valid_input = False

isValid = False
while not isValid:
    user_input = input("Enter a name: ")
    try:
        NATO_result = {data_dict[letter.upper()] for letter in user_input}
    except KeyError as error_key:
        print(f"The character {error_key} is not valid. Enter alphabetical letters only.")
    else:
        print(NATO_result)
        isValid = True