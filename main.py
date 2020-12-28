import pygame 
import neat 
import time 
import os 
import random 
import pygame

import Settings as set 
from Bird import Bird
from Base import Base
from Pipe import Pipe

def draw_window(win, bird, pipes, base, score):
    win.blit(set.BG_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    text = set.STAT_FONT.render("Score: " + str(score), 1,(255,255,255) )
    win.blit(text, (set.WIN_WIDTH - 10 - text.get_width(), 10 ))

    base.draw(win)
    bird.draw(win)

    pygame.display.update()

def main():
    
    score = 0
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]

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
        
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird) or bird.img.get_height() >= 700: 
                print("GAME END")
                pass

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()

        if add_pipe: 
            score += 1 
            pipes.append(Pipe(700))

        for r in rem:
            pipes.remove(r)

        bird.move()  
        
        draw_window(win, bird, pipes, base, score)
    pygame.quit()
    quit()
main()