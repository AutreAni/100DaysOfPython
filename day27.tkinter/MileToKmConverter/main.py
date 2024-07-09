from tkinter import *

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100)

miles_input = Entry(width = 7)
miles_input.insert(0, "0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def miles_to_km():
    miles_str = miles_input.get()
    km = round(float(miles_str) * 1.609, 2)
    converted_label.config(text=str(km))

button = Button(text="Convert", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()