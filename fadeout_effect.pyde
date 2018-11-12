def setup():
    size(500,500)
    background(0);
    noStroke();
    
def draw():
    fill(0,50);
    rect(0,0,width,height);
    
    fill(255);
    ellipse(random(width), random(height),10,10);
    delay(100);
