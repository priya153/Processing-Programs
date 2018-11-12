def setup():
    size(500,400);
    
def draw():
    fill(225)
    rect(0,0,width,height);
    fill(51);
    rect(100,50,100,100); #face
    rect(135,150,30,130); #body
    rect(70,165,65,30); #left hand
    rect(165,165,65,30); #right hand
    rect(70,250,65,30); #left leg
    rect(165,250,65,30); #right leg
    fill(255);
    ellipse(130,83,15,30); #left eye
    ellipse(167,83,15,30); #right eye
    fill(20,230)
    ellipse(150,128,20,20); #mouth
    
    print(mouseX,mouseY);
