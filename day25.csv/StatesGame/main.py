import turtle
import pandas
screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_count = 50
user_score = 0
guessed_state_names = []
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

while len(guessed_state_names) != len(states_list):
    question = "Enter a state name" if len(guessed_state_names) == 0 else "What's another state name"
    answer = turtle.textinput(f"{user_score}/50 states correct",question)
    if answer is None:
        break
    else:
        answer = answer.title()
        if answer in guessed_state_names:
            print("You have already guessed that state name")
        elif answer in states_list:
            name = turtle.Turtle()
            name.penup()
            name.hideturtle()
            state_data = data[data.state == answer]
            name.goto(int(state_data.x), int(state_data.y))
            name.write(arg=state_data.state.item(), font=("Courier", 8, "normal"))
            user_score += 1
            guessed_state_names.append(answer)
        else:
            print("Wrong name")


if len(guessed_state_names) < len(states_list):
    # revisited after day26 - list comprehensions
    missed_names = [state for state in states_list if state not in guessed_state_names]
    pandas.DataFrame(missed_names).to_csv("states_to_learn.csv")




screen.exitonclick()