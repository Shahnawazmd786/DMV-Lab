import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Bouncing Ball")
screen.bgcolor("white")
screen.tracer(0) # Turns off animation for manual updating

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)

# Movement speed
dx = 3
dy = 2

while True:
    screen.update() # Manually refresh the screen
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    # Check for wall collisions
    if ball.xcor() > 290 or ball.xcor() < -290:
        dx *= -1
    if ball.ycor() > 290 or ball.ycor() < -290:
        dy *= -1
    
    time.sleep(0.01)