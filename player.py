from coin_flip import CoinFlip

class Player():
        
    def __init__(self, interface, id):
        self.interface  = interface
        self.board      = interface.board
        self.display    = interface.display
        self.id = id
        
        self.name = self.get_name()
        self.interface.scoreboard[self] = 0
        self.score = 0
        
        
        self.sym = ""
        CoinFlip(self.display, self)
        self.opposite = self.get_oppposite_symbol()

    def __str__(self):
        return f"| {self.name} : {self.score}"
    
    def __lt__(self, p2):
        """
        This dunder method is used in order that the player object be sortable
        The obj is sorted by the ascii value for X and O"""
        # X = 088
        # O = 79
        return self.sym < p2.sym
    


    def get_move(self): 
        self.board.current_player = self
        self.board.make_move()

    def get_name(self):
        self.display.show_title(f"Player {self.id}", True)
        return input("Please enter your name: ").title()

    def get_oppposite_symbol(self):
        return " O " if self.sym == " X " else " X "

    def update_score(self):
        self.interface.scoreboard[self] += 1
        self.score += 1