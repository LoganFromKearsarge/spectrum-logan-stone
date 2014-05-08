import pygame, sys, math, time
from Color import Color


class Player(pygame.sprite.Sprite):
    def __init__(self, pos = (0,0), blocksize = [50,50], screensize = [800,600]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screensize = screensize
        
        self.colors = {"white": Color("white", blocksize),
                        "black": Color("black", blocksize)}                      
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
        self.headingx = "right"
        self.headingy = "up"
        self.lastHeading = "right"
        self.headingChanged = False
        self.radius = self.rect.width/2
        self.living = True
        self.place(pos)
        self.g = blocksize[0]/10
        self.jumping = False
        self.jumpSpeed = 0
        self.jumpSpeedMax = 50
        self.fallSpeedMax = int(blocksize[0]/2) -2
        self.onfloor = False
        self.floor = screensize[1]
        self.touchFloor = False
        
        
    def place(self, pos):
        self.rect.center = pos
        
    def fixLocation(self, x, y):
        pass
    
    def colorChange(color):    
        self.color = self.colors[color]
                 
    def update(*args):
        self = args[0]
        self.collideWall(self.screensize)
        if (self.rect.bottom < self.floor) and self.headingy == "none":
            self.headingy = "down"
        self.animate()
        self.move()
        self.headingChanged = False
        self.touchFloor = False
        
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
        if not self.touchFloor:
            self.headingy = "down"
            print "falling", self.speedy
        if self.headingy == "down":
            if self.speedy < self.fallSpeedMax:
                self.speedy += self.g
            else:
                self.speedy = self.fallSpeedMax
                
        self.realx += self.speedx
        self.realy += self.speedy
        
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
        self.rect.center = (round(self.realx), round(self.realy))
        
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
        #time.sleep(.25)
        print self.rect, self.headingx, self.headingy
        if self.floor == block.rect.top + 2 and self.headingy == "none":
            self.touchFloor = True
            print "on the floor"
            self.jumping = False
        else:
            if self.realx < block.realx and self.headingx == "right":
                self.speedx = 0
                self.realx -= 1
                print "hit right"
            if self.realx > block.realx and self.headingx == "left":
                self.speedx = 0
                self.realx += 1
                print "hit left"
            if self.realy > block.realy and self.headingy == "up":
                self.speedy = 0
                self.realy += 1
                print "hit up"
            if self.realy < block.realy and self.headingy == "down":
                self.touchFloor = True
                self.speedy = 0
                self.headingy = "none"
                self.floor = block.rect.top+2
                self.realy = self.floor - self.rect.height/2
                print "///////////////////////hit down"
            
    def collideSpikeBlock(self, block):
        if self.rect.bottom > block.rect.center[1]:
            self.living = False
            
   
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
        if dir == "jump":
            if not self.jumping:
                self.jumping = True
                self.headingy = "up"
                self.jumpSpeed = self.jumpSpeedMax
                self.speedy = -self.jumpSpeed
                self.headingChanged = True
                self.touchingFloor = False
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
