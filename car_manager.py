from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(20):
            self.add_car()

    def add_car(self, start_x = None):
        new_car = Turtle()
        new_car.up()
        new_car.hideturtle()  # Hide the turtle cursor
        if start_x is None:
            start_x = random.randint(-280, 280)
        new_car.goto(start_x, random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=0.75, stretch_len=1.5)
        self.cars.append(new_car)  # Add the new car to the cars list
        new_car.showturtle()  # Show the car turtle

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

   

    def manage_offscreen_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
                self.add_car(start_x = 300)
