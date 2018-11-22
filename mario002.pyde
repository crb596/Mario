

class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
    
    def display(self):
        fill(0,140,0)
        stroke(140)
        rect(0, self.g, self.w, self.h)
        

g = Game(1024,768,600)

def setup():
    size(g.w, g.h)
    background(255)
    
def draw():
    background(255)
    g.display()
