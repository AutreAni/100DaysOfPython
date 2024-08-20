from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message = "All the fields are required!")
    else:
        save = messagebox.askokcancel(title=website, message="Do you want to save these details?")
        if save:
            text =  website+"|"+email+"|"+password + "\n"
            with open(file="data.txt", mode="a") as file:
                file.write(text)
            website_entry.delete(0, "end")
            password_entry.delete(0,"end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100,image=image)
canvas.grid(column=1, row=0,columnspan=2)
# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label= Label(text="Password:")
password_label.grid(column=0, row=3)
# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "dohndoe@gmail.com")

password_entry= Entry(width=22)
password_entry.grid(column=1, row=3)

# buttons
generate_btn = Button(text="Generate", width=10, borderwidth=0, command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text = "Add", width=30,
                 command = save_data
                 )
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()