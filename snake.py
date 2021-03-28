from game import Game
import time
import pygame
from pygame.locals import *

def renderFrame(game,window):
    window.fill((128,128,128)) #Fill the screen with light gray,  the background
    i = 0
    j = 0
    currentBoard = game.board  #From the game we get the board and we travel it, painting the board
    while i < 100:
        if i%10==0 and i != 0:
            j = j + 1
        posx = 25 * (i%10)
        posy = 25 * j
        if currentBoard[i] == 0 : #If the position contains a 0 it means there's nothing in it, so we paint it with a black square
            pygame.draw.rect(window, (0,0,0), pygame.Rect(posx, posy, 20, 20)) 
        elif currentBoard[i] == -1: #If the position contains a -1 that position contains the food, so we paint it with a red square
            pygame.draw.rect(window, (255,0,0), pygame.Rect(posx, posy, 20, 20))
        elif currentBoard[i] == 1:  #Finally, if the position contains an 1, it means the position contains a part of the snake, so we paint it green
            pygame.draw.rect(window, (0,255,0), pygame.Rect(posx, posy, 20, 20))
        pygame.font.init()
        i = i +1

    myfont = pygame.font.SysFont('Comic Sans MS', 30)                             #
    ScoreTextSurface = myfont.render('Score', False, (0, 0, 0))                   #
    window.blit(ScoreTextSurface,(260,5))                                         #  In this five lines I have the code to render the "Score text" and the
    NumberScoreSurface = myfont.render(str(game.score), False, (0, 0, 0))         #                          score number
    window.blit(NumberScoreSurface,(275,30))                                      #
    pygame.display.flip()                                                         # In this line I update the frame

def pauseMenu():    
    check = True
    menuDisplay = ["Return to game", "Options", "Quit"]
    while check:
        events = pygame.event.get()    
        for event in events:
            if event.type == pygame.QUIT:
                return "Q"
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN :
                    check = False
    return







def main():
    pygame.init()                                               
    window = pygame.display.set_mode((500, 500))            
    pygame.display.flip()
    pygame.display.set_caption("Snake by PepAss'o")

    
    
    game = Game()
    fixInput = True
    run = True
    while run:

        pygame.time.delay(50)
        if game.state == "Win":
            game = Game()
        elif game.state == "Dead":
            print("Has perdido")
            print(game.boardToConsole())
            print(game.facing)
            print(game.positionList)
            game = Game()
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
                elif event.key == pygame.K_ESCAPE:
                    result = pauseMenu()
                    if result == "Q":
                        run = False
        if fixInput == True:
            game.move()
            renderFrame(game,window)

        fixInput = not fixInput
    pygame.quit()
if __name__ == "__main__":
    main()







