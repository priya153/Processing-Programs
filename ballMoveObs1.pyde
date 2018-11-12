y=70;
xd=1;
x1=430;
def setup():
    smooth();
    size(500,500);
    noStroke();
    background(255);
    
def draw():
    global y,xd,x1;
    
    fill(0);
    background(255);
    ellipse(50,y,50,50);
    y=y+xd;
    if(y>width-200 or y<20):
        xd=-xd
    
    fill(0);
    rect(x1,50,50,50);
    x1=x1-xd;
    if(x1>width-20 or x1<20):
        xd=-xd
    line(0,100,width,100)
   
    
