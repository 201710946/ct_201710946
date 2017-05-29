
# coding: utf-8

# In[1]:

import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()


# In[2]:

width = wn.window_width()
w3 = width / 3


# In[3]:

x1 = 0.0 - w3
x2 = 0.0
x3 = 0.0 + w3


# In[4]:

def drawTriangleAt(size, at) :
    t1.penup()
    t1.goto(at, 0)
    t1.pendown()
    t1.write(t1.pos())
    for count in range(3) :
        t1.fd(size)
        t1.lt(120)


# In[5]:

def drawPentagonAt(size, at) :
    t1.penup()
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    for count in range(5) :
        t1.fd(size)
        t1.lt(72)


# In[6]:

def drawStarAt(size, at) :
    t1.penup()
    t1.goto(at, 0)
    t1.pendown()
    t1.setheading(36)
    t1.write(t1.pos())
    for count in range(5) :
        t1.fd(size)
        t1.lt(144)


# In[7]:

drawTriangleAt(100, x1)


# In[8]:

drawPentagonAt(100, x2)


# In[10]:

drawStarAt(100, x3)


# In[ ]:

wn.exitonclick()

