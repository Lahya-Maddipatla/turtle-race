from turtle import *
import random
s=Screen()
is_race_on=True
s.setup(500,400)
colors=["pink","red","green","yellow","orange","violet"]
y_positions=[-70,-40,-10,20,50,80]
user_bet=s.textinput(title="Make your bet",prompt="which color will win the race?Enter a color:?")
all_turtles=[]
for i in range(6):
    t=Turtle()
    t.shape("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230,y_positions[i])
    all_turtles.append(t)
    t.speed("fastest")
if user_bet:
    is_race_on=True
while is_race_on:
    for i in all_turtles:
        if i.xcor()>230:
            i.penup()
            i.goto(0,0)
            is_race_on=False
            winning_color=i.pencolor()
            if winning_color==user_bet:
                print(f"You won the {winning_color} turtle color")
            else:
                print(f"You lose the {winning_color} turtle color")
        rand_distance=random.randint(0,10)
        i.forward(rand_distance)
        
s.exitonclick()