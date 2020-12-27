import pygame 
import neat 
import time 
import os 
import random 


import pygame

import Settings as set 
from Bird import Bird

def draw_window(win, bird: "Bird"):
    win.blit(set.BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    
    bird = Bird(200, 200 )
    win = pygame.display.set_mode((set.WIN_WIDTH, set.WIN_HEIGHT))
    
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            elif event.type == pygame.KEYDOWN:
                bird.jump()      
        
        bird.move()
        draw_window(win, bird)
    pygame.quit()
    quit()

main()