x=50;
xd=1;
def setup():
    smooth();
    size(500,500);
    #noStroke();
    #background(255);
    
def draw():
    global x,xd;
    fill(0);
    background(255);
    ellipse(x,70,50,50);
    x=x+xd;
    if(x>width-20 or x<20):
        xd=-xd
    fill(0);
    rect(0,100,width,50);
