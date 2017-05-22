
# coding: utf-8

# In[1]:

import turtle


# In[2]:

wn = turtle.Screen()


# In[3]:

t1 = turtle.Turtle()


# In[4]:

def giyuk(size) :
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)


# In[5]:

giyuk(100)


# In[6]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[7]:

def nieun(size) :
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)


# In[8]:

nieun(100)


# In[9]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[10]:

def diguet(size) :
    t1.setheading(180)
    t1.fd(size/2)
    giyuk(size/2)
    giyuk(size/2)
    t1.fd(size/2)


# In[11]:

diguet(100)


# In[12]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[13]:

def rieul(size) :
    t1.setheading(0)
    giyuk(size)
    t1.rt(90)
    t1.fd(size)
    t1.lt(180)
    nieun(size)


# In[14]:

rieul(100)


# In[15]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[16]:

def mieum(size) :
    giyuk(size)
    t1.penup()
    t1.home()
    t1.pendown()
    nieun(size)


# In[17]:

mieum(100)


# In[18]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[19]:

def giyukAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(size)


# In[20]:

giyukAt(-100,100,100)


# In[21]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[22]:

def nieunAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    nieun(size)


# In[23]:

nieunAt(100,-100,100)


# In[24]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[25]:

def mieumAt(x,y,size) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(size)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.lt(90)
    nieun(size)


# In[ ]:

mieumAt(100,100,100)


# In[ ]:

wn.exitonclick()

