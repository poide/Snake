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
    window = pygame.display.set_mode((429, 245))            
    pygame.display.flip()
    pygame.display.set_caption("Snake by PepAss'o")
    game = Game()
    run = True

    while run:
        x = (100 - game.score)
        pygame.time.delay(x)
        events = pygame.event.get()    
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    game.changeOrientation("W")
                    break
                elif event.key == pygame.K_UP:
                    game.changeOrientation("N")
                    break
                elif event.key == pygame.K_DOWN:
                    game.changeOrientation("S")
                    break
                elif event.key == pygame.K_RIGHT:
                    game.changeOrientation("E")
                    break
                elif event.key == pygame.K_ESCAPE:
                    result = pauseMenu()
                    if result == "Q":
                        run = False
        game.move()
        graphics.renderFrame(game,window)
        if game.state == "Win":
            game = Game()
        elif game.state == "Dead":
            print("You lose")
            game = Game()
    pygame.quit()
if __name__ == "__main__":
    main()







