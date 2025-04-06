import pygame

class Entity():
    def __init__(self,game,scale,name,pos,space,movement,ground,interactable):
        self.game = game
        self.name = name
        self.animation = "stand"
        self.change = 0
        self.change_cd = 0
        self.size = [self.game.assets[self.name][self.animation][0].get_size()[0]*scale/100,self.game.assets[self.name][self.animation][0].get_size()[1]*scale/100]
        self.pos = pos
        self.space = space
        self.rect = pygame.Rect(pos[0],pos[1],self.size[0],self.size[1])
        self.velocity = [0,0]
        self.movement = movement
        self.status = "onGround"
        self.ground = ground
        self.cooldown = 0
        self.interactable = interactable
        
    def get_rect(self):
        return pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        
    def update(self,background,camera):
        screen_size = background.contain["screen"]["size"]
        
        #left right
        self.velocity[0] = (self.movement["left"]*-1 + self.movement["right"]*1)*8
        
        self.pos[0] += self.velocity[0]
        collision_object = self.collide_object(background)
        if collision_object != None:
            if self.velocity[0] < 0:
                self.pos[0] = collision_object.pos[0]+collision_object.size[0]
                self.velocity[0] = 0
            elif self.velocity[0] > 0:
                self.pos[0] = collision_object.pos[0]-self.size[0]
                self.velocity[0] = 0
        
        #left collision
        if self.pos[0] < 0:
            self.pos[0] = 0
            self.velocity[0] = 0
            
        #right collision
        if self.pos[0]+self.size[0] > screen_size[0]:
            self.pos[0] = screen_size[0]-self.size[0]
            self.velocity[0] = 0
        
        #up collision
        if self.pos[1] < 0:
            self.pos[1] = 0
            self.velocity[1] = 0
            
        #jump
        if self.status == "onGround" and self.cooldown <= 0:
            self.velocity[1] += -20*self.movement["up"]
            if self.velocity[1] < 0:
                self.status = "inAir"
            
        self.pos[1] += self.velocity[1]
            
        collision_object = self.collide_object(background)
        if collision_object != None:
            if self.velocity[1] < 0:
                self.pos[1] = collision_object.pos[1]+collision_object.size[1]
                self.velocity[1] = 0
                self.status = "onGround"
                self.cooldown -= 0.1
            elif self.velocity[1] > 0:
                self.pos[1] = collision_object.pos[1]-self.size[1]
                self.velocity[1] = 0
                self.status = "onGround"
                self.cooldown -= 0.1
                
        #down collision
        if self.pos[1]+self.size[1] < screen_size[1]-self.ground:
            self.velocity[1] = min(25, self.velocity[1] + 1)
            if collision_object == None:
                self.status = "inAir"
                self.cooldown = 1.6
        
        elif self.pos[1]+self.size[1] >= screen_size[1]-self.ground:
            if self.pos[1]+self.size[1] > screen_size[1]-self.ground:
                self.pos[1] = screen_size[1]-self.ground-self.size[1]
            self.velocity[1] = 0
            self.status = "onGround"
            self.cooldown -= 0.1
        
        #animation
        if self.velocity[0] < 0:
            if self.animation != "walk left":
                self.change_cd = 0
            self.animation = "walk left"
        elif self.velocity[0] > 0:
            if self.animation != "walk right":
                self.change_cd = 0
            self.animation = "walk right"
        elif self.velocity[0] == 0:
            if self.animation != "stand":
                self.change_cd = 0
            self.animation = "stand"
        
        #final calculation
        if camera == 0:
            self.space[0] += self.velocity[0]
        elif camera == 1:
            self.space[1] += self.velocity[0]
        elif camera == 2:
            self.space[1] -= self.velocity[0]
        elif camera == 3:
            self.space[0] -= self.velocity[0]
        
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        
        background.contain[self.name]["size"] = self.size
        background.contain[self.name]["pos"] = self.pos
        
    def collide_object(self,background):
        object = None
        entity_rect = pygame.Rect(self.space[0],self.space[1],self.size[0],self.size[0])
        entity = self.get_rect()
        for name in [*background.contain]:
            if background.contain[name]["type"] == "object":
                object_rect = pygame.Rect(background.contain[name]["object"].space[0],background.contain[name]["object"].space[1],background.contain[name]["object"].space[2],background.contain[name]["object"].space[3])
                if entity.colliderect(background.contain[name]["object"].rect) and entity_rect.colliderect(object_rect):
                    object = background.contain[name]["object"]
        return object
                
    def render(self,surface):
        if self.change_cd <= 0:
            if self.change+1 >= len(self.game.assets[self.name][self.animation]):
                self.change = 0
            else: 
                self.change += 1
            self.change_cd = 2.6
        else:
            self.change_cd -= 0.2
        surface.blit(pygame.transform.scale(self.game.assets[self.name][self.animation][self.change], self.size), self.pos)