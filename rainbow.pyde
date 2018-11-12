def setup():
    size(700,700)
    noFill();
    background('#04B1CE');
    
def draw():
    strokeWeight(random(3,10));
    stroke(random(255),random(255),random(255));
    r=random(600,750);
    ellipse(700,700,r,r); 
    delay(50);
