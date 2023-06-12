from typing import Any
from player import Player
from ai import Ai
import time

class Menu:

    def __init__(self, interface):
        self.interface  = interface
        self.board      = interface.board
        self.display    = interface.display

        self.choice     = ""
        self.exit = False
    

    def __str__(self):
        self.display.clear()
        return """
    
        Ｔｉｃ－Ｔａｃ－Ｔｏｅ

        Which would you like to play?

        1: Player VS Player
        2: Player VS Computer
        3: Score 
        4: Quit
        """  
    
    def __call__(self) -> None:
        print(self)                         
        self.get_choice()
        self.verify_choice()
        self.execute_choice()


    def get_choice(self):
        self.choice = input("\tChoice : ")

    def verify_choice(self):
        while self.choice not in ("1", "2", "3", "4"):
            self.get_choice()
        
    def execute_choice(self):
        """
        This function executes the chosen menu option by the player
        
        Case 1 & 2 both sort the players by which one has the symbol " X " 
        (This person must start first)

        Case 3 displays the current scoreboard

        Case 4 quits the program
        """

        match self.choice:
            
            case "1":
                self.interface.players += sorted([Player(self.interface, 1), Player(self.interface, 2)], reverse=True)
            case "2":                
                self.interface.players += sorted([Player(self.interface, 1),     Ai(self.interface, 2)], reverse=True)
            case "3":
                self.display.show_score()
            case "4":
                self.exit = True


