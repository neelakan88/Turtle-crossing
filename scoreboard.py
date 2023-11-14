from turtle import Turtle
FONT = ("Courier", 24, "normal")

#writes level we're on (top left) and game over sequence (center)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-250, 250)
        self.color("black")
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align = "left", font = FONT)

    def increase_score(self):
        self.score += 1


