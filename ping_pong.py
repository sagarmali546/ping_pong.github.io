import turtle
import winsound

wn = turtle.Screen() #window
wn.title("PING PONG")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) #stop window updating



#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #Turtle() is a class name
paddle_a.speed(0)  #speed of turtle animation module, set speed as a max possible speed
paddle_a.shape("square") #builtin shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #Sets the current pen state to PENUP. Turtle will move around the screen, but will not draw when its pen state is PENUP. The turtle's default pen state is PENDOWN.
paddle_a.goto(-350, 0) #paddle a position x=-350 and y=0 at left side




#Paddle B
paddle_b = turtle.Turtle() #Turtle() is a class name
paddle_b.speed(0)  #speed of turtle animation module, set speed as a max possible speed
paddle_b.shape("square") #builtin shape
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #Sets the current pen state to PENUP. Turtle will move around the screen, but will not draw when its pen state is PENUP. The turtle's default pen state is PENDOWN.
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle() #Turtle() is a class name
ball.speed(0)  #speed of turtle animation module, set speed as a max possible speed
ball.shape("circle") #builtin shape
ball.color("red")
ball.penup() #Sets the current pen state to PENUP. Turtle will move around the screen, but will not draw when its pen state is PENUP. The turtle's default pen state is PENDOWN.
ball.goto(0, 0)
ball.dx = 0.1 #ball moves with 2px if x positive then righ or if negative left
ball.dy = -0.1 #ball moves with 2px if y positive then up or if negative then down

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal") )



#function
def paddle_a_up():
    y = paddle_a.ycor() #ycor() returns y coordinate
    y += 20 #add 20px to y coordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #ycor() returns y coordinate
    y -= 20 #add 20px to y coordinate
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() #ycor() returns y coordinate
    y += 20 #add 20px to y coordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #ycor() returns y coordinate
    y -= 20 #add 20px to y coordinate
    paddle_b.sety(y)

def quit():
     turtle.bye()




#keyboard binding
wn.listen() #listen the keyboard input
wn.onkeypress(paddle_a_up, "w") #assigning w key for up and used a function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit, "q")

#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1 #reverse the direction of the ball on upper side
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverse the direction of the ball on bottom side
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)








