from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def mov_fd():
    tim.fd(10)

screen.onkey(mov_fd, "space")

screen.exitonclick()