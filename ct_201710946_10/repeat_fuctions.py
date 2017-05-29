
# coding: utf-8

# In[1]:

import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()


# In[2]:

type(t1)


# In[3]:

def giyuk(t, size) :
    t.fd(size)
    t.rt(90)
    t.fd(size)


# In[4]:

giyuk(t1, 100)


# In[5]:

t1.penup()
t1.home()
t1.clear()
t1.pendown()


# In[6]:

def giyukBackHome(t, size) :
    oldPos = t.pos()
    oldHeading = t.heading()
    giyuk(t, size)
    t.penup()
    t.setpos(oldPos)
    t.setheading(oldHeading)
    t.pendown()


# In[7]:

for count in range(8) :
    turnby = 0
    giyukBackHome(t1, 100)
    turnby += 45
    t1.rt(turnby)


# In[8]:

print(range(0, 11))

for i in range(0, 11) :
    print '(', i+1, ')',i


# In[9]:

i = 1
while (i <= 10) :
    print i,
    i += 1


# In[10]:

sum = 0
i = 0
while (i <= 100) :
    sum += i
    i += 1
print(sum)


# In[11]:

t1.home()
t1.clear()


# In[12]:

for count in range(4) : 
    t1.fd(100)
    t1.rt(90)


# In[13]:

t1.home()
t1.clear()


# In[14]:

i = 0
while (i <= 3) :
    t1.fd(100)
    t1.rt(90)
    i += 1


# In[15]:

def drawSquare(size) :
    for count in range(4) : 
        t1.fd(size)
        t1.rt(90)


# In[16]:

drawSquare(100)


# In[ ]:



