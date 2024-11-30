from snake import Snake
from turtle import Screen
from food import Food
from scoreBoard import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

s1 = Snake()
f1 = Food()
score_obj = Score()

screen.listen()

screen.onkey(s1.move_up, "Up")
screen.onkey(s1.move_down, "Down")
screen.onkey(s1.move_left, "Left")
screen.onkey(s1.move_right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    s1.move()

    # Check for collision
    if s1.head.distance(f1) < 15:
        f1.refresh()
        s1.extend()
        score_obj.score += 1
        score_obj.update()

    if s1.head.xcor() > 280 or s1.head.xcor() < -280 or s1.head.ycor() > 280 or s1.head.ycor() < -280:
        score_obj.reset()
        s1.reset()

    for segment in s1.segments[1:]:
        if s1.head.distance(segment) < 10:
            score_obj.reset()
            s1.reset()

screen.exitonclick()
