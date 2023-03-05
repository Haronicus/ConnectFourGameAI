
import math
from ConnectFour import *
import sys

class PyGamePlayer(Player):


    def __init__(self, myGame: ConnectFour):

        self.myGame = myGame


    def taketurn(self,board,player):

        myGame = self.myGame

        myColor = RED
        while True:
            if player == 2:
                myColor = YELLOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(myGame.screen, BLACK, (0,0, myGame.width, myGame.SQUARESIZE))
                    posx = event.pos[0]
                    pygame.draw.circle(myGame.screen, myColor, (posx, int(myGame.SQUARESIZE/2)), myGame.RADIUS)
        
                pygame.display.update()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(myGame.screen, BLACK, (0,0, myGame.width, myGame.SQUARESIZE))
                    #print(event.pos
                    # Ask for Player 1 Input
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.myGame.SQUARESIZE))

                    if self.myGame.is_valid_location(board, col):


                        return col
                    else:
                        pass

                self.myGame.draw_board(board)