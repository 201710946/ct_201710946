import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()
turnBy = 45

oldpos = t1.pos()
def shape(size) :
	oldHead = t1.heading()
	t1.fd(size)
	t1.rt(90)
	t1.fd(size)
	t1.penup()
	t1.setpos(oldpos)
	t1.setheading(oldHead + turnBy)
	t1.pendown()

for count in range (8) :
	shape(100)

wn.exitonclick()

#shape(100)
#shape(100)
#shape(100)
#shape(100)
#shape(100)
#shape(100)
#shape(100)
#shape(100)