from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
initial_timer_text = "00:00"
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def rest_timer():
    global rep

    title.config(text="TIMER", fg=GREEN)
    rep = 0
    checkmark.config(text="")
    canvas.itemconfig(count_timer, text = initial_timer_text)
    window.after_cancel(id=timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    working_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep % 2 and rep != 7:
        count_down(short_break_sec)
        title.config(text="Short break", fg=RED)
        old_text = checkmark.cget("text")
        checkmark.config(text=old_text + "✔")

    elif  rep == 7:
        title.config(text="Long break", fg=PINK)
        count_down(long_break_sec)
        checkmark.config(text="✔✔✔✔")
    else:
        count_down(working_sec)
        title.config(text="Work", fg=GREEN)
    rep += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    # count_min_str = "0" + str(count_min) if count_min < 10 else str(count_min)
    count_sec = "0" + str(count_sec) if count_sec < 10 else str(count_sec)
    canvas.itemconfig(count_timer, text=f"{count_min}:{count_sec}")
    if count:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# create and set up window
window = Tk()
window.config(padx=100, pady = 100, bg=YELLOW)
window.title("Pomodoro App")

# create and set up canvas
canvas = Canvas(width=600, height = 250, bg = YELLOW, highlightthickness=0)

# add Timer label


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
title.grid(column=1, row=0)
# set background to tomato image
bg_image = PhotoImage(file='tomato.png')
canvas.create_image(300, 112, image=bg_image)

# add clock text
count_timer = canvas.create_text(300, 132, text=initial_timer_text, font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# add start and reset buttons
start_btn = Button(text="Start", command=start_timer, border = 0,font = (FONT_NAME, 12, "bold"), pady=5, padx=10, fg ="white", bg=PINK)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset",command=rest_timer, border = 0,font = (FONT_NAME, 12, "bold"), pady=5, padx=10, fg ="white", bg=PINK)
reset_btn.grid(column=2, row=2)
# add checkmarks

for _ in range(rep + 1):
    checkmark = Label(text ="", bg=YELLOW, fg=GREEN)
    checkmark.grid(column=1, row =3)


window.mainloop()