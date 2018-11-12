time=0;

def setup():
    size(700,700)
    
def draw():
    global time;
    time+=0.1;
    strokeWeight(1);
    translate(width/2,height/2);
    
    ellipse(0,0,120,120);
    for i in range(12):
        pushMatrix();
        rotate(2*i*PI/12);
        line(80,0,100,0);
        popMatrix();
        
    beginShape();
    strokeWeight(4);
    rotate(time/12);
    line(0,0,55,0);
   # triangle(-2,55,2,55,0,55);
    endShape;
        
    beginShape();
    strokeWeight(2);
    rotate(time);
    line(0,0,0,-70);
    #triangle(-2,-70,2,-70,0,-77);
    endShape;
        
