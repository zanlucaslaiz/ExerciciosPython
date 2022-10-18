# faça um programa em python que abra e reproduza o audio de um arquivo de mp3

import pygame
pygame.init()
som = pygame.mixer.Sound('pitty.mp3')
som.play()

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      RUN = False





