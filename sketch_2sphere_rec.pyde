speed = 5
x = 300
y = 700
def setup():
    #global viewport;
    size(700,700,P3D);
    background(255);
    #viewport = createGraphics(500,500);
    
def draw():
    lights();
    ambientLight(128,128,128);
    pushMatrix()
    background(255);
    move()
    display()
    popMatrix()
    pushMatrix()
    pointLight(10,10,200,0,100,200);
    # sphere1
    translate(150,350);
    rotate(y);
   # light(100)
    sphere(100);
    popMatrix()
    pushMatrix()
    pointLight(10,10,200,0,100,200);
    translate(500,350);
    fill(10,150,100);
    rotate(360-y);
    sphere(100);
    popMatrix()
    
  
  
  
def move():
    global y
    y = y - speed
    if y < 0:
        y = 700

def display():
    fill(1,100,200)
    rect(x,y,40,20)
