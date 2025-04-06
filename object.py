import pygame

class Object():
    def __init__(self,asset,size,pos,space,interactive,entity):
        self.asset = asset
        self.size = size
        self.pos = pos
        self.space = space
        self.rect = pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.interactable = interactive
        self.entity = entity
        self.star = []
        
    def update(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        
    def upload(self,object):
        self.star.append(object)