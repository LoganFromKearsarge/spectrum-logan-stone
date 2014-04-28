import pygame, sys, math

from Block import Block

class Spike(Block):
    def __init__(self, image, pos = (0,0), blocksize = [50,50]):
        blocksize = [blocksize[0], blocksize[1]/2]
        Block.__init__(self, image, pos, blocksize)
