with open("Input/StartingLetter/letter.txt") as starting_letter:
    starting_letter = starting_letter.read()

with open("Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()
    print(names_list)
    for name in names_list:
        name = name.strip()
        new_letter = starting_letter.replace("[name]", name)
        with open(f'Output/ReadyToSend/letter_to_'+ name+'.txt', mode="w") as file:
            file.write(new_letter)
