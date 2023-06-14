
from scoreboard import Scoreboard
from display import Display
from board import Board
from menu import Menu

class TTT_Interface():

    def __init__(self) -> None:
        self.players    = []
        self.end        = False

        self.scoreboard =  Scoreboard() 
        self.display    =   Display(self)
        self.board      =     Board(self)
        self.menu       =      Menu(self)


    def run(self) -> None:
        #This function runs the entire program
        while True:
            self.menu()

            while not self.end:
                for player in self.players:
                    if self.end: 
                        break
                    else:
                        player.get_move()
            
            
         
