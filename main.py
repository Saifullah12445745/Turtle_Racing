import random
import turtle
from turtle import Turtle,Screen


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "Make Your Bet",prompt = "Which turtle will win the race ? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtles =Turtle(shape ="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x= -230, y= y_position[turtle_index])
    all_turtles.append(new_turtles)


if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} turtle is the winner!")
            else:
                print(f"You have loss ! The {winning_color} turtle is the winner!")





        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()