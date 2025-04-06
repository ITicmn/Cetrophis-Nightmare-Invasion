import pygame
import random

from item import *

def use(inventory,background):
    if inventory == "needle":
        background.pollution = 0
        background.pollution_cd = random.randint(120,150)
        inventory = None
    return inventory

def interact(entity,background):
    for object in [*background.contain]:
        if background.contain[object]["type"] == "object":
            for item in background.contain[object]["object"].star:
                entity_rect = pygame.Rect(entity.pos[0],entity.pos[1],entity.size[0],entity.size[1]*3/4)
                item_rect = pygame.Rect(item.pos[0],item.pos[1],item.size[0],item.size[1])
                if entity_rect.colliderect(item_rect):
                    background.contain[object]["object"].star.remove(item)
                    return item.drop
    return None

def switch(player,camera):
    if camera == 0:
        player.pos = [player.space[0],player.pos[1]]
    elif camera == 1:
        player.pos = [player.space[1],player.pos[1]]
    elif camera == 2:
        player.pos = [1920-player.space[1]-player.size[0],player.pos[1]]
    elif camera == 3:
        player.pos = [1920-player.space[0]-player.size[0],player.pos[1]]

def star_summon(background,star_size):
    items = []
    drop = ["nothing","needle","key"]
    z = random.randint(4,20)
    for i in range(0,len(background)):
        for object in [*background[i].contain]:
            if background[i].contain[object]["type"] == "object":
                if background[i].contain[object]["object"].interactable == True:
                    x = random.randint(int(0-star_size[0]/2),int(0+background[i].contain[object]["size"][0]-star_size[0]/2-100))
                    y = random.randint(int(0-star_size[1]/2),int(0+background[i].contain[object]["size"][1]-star_size[1]/2-100))
                    if z > 2 or z < 2:
                        n = random.randint(0,1)
                        background[i].contain[object]["object"].star.append(Item(background[i].game,340,"star",[background[i].contain[object]["pos"][0]+x,background[i].contain[object]["pos"][1]+y],drop[n]))
                        z -= 1
                    elif z == 2:
                        background[i].contain[object]["object"].star.append(Item(background[i].game,340,"star",[background[i].contain[object]["pos"][0]+x,background[i].contain[object]["pos"][1]+y],drop[z]))
                        z -= 1
                        
