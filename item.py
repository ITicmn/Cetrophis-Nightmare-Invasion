import pygame

class Item():
    def __init__(self,game,scale,name,pos,drop):
        self.game = game
        self.name = name
        self.change = 0
        self.change_cd = 0
        self.size = [self.game.assets[self.name][0].get_size()[0]*scale/100,self.game.assets[self.name][0].get_size()[1]*scale/100]
        self.pos = pos
        self.drop = drop
        self.rect = pygame.Rect(pos[0],pos[1],self.size[0],self.size[1])
    
    def render(self,surface):
        if self.change_cd <= 0:
            if self.change+1 >= len(self.game.assets[self.name]):
                self.change = 0
            else: 
                self.change += 1
            self.change_cd = 1.7
        else:
            self.change_cd -= 0.2
        surface.blit(pygame.transform.scale(self.game.assets[self.name][self.change], self.size), self.pos)