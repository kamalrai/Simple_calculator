'''import turtle'''
from turtle import*
screen=Screen()
pen=Turtle()
pen.width(5)
pen.color('yellow')
pen.fillcolor('purple')
pen.begin_fill()

'''pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(500)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.left(90)
pen.forward(400)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(400)'''
pen.fillcolor('purple')

for i in range(5):
    pen.forward(300)
    pen.right(144)
pen.end_fill()
'''done()'''
screen.exitonclick()
