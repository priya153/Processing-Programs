t1=3
t2=4
clr=10
x=random(t1)
y=random(t2)

def setup():
    size(500,500)
    background(0)

def draw():
    global x,t1,t2,clr,y
    background((noise(clr)*100))
    clr+=0.01;
    x=noise(t1)
    y=noise(t2)
    x*=500
    y*=500
    t1+=0.01
    t2+=0.01
    ellipse(x,y,30,30)
