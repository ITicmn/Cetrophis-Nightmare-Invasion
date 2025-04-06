import pygame

class Space():
    def __init__(self,game,size):
        self.game = game
        self.size = size
        self.contain = {}
        
    def upload(self,object,size,pos):
        self.contain[object.name] = {"size": [size[0],size[1],size[2]],"pos": [pos[0],pos[1]],"object": object}