def setup():
    size(500,500);
    
def draw():
    fill(40,20)
    rect(0,0,width,height);
    
def keyPressed():
    fill(255);
    textSize(random(20,200));
    text(key, random(500), random(0,500));
