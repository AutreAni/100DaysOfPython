BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import choice
# read data as dict
data = None
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    if data is not None:
        data_list = pandas.DataFrame.to_dict(data,orient="records")

# get random card
timer = None
current_card = {}
def shuffle_cards():
    global timer, current_card
    if timer is not None:
        window.after_cancel(id = timer)
    current_card = choice(data_list)
    front.itemconfig(card_bg, image=front_image)
    front.itemconfig(card_title, text = "french", fill=  "black")
    front.itemconfig(card_text, text = current_card["French"],fill=  "black")
    timer = window.after(3000, func=flip)

# flip card to english
def flip():
    front.itemconfig(card_bg, image=back_image)
    front.itemconfig(card_title, text = "English", fill = "white")
    front.itemconfig(card_text, text = current_card["English"], fill = "white")

# remove the known words from list and shuffle
def remove_and_shuffle():
    data_list.remove(current_card)
    pandas.DataFrame(data_list).to_csv("data/words_to_learn.csv", index=False)
    shuffle_cards()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# background image for the front of the card
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
# front of the card
front = Canvas( width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
# set the image as bg for the front
card_bg = front.create_image(0, 0, image = front_image,anchor = "nw")

# add texts
card_title = front.create_text(400, 150, font=("Ariel", 40, "italic"))
card_text = front.create_text(400, 265, font=("Ariel", 60, "bold"))

# takes whole width
front.grid(column = 0, row = 0, columnspan = 2)
# create images for right or wrong buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# create right or wrong buttons
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0,command = remove_and_shuffle )
wrong_button = Button(image=wrong_image, highlightthickness=0,borderwidth=0,command = shuffle_cards)
right_button.grid(column = 1, row = 1, )
wrong_button.grid(column = 0, row = 1, )
shuffle_cards()
window.mainloop()
