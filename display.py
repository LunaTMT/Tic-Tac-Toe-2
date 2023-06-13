import os
import time
from coin_flip import CoinFlip

class Display():

    def __init__(self, interface) -> None:
        self.interface = interface
        self.scoreboard = interface.scoreboard
        self.clear = lambda: os.system('clear')

        self.cardinals = [
            ["","W",""],
            ["A","","D"],
            ["","S",""]]

    def show_score(self):
        self.show_title("Scoreboard", True)
        for player in self.scoreboard.get_sorted():
            print(player)
        print("-------------------------------------------")
        time.sleep(3)

    def show_title(self, title, clear=False):
        if clear: self.clear()
        print(f"""
-------------------------------------------
{title}
-------------------------------------------""")   
 
    def show_cardinals(self):

        self.show_title("Options", False)
        for r in self.cardinals:
            for card in r:
                if card:     
                    print(f"\t  {card}  ", end="")
                else:
                    print("\t    ", end="")
            print("")

        print("-------------------------------------------")
        print("\t     Y - Confirm ")
         
    def show_endgame(self, state): 
        if state == "DRAW":
            self.show_title("DRAW!")
        else:
            self.show_title(f"{self.interface.board.current_player.name.upper()} WON!")

        self.interface.end = True
        self.interface.board.reset()
        CoinFlip.initialised = False
        time.sleep(2)
