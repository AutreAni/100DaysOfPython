import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]
choice_names = ["rock", "paper", "scissors"]
comp_choice_index = random.randint(0, len(choices) - 1)
your_choice = input(f"Please, choose among {", ".join(choice_names)}: ")
your_choice = your_choice.lower()
your_choice_index = choice_names.index(your_choice)
print("Your choice\n", choices[your_choice_index])
print("Computer choice\n", choices[comp_choice_index])
loose_msg = "You loose"
win_msg = "You win"
if your_choice_index  == comp_choice_index:
    print("Even")
elif your_choice_index  == 0:
    if comp_choice_index == 1:
        print(loose_msg)
    else:
        print(win_msg)
elif your_choice_index == 1:
    if comp_choice_index == 0:
        print(win_msg)
    else:
        print(loose_msg)
else:
    if comp_choice_index == 1:
        print(win_msg)
    else:
        print(loose_msg)