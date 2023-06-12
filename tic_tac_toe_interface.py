
from display import Display
from menu import Menu
from board import Board
from player import Player

class TTT_Interface():

    def __init__(self) -> None:
        self.players    = []
        self.scoreboard = []
        self.won = False
        
        self.display    =   Display(self)
        self.board      =     Board(self)
        self.menu       =      Menu(self)
        

    def run(self) -> None:
        while not self.menu.exit:
            self.menu()
            
            while not self.won:
                for player in self.players:
                    if self.won: 
                        break
                    else:
                        player.make_move()
            
        
         
