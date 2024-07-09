import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = { row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a name: ")
NATO_result = {data_dict[letter.upper()] for letter in user_input}


print(NATO_result)