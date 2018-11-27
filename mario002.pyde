add_library('minim')
import os, random
path = os.getcwd() + "/"
player = Minim(this)

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
        
        for p in g.platforms:
            if self.y + self.r <= p.y and self.x+self.r >= p.x and self.x-self.r <= p.x+p.w:
                self.g = p.y
                break
            self.g = g.g
    
    def update(self):
        self.gravity()
    
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        stroke(255,0,0)
        
        if self.direction == 1:
            image(self.img,self.x-self.w//2 - g.x , self.y -self.h//2, self.w, self.h, int(self.f) * self.w, 0, (int(self.f) +1)* self.w, self.h )
        elif self.direction == -1:
            image(self.img,self.x-self.w//2 - g.x, self.y -self.h//2, self.w, self.h, (int(self.f) +1) * self.w, 0,  int(self.f) * self.w, self.h )
        
        if self.vx != 0:
            self.f = (self.f + .2) % self.F
            
        # noFill()    
        # ellipse(self.x, self.y,self.r*2, self.r*2)
        # stroke(0)
        # strokeWeight(5)
        # line(self.x-self.r, self.g, self.x+self.r, self.g)
    
class Mario(Creature):
    def __init__(self, x, y, r, g, img, w, h, F):
        Creature.__init__(self,x, y, r, g, img, w, h, F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.jumpSound = player.loadFile(path + "sounds/jump.mp3")
        
    def update(self):
        self.gravity()
        
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
            self.jumpSound.rewind()
            self.jumpSound.play()
            self.vy = -15
            
        if self.x - self.r < 0:
            self.x = self.r 
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x >= g.w//2:
            g.x += self.vx

class Gomba(Creature):
    def __init__(self, x, y, r, g, img, w, h, F, xL, xR):
        Creature.__init__(self,x, y, r, g, img, w, h, F)
        self.xL = xL
        self.xR = xR
        self.vx = random.randint(1,5)
        
    def update(self):
        self.gravity()
    
        if self.x > self.xR:
            self.vx *= -1
            self.direction = -1
        elif self.x < self.xL:
            self.vx *= -1
            self.direction = 1
        
        self.x += self.vx
        self.y += self.vy
        

class Platform:
    def __init__(self,x,y, w, h, img):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+"images/"+img)
    
    def display(self):
        # fill(130, 95, 1)
        # rect(self.x, self.y, self.w, self.h)
        image(self.img, self.x - g.x, self.y, self.w, self.h)
        
class Game:
    def __init__(self, w, h, g):
        self.x = 0
        self.w = w
        self.h = h
        self.g = g
        self.pause = False
        self.pauseSound = player.loadFile(path + "sounds/pause.mp3")
        self.bgSound = player.loadFile(path + "sounds/background.mp3")
        self.bgSound.play()
        self.bgSound.loop()
        self.mario = Mario(50,50, 35, self.g, "mario.png", 100, 70, 11)
        
        self.bgImgs = []
        for i in range(5,0,-1):
            self.bgImgs.append(loadImage(path+"images/layer_0" + str(i) + ".png"))
        
        self.enemies = []
        for i in range(5):
            self.enemies.append(Gomba(random.randint(200, 500), 0, 35, self.g, "gomba.png", 70, 70, 5, 200, 800))
        
        self.platforms = []
        for i in range(3):
            self.platforms.append(Platform(250+i*300, 500-i*150, 192, 50, "platform.png"))
        
        for i in range(3):
            self.platforms.append(Platform(1500+i*300, 500-i*150, 192, 50, "platform.png"))
    
    def display(self):
        # fill(0,140,0)
        # stroke(140)
        # strokeWeight(1)
        # rect(0, self.g, self.w, self.h)
        
        cnt = 0
        x = 0
        for b in self.bgImgs:
            if cnt == 1:
                x = self.x//4
            if cnt == 2:
                x = self.x//3
            if cnt == 3:
                x = self.x//2
            if cnt == 4 and cnt == 5:
                x = self.x
            cnt += 1
            
            image(b,0,0, self.w - x%self.w, self.h, x%self.w, 0, self.w, self.h)
            image(b,self.w -x%self.w, 0, x%self.w, self.h, 0, 0, x%self.w, self.h  )
        
        for p in self.platforms:
            p.display()
        
        for e in self.enemies:
            e.display()
            
        self.mario.display()
    

g = Game(1280,720,585)

def setup():
    size(g.w, g.h)
    background(255)
    
def draw():
    if not g.pause:
        background(255)
        g.display()

def keyPressed():
    if keyCode == LEFT:
        g.mario.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.mario.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.mario.keyHandler[UP] = True
    elif keyCode == 80:
        if g.pause:
            g.pause = False
        else:
            g.pause = True
        g.pauseSound.rewind()
        g.pauseSound.play()
        
def keyReleased():
    if keyCode == LEFT:
        g.mario.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.mario.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.mario.keyHandler[UP] = False
