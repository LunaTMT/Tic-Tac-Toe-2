
from display import Display
from menu import Menu
from board import Board
from player import Player

from scoreboard import Scoreboard

class TTT_Interface():

    def __init__(self) -> None:
        self.players    = []
        self.scoreboard =  Scoreboard() 
        self.end = False
        
        self.display    =   Display(self)
        self.board      =     Board(self)
        self.menu       =      Menu(self)


    def run(self) -> None:
        while True:
            self.menu()

            while not self.end:
                for player in self.players:
                    if self.end: 
                        break
                    else:
                        player.make_move()
            
            
         
