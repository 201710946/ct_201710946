
# coding: utf-8

# In[1]:

import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()


# In[2]:

def drawSquareAtFill(x, y, size, color) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(4) :
        t1.fd(size)
        t1.rt(90)
    t1.end_fill()


# In[3]:

def drawTriangleAtFill(x, y, size, color) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(3) :
        t1.fd(size)
        t1.rt(120)
    t1.end_fill()


# In[4]:

def drawStarAtFill(x, y, size, color) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.setheading(36)
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(5) :
        t1.fd(size)
        t1.rt(144)
    t1.end_fill()


# In[5]:

drawSquareAtFill(50, 50, 100, "Red")


# In[6]:

drawTriangleAtFill(-50, -50, 100, "Blue")


# In[ ]:

drawStarAtFill(100, - 100, 100, "Black")


# In[ ]:

wn.exitonclick()

