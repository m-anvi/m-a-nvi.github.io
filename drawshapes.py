from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)


### Write your code below:
#defines sides, collects input
sides = int(input('how many sides?'))
color = input('what color?')

# for loop to draw shape based on input
fillcolor(color)
begin_fill()
for x in range(sides):
    forward(50)
    left(360 / sides)
end_fill()
# Close window on click
exitonclick()
