import os
path = os.getcwd() + "/"

class Creature:
    def __init__(self, x, y, r, g, img, w, h, F):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.img = loadImage(path + "images/"+img)
        self.w = w
        self.h = h
        self.f = 0
        self.F = F
        self.direction = 1
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
        
        if self.direction == 1:
            image(self.img,self.x-self.w//2, self.y -self.h//2, self.w, self.h, int(self.f) * self.w, 0, (int(self.f) +1)* self.w, self.h )
        elif self.direction == -1:
            image(self.img,self.x-self.w//2, self.y -self.h//2, self.w, self.h, (int(self.f) +1) * self.w, 0,  int(self.f) * self.w, self.h )
            
        # noFill()    
        # ellipse(self.x, self.y,self.r*2, self.r*2)
        stroke(0)
        strokeWeight(5)
        line(self.x-self.r, self.g, self.x+self.r, self.g)
    
class Mario(Creature):
    def __init__(self, x, y, r, g, img, w, h, F):
        Creature.__init__(self,x, y, r, g, img, w, h, F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        
    def update(self):
        self.gravity()

        if self.vx != 0:
            self.f = (self.f + .2) % self.F
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.direction = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.direction = 1
        else:
            self.vx = 0
            # self.direction = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.vy = -15
            
        self.x += self.vx
        self.y += self.vy

class Game:
    def __init__(self, w, h, g):
        self.w = w
        self.h = h
        self.g = g
        self.mario = Mario(50,50, 35, self.g, "mario.png", 100, 70, 11)
    
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

def keyPressed():
    if keyCode == LEFT:
        g.mario.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.mario.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.mario.keyHandler[UP] = True
        
def keyReleased():
    if keyCode == LEFT:
        g.mario.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.mario.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.mario.keyHandler[UP] = False
