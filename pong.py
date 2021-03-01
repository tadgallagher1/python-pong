import turtle

# create a screen
wn = turtle.Screen()
# give it a title
wn.title("Pong by Tim")
# change the background color
wn.bgcolor("blue")
#change size
wn.setup(width=800, height=600)
#stop window from updating
wn.tracer(0)

# score variables 
score_a = 0
score_b = 0


# paddle a
paddle_a = turtle.Turtle()
#set max speed of animation (not paddle speed)
paddle_a.speed(0)
# set shape
paddle_a.shape("square")
# set color
paddle_a.color("red")
# omits line on screen
paddle_a.penup()
# set x and y coordinates
paddle_a.goto(-350, 0)
# make paddle 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# paddle b
paddle_b = turtle.Turtle()
#set max speed of animation (not paddle speed)
paddle_b.speed(0)
# set shape
paddle_b.shape("square")
# set color
paddle_b.color("red")
# omits line on screen
paddle_b.penup()
# set x and y coordinates
paddle_b.goto(350, 0)
# make paddle 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# ball 
ball = turtle.Turtle()
#set max speed of animation (not paddle speed)
ball.speed(0)
# set shape
ball.shape("turtle")
# set color
ball.color("white")
# omits line on screen
ball.penup()
# set x and y coordinates
ball.goto(0, 0)
# move ball by 2 pixels - you may need to adjust this based on your computer
# try .1 or 2 or something else
# note there is an x and y movement
ball.dx = .1
ball.dy = .1

# Pen - for Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Function - Paddle A Up
def paddle_a_up():
    #need to know the current coordinates for paddle a and assign to variable y
    y = paddle_a.ycor()
    # add 20 to y coordinate
    y += 20
    # set the new coordinate for a
    paddle_a.sety(y)

# Function - Paddle A Down
def paddle_a_down():
    #need to know the current coordinates for paddle a and assign to variable y
    y = paddle_a.ycor()
    # add 20 to y coordinate
    y -= 20
    # set the new coordinate for a
    paddle_a.sety(y)    


def paddle_b_up():
    #need to know the current coordinates for paddle b and assign to variable y
    y = paddle_b.ycor()
    # add 20 to y coordinate
    y += 20
    # set the new coordinate for b
    paddle_b.sety(y)

# Function - Paddle B Down
def paddle_b_down():
    #need to know the current coordinates for paddle b and assign to variable y
    y = paddle_b.ycor()
    # add 20 to y coordinate
    y -= 20
    # set th new coordinate for b
    paddle_b.sety(y)    


# keyboad binding
wn.listen()
# create an event for paddle A up
wn.onkeypress(paddle_a_up, key="w")    
# create an event for paddle A down
wn.onkeypress(paddle_a_down, key="s")  
# create an event for paddle B up
wn.onkeypress(paddle_b_up, key="Up")    
# create an event for paddle B down
wn.onkeypress(paddle_b_down, key="Down")   


# main loop
while True:  

  
 #  pen.clear
 #  pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    wn.update()
    # move the ball (add each time)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border top check
    if ball.ycor() > 290:
        # reset
        ball.sety(290)
        # reverse direction
        ball.dy *= -1
        #ball.goto(0, 0)

    # border bottom  check
    if ball.ycor() < -290:
        # reset
        ball.sety(-290)
        # reverse direction
        ball.dy *= -1
        #ball.goto(0, 0)

    # Right border
    if ball.xcor() > 390:
        # move ball to center
        ball.goto(0, 0)
        # reverse direction
        ball.dx *= -1
        # add point/score to player a
        score_a += 1
        

    # left border
    if ball.xcor() < -390:
        # move ball to center
        ball.goto(0, 0)
        # reverse direction
        ball.dx *= -1
        # add point/score to player a
        score_b += 1
      

    # Paddle and ball collision - left side (paddle b)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        # move to the left 
        ball.setx(340)
        # make it bounce the opposite direction 
        ball.dx *= -1
        ball.goto(0, 0)

    # Paddle and ball collision - right side (paddle a)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        # move to the left 
        ball.setx(340)
        # make it bounce the opposite direction 
        ball.dx *= -1  
        ball.goto(0, 0)