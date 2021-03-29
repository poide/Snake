import pygame
import graphics
from game import Game





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
    window = pygame.display.set_mode((350, 245))            
    pygame.display.flip()
    pygame.display.set_caption("Snake by PepAss'o")
    game = Game()
    fixInput = True
    run = True
    while run:
        x = 75
        if(game.score % 5 == 0):
            x = x - 5
        pygame.time.delay(x)
        if game.state == "Win":
            game = Game()
        elif game.state == "Dead":
            print("Has perdido")
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
            graphics.renderFrame(game,window)
        fixInput = not fixInput
    pygame.quit()
if __name__ == "__main__":
    main()







