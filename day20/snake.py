import turtle
DEF_FORW = 20
class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.position = [(-0,0), (-20,0), (-40,0)]
        for snake_seg in self.position:
            self.add_segment(snake_seg)

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed(1)
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.xcor = self.segments[seg_num - 1].xcor()
            self.ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=self.xcor, y=self.ycor)
        self.segments[0].fd(DEF_FORW)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)