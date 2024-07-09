from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
ORIENTATION = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def initial(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for pos in POSITIONS:
            self.add_square(pos)

    def add_square(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.setpos(position)
        self.segments.append(square)

    def refresh(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def extend(self):
        self.add_square(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(10)

    def set_direction(self, direction):
        heading_coord = int(self.head.heading())
        if ((heading_coord == ORIENTATION["up"] or heading_coord == ORIENTATION["down"]) and (
                direction == "left" or direction == "right")) or (
                (heading_coord == ORIENTATION["left"] or heading_coord == ORIENTATION["right"]) and (
                direction == "up" or direction == "down")):
            self.head.setheading(ORIENTATION[direction])

    def left(self):
        self.set_direction("left")

    def right(self):
        self.set_direction("right")

    def up(self):
        self.set_direction("up")

    def down(self):
        self.set_direction("down")
