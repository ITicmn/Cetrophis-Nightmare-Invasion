import sys, time
import pygame
from pygame.locals import *
from pygamevideo import Video
import random
import os

from util import *
from background import *
from entity import *
from video import *
from object import *
from act import *
from item import *
from shape import scale
from space import *

#Screen Settings
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
BACKGROUND_WIDTH = 2560
BACKGROUND_HEIGHT = 1440
FPS = 60
ASSET = fr'assets/'
MUSIC = fr'assets/music'
VIDEO = fr'assets/video'

#Icon
icon = pygame.image.load(f'{ASSET}icon.png')
pygame.display.set_icon(icon)

#Caption
pygame.display.set_caption('Cetrophis: Nightmare Invasion')

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
ALPHA = (0, 255, 0)


#main game functions
def main():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    
    main_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    class Game:
        def __init__(self):
            pygame.init()
            
            self.volume = 1.0
            self.assets = {
                "menu background": load_image('menu/menu bg.png'),
                "setting button": load_image('menu/setting button.png'),
                "start button": load_image('menu/start button.png'),
                "title 1": load_image('menu/title 1.png'),
                "title 2": load_image('menu/title 2.png'),
                "volume": load_image('setting/volume.png'),
                "bar": load_image('setting/bar.png'),
                "select": load_image('setting/select.png'),
                "control": load_image('setting/control.png'),
                "inventory": load_image('inventory.png'),
                "needle": load_image('needle.png'),
                "black palette": load_image('black palette.png'),
                "chat": load_image('chat.png'),
                "pollution": load_images('pollution'),
                "map": load_image('map.png'),
                "end game background": load_image('end game/background.png'),
                "end game polluted": load_image('end game/polluted.png'),
                "end game restart": load_image('end game/restart.png'),
                "text key": load_images('text/key'),
                "text needle": load_images('text/needle'),
                "text nothing": load_images('text/nothing'),
                "level_1 camera 1": load_image('level 1/level 1 bg c1.png'),
                "level_1 camera 1 cover": load_image('level 1/C1/shelf.png'),
                "level_1 camera 2": load_image('level 1/level 1 bg c2.png'),
                "level_1 camera 3": load_image('level 1/level 1 bg c3.png'),
                "level_1 camera 3 cover": load_image('level 1/C3/forbackground.png'),
                "level_1 camera 4": load_image('level 1/level 1 bg c4.png'),
                "level_1 camera 4 cover": load_image('level 1/C4/wall.png'),
                "level_2 camera 1": load_image('level 2/level 2 bg c1.png'),
                "level_2 camera 1 cover": load_image('level 2/C1/shelf.png'),
                "level_2 camera 2": load_image('level 2/level 2 bg c2.png'),
                "level_2 camera 3": load_image('level 2/level 2 bg c3.png'),
                "level_2 camera 3 cover": load_image('level 2/C3/forbackground.png'),
                "level_2 camera 4": load_image('level 2/level 2 bg c4.png'),
                #"level_2 camera 4 cover": load_image('level 2/C4/wall.png'),
                "level_3 camera 1": load_image('level 3/level 3 bg c1.png'),
                "level_3 camera 1 cover": load_image('level 3/C1/shelf.png'),
                "player": {
                    "paint": load_image('Unfy/paint.png'),
                    "stand": load_images('Unfy/stand'),
                    "walk left": load_images('Unfy/walk/left'),
                    "walk right": load_images('Unfy/walk/right')},
                "larry": {
                    "stand": load_images('.-.. .- .-. .-. -.--/stand')},
                "jerry": {
                    "stand": load_images('.--- . .-. .-. -.--/stand')},
                "star": load_images('star'),
                "small needle": load_images('small needle')
            }
            self.video = {
                #"ending 1": load_video('Ending 1.mp4'),
                "ending 1(shikonoko)": load_video('Ending 1(shikonoko).mp4'),
                #"ending 2": load_video('Ending 2.mp4'),
                #"ending 3": load_video('Ending 3.mp4'),
                "death": load_video('death.mp4'),
            }
            self.music = {
                "menu": "menu.mp3",
                "Nose Honk": "Nose Honk.mp3",
                "level_1": "level 1.mp3",
                "level_2": "level 2.mp3",
                "level_3": "level 3.mp3",
                "death": "death.mp3"
            }
            self.player = Entity(self,400,"player",[370,1000],[370,750],{"right":False,"left":False,"up":False,"down":False},0,False)
            self.larry = Entity(self,270,"larry",[450,1000],[450,750],{"right":False,"left":False,"up":False,"down":False},8,True)
            self.jerry = Entity(self,600,"jerry",[700,0],[0,0],{"right":False,"left":False,"up":False,"down":False},0,False)
            self.assets["black palette"].set_alpha(150)
            self.assets["level_1 camera 1 cover"].set_alpha(145)
            self.assets["level_1 camera 3 cover"].set_alpha(145)
            self.assets["level_1 camera 4 cover"].set_alpha(145)
            self.assets["level_2 camera 1 cover"].set_alpha(145)
            self.assets["level_2 camera 3 cover"].set_alpha(145)
            #self.assets["level_2 camera 4 cover"].set_alpha(145)
            self.assets["level_3 camera 1 cover"].set_alpha(145)
            
        def main_game(self):
            Game.menu(self)
            Game.level_1(self)
            Game.level_2(self)
            Game.level_3(self)
            
        def menu(self):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            background = Background(self,(1920,1080),"menu background")
            background.upload("screen",(1920,1080),(0,0),"screen","screen")
            bgm = pygame.mixer.Sound(fr"{MUSIC}\{self.music["menu"]}")
            bgm.set_volume(self.volume)
            bgm.play(loops=-1)
            #################################
            menu = True
            while menu:

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                background.render(screen)
                ##############################
                if pygame.mouse.get_pos()[0] >= 120 and pygame.mouse.get_pos()[0] <= 120+self.assets["start button"].get_size()[0]*0.2 and pygame.mouse.get_pos()[1] >= 130 and pygame.mouse.get_pos()[1] <= 130+self.assets["start button"].get_size()[1]*0.2:
                    screen.blit(pygame.transform.scale(self.assets["start button"],(self.assets["start button"].get_size()[0]*0.2,self.assets["start button"].get_size()[1]*0.2)),(120,130))
                    screen.blit(pygame.transform.scale(self.assets["title 2"],(self.assets["title 2"].get_size()[0]*1.7,self.assets["title 2"].get_size()[1]*1.7)),(30,646))
                else:
                    screen.blit(pygame.transform.scale(self.assets["start button"],(self.assets["start button"].get_size()[0]*0.21,self.assets["start button"].get_size()[1]*0.21)),(116,126))
                    screen.blit(pygame.transform.scale(self.assets["title 1"],(self.assets["title 1"].get_size()[0]*1.7,self.assets["title 1"].get_size()[1]*1.7)),(30,646))
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[0] <= 150+self.assets["setting button"].get_size()[0]*0.2 and pygame.mouse.get_pos()[1] >= 370 and pygame.mouse.get_pos()[1] <= 370+self.assets["setting button"].get_size()[1]*0.2:
                    screen.blit(pygame.transform.scale(self.assets["setting button"],(self.assets["setting button"].get_size()[0]*0.19,self.assets["setting button"].get_size()[1]*0.19)),(150,370))
                else:
                    screen.blit(pygame.transform.scale(self.assets["setting button"],(self.assets["setting button"].get_size()[0]*0.2,self.assets["setting button"].get_size()[1]*0.2)),(146,366))
                    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= 120 and pygame.mouse.get_pos()[0] <= 120+self.assets["start button"].get_size()[0]*0.2 and pygame.mouse.get_pos()[1] >= 130 and pygame.mouse.get_pos()[1] <= 130+self.assets["start button"].get_size()[1]*0.2:
                            menu = False
                        elif pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[0] <= 150+self.assets["setting button"].get_size()[0]*0.2 and pygame.mouse.get_pos()[1] >= 370 and pygame.mouse.get_pos()[1] <= 370+self.assets["setting button"].get_size()[1]*0.2:
                            Game.setting(self,bgm)
                            
                pygame.display.flip()
            bgm.stop()
            return self.volume
            
        def setting(self,bgm):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            background = Background(self,(1920,1080),"menu background")
            background.upload("screen",(1920,1080),(0,0),"screen","screen")
            #################################
            volume = self.volume*376+280
            menu = True
            press = False
            while menu:

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                background.render(screen)
                screen.blit(pygame.transform.scale(self.assets["volume"],(self.assets["volume"].get_size()[0]*1.7,self.assets["volume"].get_size()[1]*1.7)),(60,130))
                screen.blit(pygame.transform.scale(self.assets["bar"],(self.assets["bar"].get_size()[0]*5,self.assets["bar"].get_size()[1]*5)),(280,185))
                screen.blit(pygame.transform.scale(self.assets["control"],(self.assets["control"].get_size()[0]*0.5,self.assets["control"].get_size()[1]*0.5)),(60,500))
                ##############################
                if pygame.mouse.get_pos()[0] >= volume and pygame.mouse.get_pos()[0] <= volume+self.assets["select"].get_size()[0]*2.5 and pygame.mouse.get_pos()[1] >= 173 and pygame.mouse.get_pos()[1] <= 173+self.assets["select"].get_size()[1]*2.5:
                    screen.blit(pygame.transform.scale(self.assets["select"],(self.assets["select"].get_size()[0]*2.6,self.assets["select"].get_size()[1]*2.6)),(volume,173))
                else:
                    screen.blit(pygame.transform.scale(self.assets["select"],(self.assets["select"].get_size()[0]*2.5,self.assets["select"].get_size()[1]*2.5)),(volume,173))
                
                    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            menu = False
                    if event.type == MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pos()[0] >= volume and pygame.mouse.get_pos()[0] <= volume+self.assets["select"].get_size()[0]*2.5 and pygame.mouse.get_pos()[1] >= 173 and pygame.mouse.get_pos()[1] <= 173+self.assets["select"].get_size()[1]*2.5:
                            press = True
                    if event.type == MOUSEBUTTONUP:
                        press = False
                        
                if press == True:
                    volume = pygame.mouse.get_pos()[0]-self.assets["select"].get_size()[0]*2.5/2
                    if volume > 656:
                        volume = 656
                    elif volume < 280:
                        volume = 280
                    bgm.set_volume((volume-280)/376)
                            
                pygame.display.flip()
            self.volume = (volume-280)/376
        
        def death_screen(self,level):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            background = Background(self,(1920,1080),"end game background")
            background.upload("screen",(1920,1080),(0,0),"screen","screen")
            #################################
            bgm = pygame.mixer.Sound(fr"{MUSIC}\{self.music["death"]}")
            bgm.set_volume(self.volume)
            bgm.play(loops=-1)
            #################################
            menu = True
            text = 25
            restart = 0
            cd = 0
            while menu:

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                background.render(screen)
                ##############################
                self.assets["end game polluted"].set_alpha(text)
                screen.blit(pygame.transform.scale(self.assets["end game polluted"],(self.assets["end game polluted"].get_size()[0]*1,self.assets["end game polluted"].get_size()[1]*1)),(0,0))
                if text < 225 and cd == 0:
                    text += 10
                elif text == 225 and cd <= 36:
                    cd += 1
                elif text <= 225 and cd > 36:
                    text -= 5
                    
                self.assets["end game restart"].set_alpha(restart)
                screen.blit(pygame.transform.scale(self.assets["end game restart"],(self.assets["end game restart"].get_size()[0]*1,self.assets["end game restart"].get_size()[1]*1)),(0,0))
                if text < 0 and cd > 36 and restart < 255:
                    restart += 10
                    
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == MOUSEBUTTONDOWN:
                        if restart >= 255:
                            bgm.stop()
                            if level == 1:
                                Game.level_1(self)
                            elif level == 2:
                                Game.level_2(self)
                            elif level == 3:
                                Game.level_3(self)
                            
                pygame.display.flip()
                
        def level_1(self):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            #################################
            background1 = Background(self,(1920,1080),"level_1 camera 1")
            background1.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background1,"level 1","camera 1")
            background2 = Background(self,(1920,1080),"level_1 camera 2")
            background2.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background2,"level 1","camera 2")
            background3 = Background(self,(1920,1080),"level_1 camera 3")
            background3.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background3,"level 1","camera 3")
            background4 = Background(self,(1920,1080),"level_1 camera 4")
            background4.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background4,"level 1","camera 4")
            backgrounds = [background1,background2,background3,background4]
            star_summon(backgrounds,self.assets["star"][0].get_size())
            text = None
            #################################
            bgm = pygame.mixer.Sound(fr"{MUSIC}\{self.music["level_1"]}")
            bgm.set_volume(self.volume)
            bgm.play(loops=-1)
            #################################
            camera = 0
            story = "larry"
            inventory = 'needle'
            key = False
            game = True
            while game:
                

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                backgrounds[camera].layer(camera)
                backgrounds[camera].update()
                backgrounds[camera].render(screen)
                if story == "larry":
                    self.larry.update(backgrounds[camera],camera)
                self.player.update(backgrounds[camera],camera)
                ##############################
                if camera == 0:
                    screen.blit(pygame.transform.scale(self.assets["level_1 camera 1 cover"], (self.assets["level_1 camera 1 cover"].get_size()[0]*12,self.assets["level_1 camera 1 cover"].get_size()[1]*12)), (660,504))
                elif camera == 2:
                    screen.blit(pygame.transform.scale(self.assets["level_1 camera 3 cover"], (self.assets["level_1 camera 3 cover"].get_size()[0]*12,self.assets["level_1 camera 3 cover"].get_size()[1]*12)), (0,0))
                elif camera == 3:
                    screen.blit(pygame.transform.scale(self.assets["level_1 camera 4 cover"], (self.assets["level_1 camera 4 cover"].get_size()[0]*12,self.assets["level_1 camera 4 cover"].get_size()[1]*12)), (12,36))
                ##############################
                """
                backgrounds[camera].pollute()
                if backgrounds[camera].pollution > 0:
                    if backgrounds[camera].pollution >= 7:
                        bgm.stop()
                        play_video(screen,self.video["death"],self.volume)
                        Game.death_screen(self,1)
                    self.assets["pollution"][backgrounds[camera].pollution].set_alpha(220)
                    screen.blit(pygame.transform.scale(self.assets["pollution"][backgrounds[camera].pollution], (1920,1080)), (0,0))
                """
                ##############################
                screen.blit(pygame.transform.scale(self.assets["black palette"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                if inventory == None:
                    screen.blit(pygame.transform.scale(self.assets["inventory"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                elif inventory == "needle":
                    screen.blit(pygame.transform.scale(self.assets["inventory"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                    screen.blit(pygame.transform.scale(self.assets["needle"], (self.assets["needle"].get_size()[0]*1.4,self.assets["needle"].get_size()[1]*1.4)), (5,5))
                ##############################
                pygame.draw.rect(screen,(255, 255, 255),(1662,0,self.assets["map"].get_size()[0]*0.3-2,self.assets["map"].get_size()[1]*0.3))
                screen.blit(pygame.transform.scale(self.assets["map"], (self.assets["map"].get_size()[0]*0.3,self.assets["map"].get_size()[1]*0.3)), (1662,0))
                pygame.draw.rect(screen,(255, 0, 0),(1662+self.player.space[0]*0.13+9,self.player.space[1]*0.13+9,self.player.size[0]*0.13,self.player.size[0]*0.13))
                ##############################
                if text != None:
                    text.render(screen)
                    if text.change == 19:
                        text = None
                ##############################
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = True
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = True
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = True
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = True
                        if event.key == pygame.K_1:
                            backgrounds[0].pollution = backgrounds[camera].pollution
                            backgrounds[0].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 0
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_2:
                            backgrounds[1].pollution = backgrounds[camera].pollution
                            backgrounds[1].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 1
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_3:
                            backgrounds[2].pollution = backgrounds[camera].pollution
                            backgrounds[2].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 2
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_4:
                            backgrounds[3].pollution = backgrounds[camera].pollution
                            backgrounds[3].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 3
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == K_e:
                            inventory = use(inventory,backgrounds[camera])
                        if event.key == K_f:
                            if self.player.rect.colliderect(self.larry.rect):
                                Game.dialogue(self,screen,"dialogue 1")
                                for background in backgrounds:
                                    background.contain["larry"]["pos"] = [-1000,-1000]
                                self.larry.pos = [-1000,-1000]
                                self.larry.rect = pygame.Rect(-1000,-1000,self.larry.size[0],self.larry.size[1])
                                story = "tutorial"
                            if camera == 3:
                                shelf = pygame.Rect(792,504,self.assets["level_1 camera 1 cover"].get_size()[0]*12,self.assets["level_1 camera 1 cover"].get_size()[0]*12)
                                door = backgrounds[camera].contain["door"]["object"].rect
                                entity = pygame.Rect(self.player.pos[0],self.player.pos[1],self.player.size[0],self.player.size[1])
                                if entity.colliderect(shelf):
                                    pygame.mixer.music.load(fr"{MUSIC}\{self.music["Nose Honk"]}")
                                    pygame.mixer.music.set_volume(self.volume)
                                    pygame.mixer.music.play()
                                elif entity.colliderect(door) and key == True:
                                    game = False
                            item = interact(self.player,backgrounds[camera])
                            if item == "nothing":
                                text = Item(self,200,"text nothing",[750,880],None)
                            elif item == "needle":
                                inventory = "needle"
                                text = Item(self,200,"text needle",[750,880],None)
                            elif item == "key":
                                key = True
                                text = Item(self,200,"text key",[750,880],None)
                        if event.key == K_r:
                            game = False
                            Game.level_1(self)
                        if event.key == pygame.K_ESCAPE:
                            Game.setting(self,bgm)
                    if event.type == KEYUP:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = False
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = False
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = False
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = False
                            
                pygame.display.flip()
        
        def level_2(self):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            #################################
            background1 = Background(self,(1920,1080),"level_2 camera 1")
            background1.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background1,"level 2","camera 1")
            background2 = Background(self,(1920,1080),"level_2 camera 2")
            background2.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background2,"level 2","camera 2")
            background3 = Background(self,(1920,1080),"level_2 camera 3")
            background3.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background3,"level 2","camera 3")
            background4 = Background(self,(1920,1080),"level_2 camera 4")
            background4.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background4,"level 2","camera 4")
            backgrounds = [background1,background2,background3,background4]
            star_summon(backgrounds,self.assets["star"][0].get_size())
            text = None
            self.player = Entity(self,400,"player",[370,1000],[370,750],{"right":False,"left":False,"up":False,"down":False},0,False)
            #################################
            bgm = pygame.mixer.Sound(fr"{MUSIC}\{self.music["level_2"]}")
            bgm.set_volume(self.volume)
            bgm.play(loops=-1)
            #################################
            camera = 0
            inventory = None
            key = False
            game = True
            while game:
                

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                backgrounds[camera].layer(camera)
                backgrounds[camera].update()
                backgrounds[camera].render(screen)
                self.player.update(backgrounds[camera],camera)
                self.larry.update(backgrounds[camera],camera)
                #self.jerry.update(backgrounds[camera])
                ##############################
                if camera == 0:
                    screen.blit(pygame.transform.scale(self.assets["level_2 camera 1 cover"], (self.assets["level_2 camera 1 cover"].get_size()[0]*12,self.assets["level_2 camera 1 cover"].get_size()[1]*12)), (660,504))
                elif camera == 2:
                    screen.blit(pygame.transform.scale(self.assets["level_2 camera 3 cover"], (self.assets["level_2 camera 3 cover"].get_size()[0]*12,self.assets["level_2 camera 3 cover"].get_size()[1]*12)), (0,0))
                elif camera == 3:
                    pass
                    #screen.blit(pygame.transform.scale(self.assets["level_1 camera 4 cover"], (self.assets["level_1 camera 4 cover"].get_size()[0]*12,self.assets["level_1 camera 4 cover"].get_size()[1]*12)), (12,36))
                ##############################
                backgrounds[camera].pollute()
                if backgrounds[camera].pollution > 0:
                    if backgrounds[camera].pollution >= 7:
                        bgm.stop()
                        play_video(screen,self.video["death"],self.volume)
                        Game.death_screen(self,2)
                    self.assets["pollution"][backgrounds[camera].pollution].set_alpha(220)
                    screen.blit(pygame.transform.scale(self.assets["pollution"][backgrounds[camera].pollution], (1920,1080)), (0,0))
                ##############################
                screen.blit(pygame.transform.scale(self.assets["black palette"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                if inventory == None:
                    screen.blit(pygame.transform.scale(self.assets["inventory"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                elif inventory == "needle":
                    screen.blit(pygame.transform.scale(self.assets["inventory"], (self.assets["inventory"].get_size()[0]*2.7,self.assets["inventory"].get_size()[1]*2.7)), (0,0))
                    screen.blit(pygame.transform.scale(self.assets["needle"], (self.assets["needle"].get_size()[0]*1.4,self.assets["needle"].get_size()[1]*1.4)), (5,5))
                ##############################
                pygame.draw.rect(screen,(255, 255, 255),(1662,0,self.assets["map"].get_size()[0]*0.3-2,self.assets["map"].get_size()[1]*0.3))
                screen.blit(pygame.transform.scale(self.assets["map"], (self.assets["map"].get_size()[0]*0.3,self.assets["map"].get_size()[1]*0.3)), (1662,0))
                pygame.draw.rect(screen,(255, 0, 0),(1662+self.player.space[0]*0.13+9,self.player.space[1]*0.13+9,self.player.size[0]*0.13,self.player.size[0]*0.13))
                ##############################
                if text != None:
                    text.render(screen)
                    if text.change == 19:
                        text = None
                ##############################
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = True
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = True
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = True
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = True
                        if event.key == pygame.K_1:
                            backgrounds[0].pollution = backgrounds[camera].pollution
                            backgrounds[0].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 0
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_2:
                            backgrounds[1].pollution = backgrounds[camera].pollution
                            backgrounds[1].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 1
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_3:
                            backgrounds[2].pollution = backgrounds[camera].pollution
                            backgrounds[2].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 2
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == pygame.K_4:
                            backgrounds[3].pollution = backgrounds[camera].pollution
                            backgrounds[3].pollution_cd = backgrounds[camera].pollution_cd
                            camera = 3
                            switch(self.player,camera)
                            switch(self.larry,camera)
                        if event.key == K_e:
                            inventory = use(inventory,backgrounds[camera])
                        if event.key == K_f:
                            item = interact(self.player,backgrounds[camera])
                            if item == "nothing":
                                text = Item(self,200,"text nothing",[750,880],None)
                            elif item == "needle":
                                inventory = 'needle'
                                text = Item(self,200,"text needle",[750,880],None)
                            elif item == "key":
                                key = True
                                text = Item(self,200,"text key",[750,880],None)
                        if event.key == K_r:
                            Game.level_2(self)
                        if event.key == pygame.K_ESCAPE:
                            Game.setting(self,bgm)
                    if event.type == KEYUP:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = False
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = False
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = False
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = False
                            
                pygame.display.flip()
        
        def level_3(self):
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),pygame.RESIZABLE)
            #################################
            background = Background(self,(2560,1440),"level_3 camera 1")
            background.upload("screen",(1920,1080),(0,0),"screen","screen")
            set_background(background,"level 3","camera 1")
            star_summon(background,self.assets["star"][0].get_size())
            #################################
            bgm = pygame.mixer.Sound(fr"{MUSIC}\{self.music["level_3"]}")
            bgm.set_volume(self.volume)
            bgm.play(loops=-1)
            #################################
            items = []
            inventory = None
            key = False
            game = True
            while game:
                

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                background.update()
                background.render(screen)
                ##############################
                self.player.update(background,0)
                self.larry.update(background,0)
                self.jerry.update(background,0)
                ##############################
                #pygame.draw.rect(screen,'red',[x,y,w,h])
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()                 
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = True
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = True
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = True
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = True
                        if event.key == K_f:
                            interact(self.player,items)
                        if event.key == K_r:
                            Game().level_3(self)
                        if event.key == pygame.K_ESCAPE:
                            Game().setting(self,bgm)
                    if event.type == KEYUP:
                        if event.key == pygame.K_w:
                            self.player.movement["up"] = False
                        elif event.key == pygame.K_SPACE:
                            self.player.movement["up"] = False
                        if event.key == pygame.K_a:
                            self.player.movement["left"] = False
                        if event.key == pygame.K_d:
                            self.player.movement["right"] = False
                            
                pygame.display.flip()
        
        def dialogue(self,surface,dialogue):
            with open(fr"{ASSET}dialogue.json", 'r') as file:
                data = json.load(file)
            dialogue = data[dialogue]
            self.player.movement = {"right":False,"left":False,"up":False,"down":False}
            pygame.image.save(surface, fr"{ASSET}\screenshot.png")
            image = load_image('screenshot.png')
            #################################
            font = pygame.font.SysFont('Comic Sans MS', 50)
            part = 0
            text = dialogue[part][1][0]
            length = len(dialogue[part][1])
            animation = True
            #################################
            left_x = -950
            right_x = 1800
            state = "intro"
            talk = True
            while talk:

                #FPS
                main_clock.tick(FPS)

                #Blit Background
                surface.blit(image,(0,0))
                surface.blit(pygame.transform.scale(self.assets["black palette"],(1920,1080)),(0,0))
                
                surface.blit(pygame.transform.scale(self.assets["player"]["paint"], [self.assets["player"]["paint"].get_size()[0]*0.3,self.assets["player"]["paint"].get_size()[1]*0.3]),(left_x,-235))#-400 -235
                surface.blit(pygame.transform.scale(self.assets["larry"]["stand"][0], [self.assets["larry"]["stand"][0].get_size()[0]*10,self.assets["larry"]["stand"][0].get_size()[1]*10]),(right_x,90))#1250 90
                if state == "intro":
                    left_x += 30
                    right_x -= 30
                    if left_x >= -400 and right_x <= 1250:
                        state = "chatting"
                
                elif state == "chatting":
                    surface.blit(pygame.transform.scale(self.assets["chat"],(1920,1080)),(0,0))
                
                    text_surface = font.render(text, False, (0, 0, 0))
                    chat_surface = font.render(dialogue[part][0], False, (0,0,0))
                    surface.blit(chat_surface,(400,690))
                    surface.blit(text_surface,(550,845))
                    
                    if len(text)-1 < length-1:
                        if animation == False:
                            text = dialogue[part][1]
                        else:
                            text += dialogue[part][1][len(text)]
                    else:
                        animation = False
                    
                elif state == "outro":
                    left_x -= 30
                    right_x += 30
                    if left_x <= -950 and right_x >= 1800:
                        talk = False
                        
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if state == "chatting":
                                if animation == True:
                                    animation = False
                                elif animation == False:
                                    if part < len(dialogue)-1:
                                        part += 1
                                        text = dialogue[part][1][0]
                                        length = len(dialogue[part][1])
                                        animation = True
                                    else:
                                        state = "outro"
                
                
                pygame.display.flip()
        
        
    Game().main_game()



#run game
if __name__ == '__main__':    
    main()