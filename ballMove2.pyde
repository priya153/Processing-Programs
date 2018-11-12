y=50;
xd=2;
def setup():
    smooth();
    size(500,300);
    noStroke();
    background(55);
    
def draw():
    global y,xd;
    
    fill(255);
    background(55);
    ellipse(150,y,50,50);
    y=y+xd;
    if(y>width-300 or y<20):
        xd=-xd
    
    fill(255);
    rect(0,200,width,50);
   
    
