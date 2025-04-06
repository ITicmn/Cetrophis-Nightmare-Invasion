from moviepy.editor import *
from moviepy.video.fx import resize

import pygame
from pygame.locals import *
from pygamevideo import Video
import os

pygame.init()
window = pygame.display.set_mode((2560,1440))

# Load the video from the specified dir
video = Video(fr"C:\Users\USER\Downloads\Shikonokonoko koshitantan.mp4")
video.volume = 0.2

# Start the video
#video.play()

def play_video(video):
    video.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    video.stop()
                    break
        if video.is_playing == False:
            break
        video.draw_to(window, (0, 0))
        pygame.display.flip()

# Main loop
while True:

  # Draw video to display surface
  # this function should be called every frame
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if event.type == KEYDOWN:
          if event.key == K_DOWN:
              play_video(video)
              
    pygame.draw.rect(window,'white',[0,0,2560,1440])
              
          

  # Update pygame display
    pygame.display.flip()


#video = VideoFileClip(fr'C:\Users\USER\Downloads\Shikonokonoko koshitantan.mp4')
#video = video.without_audio()
#video.preview()

pygame.quit()