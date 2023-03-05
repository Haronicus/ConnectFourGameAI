import ConnectFour

class TerminalPlayer(ConnectFour.Player):

    def taketurn(self,board,player):

        return int(input("Your Move between 0 and 6?:"))