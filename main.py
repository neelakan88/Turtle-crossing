import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#define the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#set up scoreboard
score = Scoreboard()
score.update_score()

#create player
player = Player()


#define keystrokes
screen.listen()
screen.onkey(player.move_up, "Up")

#create cars?
cars = CarManager()
cars.create_cars()

#game variables
game_is_on = True
while game_is_on:
    time.sleep(0.1 /(1 +score.score)) #basically defining your x-axis resolution and time-constant simultaneously. You can make this the variable which changes the speed of the game and it also allows the player to get more clicks possibly?
    cars.move_cars()
    cars.manage_offscreen_cars()
    screen.update()
    if player.ycor() > 290:
        player.back_to_start()
        score.increase_score()
        score.update_score()
        # cars.increase_speed() ## this can be swapped out for a variable in time.sleep(). time.sleep() is key for making games as it defines your time constant / how many times you iterate through the code. i.e. time.sleep(0.1) iterates through the game 10x in a second
    for car in cars.cars:
        if abs(player.xcor() - car.xcor()) < 25 and abs(player.ycor() - car.ycor()) < 15:
            game_is_on = False
            player.write("Game Over")





screen.exitonclick()