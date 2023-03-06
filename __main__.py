from ConnectFour import *
from PyGamePlayer import *
from TerminalPlayer import TerminalPlayer
from StudentPlayer import StudentPlayer

myGame = ConnectFour(render=True)

playerA = StudentPlayer()  # random bot
playerB = TerminalPlayer()
playerC2 = PyGamePlayer(myGame)

myGame.playGame(playerA, playerC2)
