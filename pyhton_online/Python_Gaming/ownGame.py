import random #to generate random moves
import sys     #to exit the program
import pygame
from pygame.key import name
from pygame.locals import *

FPS=60
screen_width=1100
screen_hieght=600

screen=pygame.display.set_mode((screen_width,screen_hieght))
ground_hieght=screen_hieght*0.6
Game_Sprites={}
Game_Sounds={}
background="A:\\pyhton_online\\Python_Gaming\\backPower.jpg"
player="A:\\pyhton_online\\Python_Gaming\\player.jpg"


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption= ("Power Fighter")
    Game_Sprites['background']=pygame.image.load(background).convert()
    Game_Sprites['player']=pygame.image.load(player).convert()
    screen.blit(pygame.image.load(background).convert(),(0,0))
    screen.blit(pygame.image.load(player).convert(),(200,150))
    pygame.display.update()

    # while True:
    #     welcome_screen()
    #     main_game()

