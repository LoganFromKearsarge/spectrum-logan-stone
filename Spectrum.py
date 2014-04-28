import pygame, sys, math, random

pygame.init()

from Block import Block
from Player import Player
from HardBlock import HardBlock
from PortalBlock import PortalBlock
from ShadeBlock import ShadeBlock
from Spike import Spike
from Enemy import Enemy
from Background import Background
from Color import Color

clock = pygame.time.Clock()

width = 1050
height = 675
size = width, height

blocksize = [75,75]
playersize = [70,70]

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0

blocks = pygame.sprite.Group()
hardBlocks = pygame.sprite.Group()
portalBlocks = pygame.sprite.Group()
shadeBlocks = pygame.sprite.Group()
spikes = pygame.sprite.Group()
enemies = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (all, players)
Block.containers = (all, blocks)
HardBlock.containers = (all, hardBlocks, blocks)
PortalBlock.containers = (all, portalBlocks, blocks)
ShadeBlock.containers = (all, shadeBlocks, blocks)
Spike.containers = (all, spikes, blocks)
Enemy.containers = (all, enemies)
Background.containers = (all, blocks)

bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("rsc/bg/mainbg.png")
bgRect = bgImage.get_rect()
bg = Background("rsc/bg/mainbg.png", size)

levels = ["rsc/levels/level1",
          "rsc/levels/level2",
          "rsc/levels/level3"]
level = 0

def loadLevel(level):
    f = open(level+".lvl", 'r')
    lines = f.readlines()
    f.close()
    
    newlines = []
    
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newlines += [newline]
        
    for line in newlines:
        print line
    
    for y, line in enumerate(newlines):
        for x, c in enumerate(line):
            if c == "#":
                HardBlock("rsc/blocks/black.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "+":
                PortalBlock("rsc/blocks/portal.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2],
                      blocksize)
            elif c == "r":
                Block("rsc/blocks/red.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "b":
                Block("rsc/blocks/blue.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "y":
                Block("rsc/blocks/yellow.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "p":
                Block("rsc/blocks/purple.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "g":
                Block("rsc/blocks/green.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "o":
                Block("rsc/blocks/orange.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "x":
                Spike("rsc/blocks/Obstacles/spike.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "s":
                ShadeBlock("rsc/blocks/shade.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
                      
    f = open(level+".tng", 'r')
    lines = f.readlines()
    f.close()
    
    newlines = []
    
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newlines += [newline]
        
    for line in newlines:
        print line
    
    for y, line in enumerate(newlines):
        for x, c in enumerate(line):
            if c == "@":
                player = Player([(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2],
                     playersize,
                     size)
            elif c == "e":
                Enemy("rsc/enemy/red guy.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      playersize)
    #for each in all.sprites():
    #    each.fixLocation(player.offsetx, player.offsety)
     
    
def loadNextLevel(level):
    for each in all.sprites():
        each.kill()
    bg = Background("rsc/bg/mainbg.png", size)
    screen.blit(bg.image, bg.rect)
    loadLevel(levels[level])
    return level
    
loadLevel(levels[level])
player1 = players.sprites()[0]


start = False
while True:
    bgImage = pygame.image.load("rsc/screen/TitleScreen.png")  
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    start = True                    
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
     
    while start and player1.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    player1.change("white")
                if event.key == pygame.K_KP1:
                    player1.change("black")
                if event.key == pygame.K_KP2:
                    player1.change("red")
                if event.key == pygame.K_KP3:
                    player1.change("orange")
                if event.key == pygame.K_KP4:
                    player1.change("yellow")
                if event.key == pygame.K_KP5:
                    player1.change("green")
                if event.key == pygame.K_KP6:
                    player1.change("blue")
                if event.key == pygame.K_KP7:
                    player1.change("purple")
                    
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.direction("up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.direction("down")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.direction("stop down")
                    
        playersHitBlocks = pygame.sprite.groupcollide(players, hardBlocks, False, False)
        playersHitPortalBlocks = pygame.sprite.groupcollide(players, portalBlocks, False, False)
        playersHitSpikes = pygame.sprite.groupcollide(players, spikes, False, False)
        playersHitShadeBlocks = pygame.sprite.groupcollide(players, shadeBlocks, False, False)
        
        enemiesHitBlocks = pygame.sprite.groupcollide(enemies, hardBlocks, False, False)
        enemiesHitEnemies = pygame.sprite.groupcollide(enemies, enemies, False, False)
        
        
        for player in playersHitBlocks:
            for block in playersHitBlocks[player]:
                player.collideBlock(block)
                
        for player in playersHitPortalBlocks:
            for block in playersHitPortalBlocks[player]:
                level = loadNextLevel(level+1)
                player1 = players.sprites()[0]
                
        for player in playersHitSpikes:
            for block in playersHitSpikes[player]:
                player1.living = False
        
        for player in playersHitShadeBlocks:
            for block in playersHitShadeBlocks[player]:
                player.collideBlock(block)
        
        for enemy in enemiesHitBlocks:
            for block in enemiesHitBlocks[enemy]:
                enemy.collideBlock(block)
                
        for enemy in enemiesHitEnemies:
            for otherEnemy in enemiesHitEnemies[enemy]:
                enemy.collideBlock(otherEnemy)
        
        all.update(size,
                   player1.speedx, 
                   player1.speedy, 
                   player1.scrollingx, 
                   player1.scrollingy,
                   player1.realx,
                   player1.realy)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(30)
        
    bgImage = pygame.image.load("rsc/screen/EndScreen.png") 
    while start and not player.living:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    start = False
                    level = 0
                    loadNextLevel(level)
                    player1 = players.sprites()[0]
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)













