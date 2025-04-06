import pygame
import json
import random

from object import Object
from entity import Entity

ASSET = fr'assets/'

class Background():
    def __init__(self,game,size,name):
        self.game = game
        self.size = size
        self.name = name
        self.contain = {}
        self.pollution = 0
        self.pollution_cd = 180
        
    def update(self):
        translucent = False
        for name in [*self.contain]:
            if self.contain[name]["type"] == "object":
                if translucent == True and self.contain["player"]["object"].rect.colliderect(self.contain[name]["object"]):
                    self.contain[name]["object"].asset.set_alpha(170)
                else:
                    self.contain[name]["object"].asset.set_alpha(255)
            if name == "player":
                translucent = True
            
        
    def upload(self,name,size,pos,object,type):
        self.contain[name] = {"size": [size[0],size[1]],"pos": [pos[0],pos[1]],"object":object,"type":type}
        
    def pollute(self):
        if self.pollution_cd <= 0:
            self.pollution += 1
            self.pollution_cd = random.randint(120,150)
        else:
            self.pollution_cd -= 0.2
                
    def layer(self,camera):
        layer = []
        for name in [*self.contain]:
            if name != "screen":
                if camera == 0:
                    layer.append([self.contain[name]["object"].space[1],name,self.contain[name]])
                elif camera == 1:
                    layer.append([self.contain[name]["object"].space[0],name,self.contain[name]])
                elif camera == 2:
                    layer.append([self.contain[name]["object"].space[0],name,self.contain[name]])
                elif camera == 3:
                    layer.append([self.contain[name]["object"].space[1],name,self.contain[name]])
        if camera == 0:
            layer.sort()
        elif camera == 1:
            layer.sort(reverse=True)
        elif camera == 2:
            layer.sort()
        elif camera == 3:
            layer.sort(reverse=True)
        self.contain = {"screen":{"size":[1920,1080],"pos":[0,0],"object":"screen","type":"screen"}}
        for i in range(0,len(layer)):
            self.contain[layer[i][1]] = layer[i][2]
        
    def render(self, surface):
        for name in [*self.contain]:
            if name == "screen":
                surface.blit(pygame.transform.scale(self.game.assets[self.name],(self.contain[name]["size"][0],self.contain[name]["size"][1])), (self.contain[name]["pos"][0]*-1,self.contain[name]["pos"][1]*-1))
            elif self.contain[name]["type"] == "entity":
                self.contain[name]["object"].render(surface)
            else:
                surface.blit(pygame.transform.scale(self.contain[name]["object"].asset,(self.contain[name]["size"][0],self.contain[name]["size"][1])), (self.contain[name]["pos"][0]-self.contain["screen"]["pos"][0],self.contain[name]["pos"][1]-self.contain["screen"]["pos"][0]))
                if len(self.contain[name]["object"].star) > 0:
                    for star in self.contain[name]["object"].star:
                        star.render(surface)
                
class Level_3_Background():
    def __init__(self,game,size,name):
        self.game = game
        self.size = size
        self.name = name
        self.contain = {}
        
    def upload(self,name,size,pos,object):
        self.contain[name] = {"size": [size[0],size[1]],"pos": [pos[0],pos[1]],"object":object}
        
    def render(self, surface):
        for name in [*self.contain]:
            if name == "screen":
                surface.blit(pygame.transform.scale(self.game.assets[self.name],(self.contain[name]["size"][0],self.contain[name]["size"][1])), (self.contain[name]["pos"][0]*-1,self.contain[name]["pos"][1]*-1))
            else:
                surface.blit(pygame.transform.scale(self.contain[name]["object"].asset,(self.contain[name]["size"][0],self.contain[name]["size"][1])), (self.contain[name]["pos"][0]-self.contain["screen"]["pos"][0],self.contain[name]["pos"][1]-self.contain["screen"]["pos"][0]))
                if len(self.contain[name]["object"].star) > 0:
                    for star in self.contain[name]["object"].star:
                        star.render(surface)

def set_background(bg,level,camera):
    path = f'assets/{level}/C{list(camera)[7]}'
    with open(fr"{ASSET}furniture position.json", 'r') as file:
        pos_data = json.load(file)
    with open(fr"{ASSET}space position.json", 'r') as file:
        space_data = json.load(file)
    data = pos_data[level][camera]
    for name in [*data]:
        if name == "player":
            entity = bg.game.player
            bg.upload(entity.name,entity.size,entity.pos,entity,"entity")
        elif name == "larry":
            entity = bg.game.larry
            bg.upload(entity.name,entity.size,entity.pos,entity,"entity")
        elif name == "jerry":
            entity = bg.game.jerry
            bg.upload(entity.name,entity.size,entity.pos,entity,"entity")
        else:
            image = pygame.image.load(f"{path}/{name}.png").convert_alpha()
            object = Object(image,[image.get_size()[0]*data[name][2],image.get_size()[1]*data[name][2],space_data[name][4]],(data[name][0],data[name][1]),(space_data[name][0],space_data[name][1],space_data[name][2],space_data[name][3]),data[name][3],data[name][4])
            bg.upload(name,object.size,object.pos,object,"object")