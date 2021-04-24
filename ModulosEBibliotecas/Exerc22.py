#Usando lib para tocar um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('Exerc22.mp3')
pygame.mixer.music.play()
pygame.event.wait()

