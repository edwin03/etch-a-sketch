from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def mov_fd():
    tim.fd(10)

def mov_lf():
    tim.seth(tim.heading()+10)

def mov_rh():
    tim.seth(tim.heading()-10)

def mov_dw():
    tim.backward(10)

def clear():
    tim.home()
    tim.clear()

screen.onkey(mov_fd, "w")
screen.onkey(mov_dw, "s")
screen.onkey(mov_lf, "a")
screen.onkey(mov_rh, "d")
screen.onkey(clear, "c")


screen.exitonclick()