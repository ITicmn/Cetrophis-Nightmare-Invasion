import pygame
from pygame.locals import *
from pygamevideo import Video
import os
import sys, time

BASE_VID_PATH = 'assets/video/'
#GMTK/assets/video/

def load_video(path):
    video = Video(BASE_VID_PATH + path)
    return video

def load_videos(path):
    videos = []
    for video_name in os.listdir(BASE_VID_PATH + path):#用os.listdir來取得文件夾裡的所有文件地址並做成一個list
        videos.append(load_video(path + '/' + video_name))
    return videos

def play_video(surface,video,game_volume):
    video.volume = game_volume
    video.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    video.stop()
                    break
        if video.is_playing == False:
            break
        video.draw_to(surface, (0, 0))
        pygame.display.flip()