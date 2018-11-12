x=50;
xd=1;
x1=430;

def setup():
    smooth();
    size(500,500);
    #noStroke();
    #background(255);
    
def draw():
    global x,xd,x1;
    fill(0);
    background(255);
    ellipse(x,70,50,50);
    x=x+xd;
    if(x>width-20 or x<20):
        xd=-xd
        
    fill(0);
    rect(x1,50,50,50);
    x1=x1-xd;
    if(x1>width-20 or x1<20):
        xd=-xd
    line(0,100,width,100)
