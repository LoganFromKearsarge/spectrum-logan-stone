import pygame, sys, math

from Block import Block

class Spike(Block):
    def __init__(self, image, pos = (0,0), blocksize = [25,50]):
        Block.__init__(self, image, pos, blocksize)
