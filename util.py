import os
import pygame

BASE_IMG_PATH = 'assets/'
#GMTK/assets/

def load_image(path):
    image = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    #image.set_colorkey((0,0,0))
    return image

def load_images(path):
    images = []
    for image_name in os.listdir(BASE_IMG_PATH + path):#用os.listdir來取得文件夾裡的所有文件地址並做成一個list
        images.append(load_image(path + '/' + image_name))
    return images