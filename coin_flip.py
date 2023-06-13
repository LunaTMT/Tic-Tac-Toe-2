import time
import random

class CoinFlip:

    initialised = False
    first_symbol = ""

    def __init__(self, display, player) -> None:
        self.display = display
        self.player = player

        self.guess = ""
        #self.outcome = random.choice(("Tails", "Heads"))
        self.outcome = "Heads"

        self()
        

    def __call__(self):
        if not CoinFlip.initialised:
            self.get_choice()
            self.show_coin_flip()
            self.verify_outcome()
            CoinFlip.initialised = True
            self.player.sym = CoinFlip.first_symbol  
        else: 
            self.player.sym = " O " if CoinFlip.first_symbol == " X " else " X "


    def get_choice(self):
        while self.guess not in ("H", "T"):
            self.display.show_title("Coin Flip!", True)
            self.guess = input(f"{self.player.name}, Heads or Tails? (H/T) \nInput : ").upper()
            
        self.guess = "Heads" if self.guess == "H" else "Tails"

    def show_coin_flip(self):
        for i in ["Tails", "Heads"] * 10 + [self.outcome]:
            self.display.show_title("Flipping", True)
            print(f"""Your choice : {self.guess} \nOutcome     : {i}""")
            time.sleep(0.1)
        print()

    def verify_outcome(self):

        if self.guess == self.outcome:
            print(f"{self.outcome} is correct!")
            CoinFlip.first_symbol = " X "
        else:           
            print(f"Unlucky, {self.guess} was wrong.")
            CoinFlip.first_symbol = " O "
        time.sleep(2)
