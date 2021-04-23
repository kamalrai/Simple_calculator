import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
pen.fillcolor('pink')
pen.pensize(5)
pen.speed(69)

pen.begin_fill()
def drawCircle(x,y,r):
    pen.pu()
    pen.goto(x,y-r)
    pen.pd()
    pen.circle(r)
'''for i in range(20,220,20):
    drawCircle(0,0,200)'''
def makePicture(r):
    if r<20:
        pass
    else:
        drawCircle(0,0,r)
        makePicture(r-20)

makePicture(200)

pen.end_fill()
turtle.done()