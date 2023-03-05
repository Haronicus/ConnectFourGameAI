import numpy as np
import pygame
from random import randint
import time
import signal



BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7


class Player:

    def __init__(self):
        pass

    def taketurn(self,board,player):
        # return a number between 0-(n-1) where n is the number or columns
        moves = np.array([i for i in range(COLUMN_COUNT)])

        #if column is full... then its not possible
        filter = np.min(board.T,axis=1) == 0

        filteredMoves = moves[filter]

        return np.random.choice(filteredMoves)

        

class ConnectFour: 

    def __init__(self, render) -> None:
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0
        self.render = render

            #initalize pygame
        if render == True:
            
            self.SQUARESIZE = 100
            self.width = COLUMN_COUNT * self.SQUARESIZE
            self.height = (ROW_COUNT+1) * self.SQUARESIZE
            
            size = (self.width, self.height)
            
            
            self.RADIUS = int(self.SQUARESIZE/2 - 5)

            pygame.init()
            self.screen = pygame.display.set_mode(size)
            #Calling function draw_board again
            self.draw_board(self.board)
            pygame.display.update()
            self.myfont = pygame.font.SysFont("monospace", 75)

        pass

    
    def create_board(self):
        board = np.zeros((ROW_COUNT,COLUMN_COUNT)).astype(np.int8)
        return board
    
    def drop_piece(self,board, row, col, piece):
        board[row][col] = piece
    
    def is_valid_location(self,board, col):
        return board[ROW_COUNT-1][col] == 0
    
    def get_next_open_row(self,board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r
    
    def print_board(self,board):
        print(np.flip(board, 0))
    
    def winning_move(self,board, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
    
        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True
    
        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True
    
        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
    
    def draw_board(self,board):

        assert self.render == True

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):      
                if board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(self.screen, YELLOW, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        pygame.display.update()
    

    def playGame(self,player1: Player,player2: Player):
        self.print_board(self.board)
        game_over=False
        turn = 0




        while not game_over:

            #signal.signal(signal.SIGALRM,self.signal_handler)
            #signal.alarm(10)   # Ten seconds

            startTime = time.time()
            try:
                if turn == 0:
                    col = player1.taketurn(self.board,turn + 1)
                else:
                    col = player2.taketurn(self.board,turn + 1)
            except Exception as ex:


                error = ex.args[0]

                col = Player().taketurn(self.board,turn + 1)

                if error == 'Ran out of time':
                    print ('Player {} ran out of time'.format(turn + 1))
                
                else:
                    print('Player {} code crashed'.format(turn + 1))

                
            if time.time() - startTime > 10:                
                print("Ran out of time, replacing move with random move")
                col = Player().taketurn(self.board,turn + 1)

                



            if self.is_valid_location(self.board, col):
                row = self.get_next_open_row(self.board, col)
                self.drop_piece(self.board, row, col,  turn + 1)

                if self.render:
                    self.draw_board(self.board)

            else:
                print("Player {} made an invalid move".format(turn + 1))
                game_over = True


            self.print_board(self.board)



            if self.winning_move(self.board, turn + 1):
                print("Player {} WON!!".format(turn +1))
                game_over = True


            if self.is_tie(self.board):
                print("Game is a Tie!!")
                game_over = True

            turn += 1
            turn = turn % 2

        #see the game for 1.5 second before it is done and exits
        time.sleep(1.5)

    def is_tie(self,board):
        moves = np.array([i for i in range(COLUMN_COUNT)])

        #if column is full... then its not possible
        filter = np.min(board.T,axis=1) == 0

        filteredMoves = moves[filter]

        if filteredMoves.shape[0] == 0:
            print("Draw")
            return True
        return False

    def signal_handler(self, signum, frame):
        raise Exception("Ran out of time")

    
    
    #define width and height of board

    
    
