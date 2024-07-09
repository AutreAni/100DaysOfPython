import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Text Input Example")

# Create a turtle
pen = turtle.Turtle()
pen.hideturtle()

# Function to move the turtle to the top left corner
def move_to_top_left():
    screen.tracer(0)  # Turn off screen updates
    pen.penup()
    pen.goto(-screen.window_width() // 2 + 20, screen.window_height() // 2 - 40)  # Position in the top left corner
    pen.pendown()
    pen.write("Please enter your text below:", align="left", font=("Arial", 14, "normal"))
    screen.tracer(1)  # Turn on screen updates

# Move the turtle to the top left corner and show the message
move_to_top_left()

# Show the text input prompt
user_input = screen.textinput("Input", "Enter your text:")

# Display the user input on the screen
pen.penup()
pen.goto(-screen.window_width() // 2 + 20, screen.window_height() // 2 - 80)  # Position below the initial message
pen.pendown()
pen.write(f"You entered: {user_input}", align="left", font=("Arial", 14, "normal"))

# Hide the turtle and complete
pen.hideturtle()
turtle.done()
