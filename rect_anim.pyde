r=0;
backR=0;
backG=0;
backB=0;

def setup():
    global backR;
    global backG;
    global backB;
    size(700,500);
    backR = noise(0,100);
    backG = noise(0,100);
    backB = noise(0,100);
    
    background(backR, backG, backB);
    rectMode(CENTER);
    
    noStroke();
    smooth();
    
def draw():
    global r;
    fill(backR, backG, backB,50);
    rect(width/2,height/2,width, height);
    
    fill(255);
    translate(mouseX,mouseY);
    rotate(mouseX);
    rotate(r);
    rect(0,0,100,100);
    r+=5;
    
    
