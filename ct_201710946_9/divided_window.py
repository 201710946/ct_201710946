
# coding: utf-8

# In[1]:

import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
width = win.window_width()
print(win.window_width())
w3 = (width - 40) / 3


# In[2]:

x1 = 0.0 - w3
x2 = 0.0
x3 = 0.0 + w3
print(x1, x2, x3)


# In[3]:

t1.penup()
t1.goto(x1, 0)
t1.pendown()
t1.pos()


# In[4]:

t1.write(t1.pos())


# In[5]:

def giyuk(size) :
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)


# In[6]:

giyuk(100)


# In[7]:

t1.penup()
t1.goto(x2, 0)
t1.setheading(0)
t1.pendown()
t1.pos()


# In[8]:

t1.write(t1.pos())


# In[9]:

giyuk(100)


# In[10]:

t1.penup()
t1.goto(x3, 0)
t1.setheading(0)
t1.pendown()
t1.pos()


# In[11]:

t1.write(t1.pos())


# In[12]:

giyuk(100)


# In[13]:

def giyukAt(size, at) :
    t1.penup()
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.pos()
    t1.write(t1.pos())
    giyuk(size)


# In[14]:

t1.clear()


# In[15]:

giyukAt(100, x1)
giyukAt(100, x2)
giyukAt(100, x3)


# In[ ]:



