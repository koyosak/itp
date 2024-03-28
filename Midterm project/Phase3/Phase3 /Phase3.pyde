def setup():
    size(400, 400) 
    fill(137, 169, 255)
    rect(0, 0, 400, 400)
    stroke(25, 50, 160)
    strokeWeight(1.5)


def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(255)
    
    beginShape()
    vertex(75, 150)
    bezierVertex(70, 120, 40, 80, 0, 75)
    bezierVertex(0, 75, 0, 150, 75, 150)
    endShape()
    
    beginShape()
    vertex(0, 75)
    bezierVertex(40, 70, 70, 40, 75, 0)
    bezierVertex(75, 0, 0, 0, 0, 75)
    endShape()
    
    beginShape()
    vertex(75, 0)
    bezierVertex(80, 40, 110, 70, 150, 75)
    bezierVertex(150, 75, 150, 0, 75, 0)
    endShape()
    
    beginShape()
    vertex(150, 75)
    bezierVertex(120, 80, 80, 120, 75, 150)
    bezierVertex(75, 150, 150, 150, 150, 75)
    endShape()
    
    pop()
    
def draw():
        drawObject(0,0,0.5)
        drawObject(0,200,0.5)
    
