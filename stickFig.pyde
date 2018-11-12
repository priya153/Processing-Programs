def setup():
    global viewport;
    size(500,400);
    viewport = createGraphics (400,200);
def draw():
    fill(255);
    ellipse(200,100,60,60);
    line(201,131,201,235);
    line(201,151,145,165);
    line(201,151,251,164);
    line(201,206,245,224);
    line(201,206,150,224);
    
    print(mouseX,mouseY);
    viewport.beginDraw();
    viewport.background(255);
    viewport.noFill();
    image(viewport,120,200);
