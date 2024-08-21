from turtle import Turtle, Screen
from random import *


screen = Screen()
screen.setup(width=500, height=400)

race_is_on = False

user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "brown", "gold", "green", "blue", "purple"]
start_point = [-75, -45, -15, 15, 45, 75]
all_turtles = []

for turtles in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtles])
    timmy.penup()
    timmy.goto(x=-230, y=start_point[turtles])
    all_turtles.append(timmy)

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor() > 100:
            race_is_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print("Congrats you won!")
            else:
                print("Sorry, you lost!")

screen.exitonclick()