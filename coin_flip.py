import time
import random

class CoinFlip:

    run = False
    first_symbol = ""

    def __init__(self, display, player) -> None:
        self.display = display
        self.player = player

        self.guess = ""
        self.outcome = random.choice(("Tails", "Heads"))
        
        self()
        
    def __call__(self):
        """If the coinflip not already been run then it will:
        - get the users choice, 
        - show the actual flip, and then 
        - verify their guess.
        
        If the coinflip has already been run then the other player will just be assigned 
        the opposite symbol that has been store in the class variale (first_symbol)"""
        
        if not CoinFlip.run:
            self.get_choice()
            self.show_coin_flip()
            self.verify_outcome()
            CoinFlip.run = True
            self.player.sym = CoinFlip.first_symbol  
        else: 
            self.player.sym = " O " if CoinFlip.first_symbol == " X " else " X "


    def get_choice(self):
        "This function gets the players choice for the coin flip, either: Heads (H) or Tails (T)"

        if self.player.name == "Ai":
            self.guess = random.choice(("Tails", "Heads"))
        else:
            while self.guess not in ("H", "T"):
                self.display.show_title("Coin Flip!", True)
                self.guess = input(f"{self.player.name}, Heads or Tails? (H/T) \nInput : ").upper()
                
            self.guess = "Heads" if self.guess == "H" else "Tails"

    def show_coin_flip(self):
        "Displays the coin flip in a pretty manner"

        for i in ["Tails", "Heads"] * 10 + [self.outcome]:
            self.display.show_title("Flipping", True)
            print(f"""{self.player.name}'s choice : {self.guess} \nOutcome     : {i}""")
            time.sleep(0.1)
        print()

    def verify_outcome(self):
        "This function verifies the users choice"

        if self.guess == self.outcome:
            print(f"{self.outcome} is correct!")
            CoinFlip.first_symbol = " X "
        else:           
            print(f"Unlucky, {self.guess} was wrong.")
            CoinFlip.first_symbol = " O "
        time.sleep(2)
