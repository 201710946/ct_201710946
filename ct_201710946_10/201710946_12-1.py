
# coding: utf-8

# In[1]:

import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()


# In[2]:

def drawSquareAt(x, y, size) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    for i in range(4) :
        t1.fd(size)
        t1.rt(90)


# In[3]:

def drawTriangleAt(x, y, size) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    for i in range(3) :
        t1.fd(size)
        t1.rt(120)


# In[4]:

def drawStarAt(x, y, size) :
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.setheading(36)
    for i in range(5) :
        t1.fd(size)
        t1.rt(144)


# In[5]:

drawSquareAt(50, 50, 100)


# In[6]:

drawTriangleAt(-50, -50, 100)


# In[7]:

drawStarAt(100, - 100, 100)


# In[ ]:



