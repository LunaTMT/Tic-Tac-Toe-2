
from player import Player
from ai import Ai

from coin_flip import CoinFlip

class Menu:

    def __init__(self, interface):
        self.interface  = interface
        self.board      = interface.board
        self.display    = interface.display

        self.choice     = ""
        self.exit = False
        

    def __str__(self):
        """This dunder returns the menu as a str
        The 5th option will only display when there has already been an instance of people playing (i.e. players exist)
        """
        self.display.clear()
        return f"""
    
        Ｔｉｃ－Ｔａｃ－Ｔｏｅ

        Which would you like to play?

        1: Player VS Player 
        2: Player VS Computer
        3: Score 
        4: Quit
        {f'5: Play again? ({" ".join(player.name for player in self.interface.players)})' if self.interface.players else ""}
        """  
    
    def __call__(self) -> None:
        #Running process of menu
        self.interface.end = False #So the game can start again
        print(self)                         
        self.choice = input("\tChoice : ")
        self.execute_choice()

        
    def execute_choice(self):
        """
        This function executes the chosen menu option by the player
        
        Case 1 & 2 both sort the players by which one has the symbol " X " 
        (This person must start first)

        Case 3 displays the current scoreboard

        Case 4 quits the program

        Case 5 is only possible if the game has been played before and there exists players to play again
        A coinflip will be remade to determine the starting player

        The default case just reruns the menu (i.e. invalid option)
        """
        
        match self.choice:
            
            case "1":
                self.interface.players = sorted([Player(self.interface, 1), Player(self.interface, 2)], reverse=True)
            case "2":                
                self.interface.players = sorted([Player(self.interface, 1),     Ai(self.interface, 2)], reverse=True)
            case "3":
                self.display.show_score()
                self() 
            case "4":
                self.exit = True
            case "5" if self.interface.players:
                #Instead of instantiating new players we must reroll the coinflip to get the correct symbols
                #Then must sort to determine who is the starting player (sym = X)
                for player in self.interface.players:
                    CoinFlip(self.display, player) 
                    player.get_oppposite_symbol()
                self.interface.players.sort(reverse=True)
            case _:
                self()



