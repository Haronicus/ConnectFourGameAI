import ConnectFour
import numpy as np

class StudentPlayer(ConnectFour.Player):
    def __init__(self):
        #any initiization you want to perform
        pass

    def taketurn(self,board,player):
        #board is a 2d numpy array with size of (ROWCOUNT,COLUMNCOUNT)
        # return a number between 0-(n-1) where n is the number or columns

        moves = np.array([i for i in range(ConnectFour.COLUMN_COUNT)])

        #if column is full... then its not possible
        filter = np.min(board.T,axis=1) == 0

        filteredMoves = moves[filter]

        return np.random.choice(filteredMoves)