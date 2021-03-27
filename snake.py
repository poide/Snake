from game import Game
import time
import pygame
from pygame.locals import *


def main():
    pygame.init()                                               
    window = pygame.display.set_mode((500, 500))            
    pygame.display.flip()
    pygame.display.set_caption("Snake by PepAss'o")
    game = Game()
    run = True
    fixInput = True

    while run:
        pygame.time.delay(50)
        if game.state == "Win":
            run = False
        elif game.state == "Dead":
            run = False
        events = pygame.event.get()    
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    game.changeOrientation("W")
                elif event.key == pygame.K_UP:
                    game.changeOrientation("N")
                elif event.key == pygame.K_DOWN:
                    game.changeOrientation("S")
                elif event.key == pygame.K_RIGHT:
                    game.changeOrientation("E")


        if fixInput == True:
            game.move()
            window.fill((128,128,128)) #Fill the screen with light gray,  the background

            i = 0
            j = 0
            currentBoard = game.board
            while i < 100:
                if i%10==0 and i != 0:
                    j = j+1
                posx = 25 * (i%10)
                posy = 25 * j
                if currentBoard[i] == 0 :
                    pygame.draw.rect(window, (0,0,0), pygame.Rect(posx, posy, 20, 20))
                elif currentBoard[i] == -1:
                    pygame.draw.rect(window, (255,0,0), pygame.Rect(posx, posy, 20, 20))
                elif currentBoard[i] == 1:
                    pygame.draw.rect(window, (0,255,0), pygame.Rect(posx, posy, 20, 20))


                i = i +1


            pygame.display.flip()

        fixInput = not fixInput
    
    pygame.quit()
if __name__ == "__main__":
    main()









