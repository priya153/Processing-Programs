def setup():
    size(600,500,P3D);
    
def draw():
    background(255);
    translate(250,250);
    fill(mouseX+55,mouseY+3,1000);
    rotate(mouseX);
    sphere(60);
