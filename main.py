import cv2
import pygame
import mediapipe as mp
import random
#init pygame
pygame.init()
#setup display
WIDTH,HEIGHT=800,600
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hand Controlled Dream Catcher Game")

#load assets
background=pygame.image.load("sky.webp")
player=pygame.image.load("basket.png")
stars=pygame.image.load("star.png")
extra_life=pygame.image.load("extra_life.png")
#resize images
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
player=pygame.transform.scale(player,(100,100))
stars=pygame.transform.scale(stars,(50,50))
extra_life=pygame.transform.scale(extra_life(50,50))