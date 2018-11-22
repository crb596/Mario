
class Creature:
    def __init__(self, x, y, r, g):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.vx = 0
        self.vy = 0
    
    def gravity(self):
        if self.y+self.r >= self.g:
            self.vy = 0
        else:
            self.vy += 0.4
            if self.y + self.r + self.vy > self.g:
                 self.vy = self.g - (self.y+self.r)
    
    def update(self):
        self.gravity()
        
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        stroke(255,0,0)
        noFill()    
        ellipse(self.x, self.y,self.r*2, self.r*2)
        stroke(0)
        strokeWeight(5)
        line(self.x-self.r, self.g, self.x+self.r, self.g)
    
    

class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Creature(50,50, 35, self.g)
    
    def display(self):
        fill(0,140,0)
        stroke(140)
        strokeWeight(1)
        rect(0, self.g, self.w, self.h)
        self.mario.display()
        

g = Game(1024,768,600)

def setup():
    size(g.w, g.h)
    background(255)
    
def draw():
    background(255)
    g.display()
