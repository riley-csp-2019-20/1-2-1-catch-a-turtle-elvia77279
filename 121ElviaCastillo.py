# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
turtleshape = "circle"
turtlesize = 2
turtlecolor = "green"
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False
score = 0

#-----initialize turtle-----
boop = trtl.Turtle (shape = turtleshape)
boop.color (turtlecolor)
boop.shapesize (turtlesize)
boop.speed(0)

score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-350,250)
score_writer.ht()
score_writer.clear()

font = ( "Ariel", 35, "bold")
score_writer.write(score, font = font)

counter =  trtl.Turtle()
font_setup = ("Arial", 20, "normal")

counter.ht()
counter.penup()
counter.goto(275,275)



#-----game functions--------
def turtle_clicky(x,y): 
    print("Boop got bopped")
    change_position()
    update_score()

def change_position():
    boop.penup()
    boop.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    boop.goto(new_xpos, new_ypos)
    boop.showturtle()

def update_score():
    global score
    score += 1  
    print(score)  
    score_writer.clear()
    score_writer.write(score, font=font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_over()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
def game_over(): 
    wn.bgcolor("red")
    boop.stamp()
    counter.ht()
    counter.goto(-450,0)
    counter.write("Game over. Thanks for playing!", font= font)

#-----events----------------
boop.onclick(turtle_clicky)
wn = trtl.Screen()
wn.bgcolor("violet")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()