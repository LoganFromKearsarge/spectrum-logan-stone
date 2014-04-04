import pygame, sys, math, random

pygame.init()

from Block import Block
from Player import Player
from HardBlock import HardBlock
from PortalBlock import PortalBlock
from Enemy import Enemy
from Background import Background

clock = pygame.time.Clock()

width = 1050
height = 675
size = width, height

blocksize = [75,75]
playersize = [75,75]

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0

blocks = pygame.sprite.Group()
hardBlocks = pygame.sprite.Group()
portalBlocks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (all, players)
Block.containers = (all, blocks)
HardBlock.containers = (all, hardBlocks, blocks)
PortalBlock.containers = (all, blocks)
Enemy.containers = (all, enemies)
Background.containers = (all, blocks)


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
    if level < len(levels)-1:
        level += 1
    else:
        level = 0
    for each in all.sprites():
        each.kill()
    bg = Background("rsc/bg/mainbg.png", size)
    screen.blit(bg.image, bg.rect)
    loadLevel(levels[level])

loadLevel(levels[level])
player1 = players.sprites()[0]
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
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
    enemiesHitBlocks = pygame.sprite.groupcollide(enemies, hardBlocks, False, False)
    enemiesHitEnemies = pygame.sprite.groupcollide(enemies, enemies, False, False)
    
    for player in playersHitBlocks:
        for block in playersHitBlocks[player]:
            player.collideBlock(block)
            
    for player in playersHitPortalBlocks:
        for block in playersHitPortalBlocks[player]:
            loadNextLevel(level)
            print "Level Loaded"
    
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
    














