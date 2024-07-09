from tkinter import *

window = Tk()
window.minsize(width =600, height =600)


label = Label(text="Greetings", font =("Arial", 20, "bold"))
label_text = "Greetings!"
label.grid(column=0, row = 0)

def change_label():
    global label_text
    label_text = text_input.get()
    label.config(text = label_text)

button = Button(text="Click here", command=change_label)
button.grid(column=1, row = 1)

new_button = Button(text="New button", command=change_label)
new_button.grid(column=2, row = 0)

text_input = Entry()
text_input.insert(0, "Placeholder")

text_input.grid(column=4, row = 2)

window.mainloop()