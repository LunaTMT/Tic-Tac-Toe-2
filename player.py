from coin_flip import CoinFlip

class Player():
        
    def __init__(self, interface, id):
        self.interface  = interface
        self.board      = interface.board
        self.display    = interface.display
        self.id = id
        
        self.name = self.get_name()
        self.score = 0
        self.interface.scoreboard.append(self)
        
        self.sym = ""
        CoinFlip(self.display, self) 
        self.opposite = self.get_oppposite_symbol(self.sym)

    def __str__(self):
        return f"| {self.name} : {self.score}"
    

    def __lt__(self, p2):
        """
        This dunder method is used in order that the player object be sortable
        The obj is sorted by the ascii value for X and O"""
        # X = 088
        # O = 79
        return self.sym < p2.sym
    
    def make_move(self): 
        self.board.current_player = self
        self.board.get_move()

    def get_name(self):
        self.display.show_title(f"Player {self.id}", True)
        return input("Please enter your name: ").title()

    def get_oppposite_symbol(self, sym):
        return " O " if sym == " X " else " X "
