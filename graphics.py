import pygame
import os
from pygame.locals import *
image = pygame.image.load('./Images/SnakeScore.jpg')
justLoadScore = False
def renderBoard100(game,window):
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


def renderFullScore100(game,window):
    window.blit(image, (245, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)                             #
    NumberScoreSurface = myfont.render(str(game.score), False, (255, 234, 0))         #                          score number
    window.blit(NumberScoreSurface,(295,60))                                      #
    pygame.display.flip()                                                         # In this line I update the frame

def rederUpdateScore100(game,window):
    NumberScoreSurface = myfont.render(str(game.score), False, (255, 234, 0))         #                          score number
    window.blit(NumberScoreSurface,(295,60))                                      #
    pygame.display.flip()                                                         # In this line I update the frame    



def renderFrame(game,window):
    renderBoard100(game,window)
    if justLoadScore == False:
        renderFullScore100(game,window)
    else:
        rederUpdateScore100(game,window)
