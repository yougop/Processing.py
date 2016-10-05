# simple class object

class JitterBug(object):
    def __init__(self, tempX, tempY, tempDiameter, tempSpeed):
        self.x = tempX
        self.y = tempY
        self.diameter = tempDiameter
        self.speed = tempSpeed        
    def move(self):
        self.x += random(-self.speed, self.speed)
        self.y += random(-self.speed, self.speed)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
def settings():
    size(1300, 700)
    smooth()

bugs = []

def setup():
    background(200)
    for i in range(10):
        bugs.append( JitterBug(random(200, width-200), random(200, height-200), random(10, 60), random(4, 10) ) )    

def draw():
    for y in range( len(bugs) ):
        fill( random(255), random(255), random(255) )
        bugs[y].move()

def stop():
    print("Stopped")
    saveFrame()
