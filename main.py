from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def mov_fd():
    tim.fd(10)

def mov_lf():
    tim.seth(180)
    tim.fd(10)

def mov_rh():
    tim.seth(0)
    tim.fd(10)

def mov_dw():
    tim.seth(270)
    tim.fd(10)

def clear():
    screen.clearscreen()
    tim.home()

screen.onkey(mov_fd, "w")
screen.onkey(mov_dw, "s")
screen.onkey(mov_lf, "a")
screen.onkey(mov_rh, "d")
screen.onkey(clear, "c")


screen.exitonclick()