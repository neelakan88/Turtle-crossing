from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# player class is the turtle which tries to cross the road
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    #method for putting the turtle back after he scores
    def back_to_start(self):
        self.goto(STARTING_POSITION)
        
    #method for moving
    def move_up(self):
        self.forward(MOVE_DISTANCE)

        


