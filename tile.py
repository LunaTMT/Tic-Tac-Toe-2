from termcolor import colored

class Tile:
        
    def __init__(self, pos) -> None:
        self.pos = pos
        self.free = True
        self.sym = "   "
        self.colour = None

    def __str__(self):
        result = colored(f'  {self.sym}  ', self.colour, attrs=["reverse", "blink"])
        if self.pos in ((0,0), (1,0), (2,0)): 
            return "\n\n\t" + result  
        return result
        