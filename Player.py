import pygame, sys, math
from Color import Color


class Player(pygame.sprite.Sprite):
    def __init__(self, pos = (0,0), blocksize = [50,50], screensize = [800,600]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screensize = screensize
        
        self.colors = {"white": Color("white", blocksize),
                        "black": Color("black", blocksize), 
                        "red": Color("red", blocksize)} 
                        #"orange": Color("orange", blocksize), 
                        #"yellow": Color("yellow", blocksize),  
                        #"green":  Color("green", blocksize),
                        #"blue":  Color("blue", blocksize),
                        #"purple":  Color("purple", blocksize)}                      
        self.color = self.colors["white"]
        
        self.images = self.color.rightImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.waitCountMax = 5
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeed = blocksize[0]/10.0
        self.speed = [0,0]
        self.speedx = 0
        self.speedy = 0
        self.realx = pos[0]
        self.realy = pos[1]
        self.x = screensize[0]/2
        self.y = screensize[1]/2
        self.offsetx = self.x - self.realx
        self.offsety = self.y - self.realy
        self.scrollingx = False
        self.scrollingy = False
        self.scrollBoundry = 200
        self.headingx = "right"
        self.headingy = "up"
        self.lastHeading = "right"
        self.headingChanged = False
        self.radius = self.rect.width/2
        self.living = True
        self.place(pos)
        
        
    def place(self, pos):
        self.rect.center = pos
        
    def fixLocation(self, x, y):
        pass
    
    def colorChange(color):    
        self.color = self.colors[color]
                 
    def update(*args):
        self = args[0]
        self.collideWall(self.screensize)
        self.animate()
        self.move()
        self.headingChanged = False
        
    def animate(self):
        if self.headingChanged:
            if self.lastHeading == "up":
                self.images = self.color.upImages
            if self.lastHeading == "down":
                self.images = self.color.downImages
            if self.lastHeading == "right":
                self.images = self.color.rightImages
            if self.lastHeading == "left":
                self.images = self.color.leftImages
            self.image = self.images[self.frame]
        
        if self.waitCount < self.waitCountMax:
            self.waitCount += 1
        else:
            self.waitCount = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
            
        
    def move(self):
        self.realx += self.speedx
        self.realy += self.speedy
        self.x = self.realx
        self.y = self.realy
        """
        if not self.scrollingx:
            self.x += self.speedx
        if self.x > self.screensize[0] - self.scrollBoundry and self.headingx == "right":
            self.scrollingx = True
        elif self.x < self.scrollBoundry and self.headingx == "left":
            self.scrollingx = True
        else:
            self.scrollingx = False
            
        if not self.scrollingy:
            self.y += self.speedy
        if self.y > self.screensize[1] - self.scrollBoundry and self.headingy == "down":
            self.scrollingy = True
        elif self.y < self.scrollBoundry and self.headingy == "up":
            self.scrollingy = True
        else:
            self.scrollingy = False
        """    
        self.rect.center = (round(self.x), round(self.y))
        
    def collideWall(self, size):
        if self.rect.left < 0 and self.headingx == "left":
            self.speedx = 0
        elif self.rect.right > size[0] and self.headingx == "right":
            self.speedx = 0
        if self.rect.top < 0 and self.headingy == "up":
            self.speedy = 0
        elif self.rect.bottom > size[1] and self.headingy == "down":
            self.speedy = 0
       
    def change(self, color):
        if color in self.colors.keys():
            self.color = self.colors[color]
            self.headingChanged = True
        else:
            print "not a color", self.colors.keys()
    
    def collideBlock(self, block):
        print self.rect, self.headingx, self.headingy
        if self.realx < block.realx and self.headingx == "right":
            self.speedx = 0
            self.realx -= 1
            self.x -= 1
            print "hit right"
        if self.realx > block.realx and self.headingx == "left":
            self.speedx = 0
            self.realx += 1
            self.x += 1
            print "hit left"
        if self.realy > block.realy and self.headingy == "up":
            self.speedy = 0
            self.realy += 1
            self.y += 1
            print "hit up"
        if self.realy < block.realy and self.headingy == "down":
            self.speedy = 0
            self.realy -= 1
            self.y -= 1
            print "hit down"
   
    def direction(self, dir):
        if dir == "right":
            self.headingx = "right"
            self.speedx = self.maxSpeed
            self.lastHeading = "right"
            self.headingChanged = True
        if dir == "stop right":
            self.headingx = "right"
            self.speedx = 0
        if dir == "left":
            self.headingx = "left"
            self.speedx = -self.maxSpeed
            self.lastHeading = "left"
            self.headingChanged = True
        if dir == "stop left":
            self.headingx = "left"
            self.speedx = 0
        if dir == "up":
            self.headingy = "up"
            self.speedy = -self.maxSpeed
            self.lastHeading = "up"
            self.headingChanged = True
        if dir == "stop up":
            self.headingy = "up"
            self.speedy = 0
        if dir == "down":
            self.headingy = "down"
            self.speedy = self.maxSpeed
            self.lastHeading = "down"
            self.headingChanged = True
        if dir == "stop down":
            self.headingy = "down"
            self.speedy = 0
