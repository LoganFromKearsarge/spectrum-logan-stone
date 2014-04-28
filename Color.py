import pygame


class Color:
    def __init__(self, color, blocksize):
        self.color = color
        self.upImages = [pygame.image.load("rsc/player/"+color+"/player.png"),
                         pygame.image.load("rsc/player/"+color+"/player.png")]
        self.upImages = [pygame.transform.scale(self.upImages[0], blocksize),
                         pygame.transform.scale(self.upImages[1], blocksize)]
        self.downImages = [pygame.image.load("rsc/player/"+color+"/playerDown.png"),
                         pygame.image.load("rsc/player/"+color+"/playerDown2.png")]
        self.downImages = [pygame.transform.scale(self.downImages[0], blocksize),
                         pygame.transform.scale(self.downImages[1], blocksize)]
        self.rightImages = [pygame.image.load("rsc/player/"+color+"/playerRight.png"),
                         pygame.image.load("rsc/player/"+color+"/playerRight2.png")]
        self.rightImages = [pygame.transform.scale(self.rightImages[0], blocksize),
                         pygame.transform.scale(self.rightImages[1], blocksize)]
        self.leftImages = [pygame.image.load("rsc/player/"+color+"/playerLeft.png"),
                         pygame.image.load("rsc/player/"+color+"/playerLeft2.png")]
        self.leftImages = [pygame.transform.scale(self.leftImages[0], blocksize),
                         pygame.transform.scale(self.leftImages[1], blocksize)]
        