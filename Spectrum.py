import pygame, sys, math, random

pygame.init()

from Block import Block
from Player import Player
from HardBlock import HardBlock
from PortalBlock import PortalBlock
from BlackBlock import BlackBlock
from WhiteBlock import WhiteBlock
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
blackBlocks = pygame.sprite.Group()
whiteBlocks = pygame.sprite.Group()
spikes = pygame.sprite.Group()
enemies = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (all, players)
Block.containers = (all, blocks)
HardBlock.containers = (all, hardBlocks, blocks)
PortalBlock.containers = (all, portalBlocks, blocks)

BlackBlock.containers = (all, blackBlocks, blocks)
WhiteBlock.containers = (all, whiteBlocks, blocks)

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
                HardBlock("rsc/blocks/block.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "+":
                PortalBlock("rsc/blocks/portal.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2],
                      blocksize)
            elif c == "x":
                Spike("rsc/blocks/Obstacles/spike.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "b":
                BlackBlock("rsc/blocks/black.png",
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "w":
                WhiteBlock("rsc/blocks/white.png",
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
                if event.key == pygame.K_SPACE:
                    if player1.color.color == "white":
                        player1.change("black")
                    else:
                        player1.change("white")
                    
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.direction("jump")
                #if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #    player1.direction("down")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("stop left")
                #if event.key == pygame.K_w or event.key == pygame.K_UP:
                 #   player1.direction("stop up")
                #if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                 #   player1.direction("stop down")
                    
        playersHitBlocks = pygame.sprite.groupcollide(players, hardBlocks, False, False)
        playersHitPortalBlocks = pygame.sprite.groupcollide(players, portalBlocks, False, False)
        playersHitSpikes = pygame.sprite.groupcollide(players, spikes, False, False)
        playersHitBlackBlocks = pygame.sprite.groupcollide(players, blackBlocks, False, False)
        playersHitWhiteBlocks = pygame.sprite.groupcollide(players, whiteBlocks, False, False)
        
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
                player1.collideSpikeBlock(block)
        
        for player in playersHitBlackBlocks:
            for block in playersHitBlackBlocks[player]:
                if player.color.color == "white":
                    player.collideBlock(block)
        
        for player in playersHitWhiteBlocks:
            for block in playersHitWhiteBlocks[player]:
                if player.color.color == "black":
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













