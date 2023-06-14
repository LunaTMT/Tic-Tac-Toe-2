from tile import Tile

import numpy as np
import random

class Board():
    
    corner  = [(0, 0), (0, 2), (2, 0), (2, 2)]
    center  = [(1, 1)]
    side    = [(0, 1), (1, 0), (2, 1), (1, 2)]

    def __init__(self, interface) -> None:
        self.interface  = interface
        self.display    = interface.display

        self.board = np.array([[Tile((0, 0)), Tile((0, 1)), Tile((0, 2))],
                               [Tile((1, 0)), Tile((1, 1)), Tile((1, 2))],
                               [Tile((2, 0)), Tile((2, 1)), Tile((2, 2))]]) 
        
        self.slices = self.get_slices() 
        self.current_player = ""
        self.total = 0
        

    def __str__(self):
        "Used to display the board"
        self.display.show_title("Tic Tac Toe!", True)
        return " ".join([tile.__str__() for row in self.board for tile in row])

    def __getitem__(self, position):
        #Dunder method used to make reference to numpy array clearer
        return self.board[position]  
    
    def __setitem__(self, position, value):
        #Dunder method used to make setting values in numpy array clearer
        self.board[position] = value 

    def highlight_winner(self, slice):
        "This function highlights all pieces that are the winning one and sets the rest to white"
        for r in self:
            for tile in r:
                tile.colour = "white"

        for tile in slice:
            tile.colour = "light_yellow"                      
    def colour_update(self, current, new=False):
        "This function updates the colours and symbols for the currently selected tile and the newly selected one"

        if current and not new:
            #Initial square
            self[current].sym = self.current_player.sym
            self[current].colour = "green"
        elif new != current: 
            #when we have an actual new square to update
            if self[current].free: 
                self[current].sym = '   '
            
            if self[new].free:
                self[new].sym = self.current_player.sym
                self[new].colour = "green"
            else:
                self[new].colour = "red"

            #We always want to change the previous square when there is a new one         
            self[current].colour = None
        else:
            #If The user is trying to choose a taken square we do not want to update any colours
            pass  
            
    def show_moves(self):
        print(self)
        self.display.show_cardinals() 
    def make_move(self):
        """
        This function is the whole moving process across the board. 
        The user is shown each updated position depending on where they want to go.
        Finally the user comits the move and the board is updated (Y)"""

        #initialise first 
        current = self.get_next_available_position()
        self.colour_update(current) 
        
        choice = ""
        while choice != "Y" or not self[current].free: #Continue unitl the user chooses a valid square
            
            #Show moves and get choice
            self.show_moves()
            choice = self.get_choice()

            #get the new position based upon choice (YWASD)
            new = self.get_new_pos(current, choice)
            
            #Update the colour
            self.colour_update(current, new)

            #update new position
            current = new
            
        #comit the move once chosen
        self.commit_move(current)   
    def commit_move(self, position):
        """
        This function sets the current position on the board to being owned by a given player
        thus making it inacessible to the other player."""

        self[position].sym = self.current_player.sym
        self[position].colour = None
        self[position].free = False
        self.total += 1

        self.check_winner()

    def check_boundary(self, position):
        "This function verifys if the given position actually exists"
        try: 
            self[position]
            return position
        except:
            return False
    def check_winner(self):
        #This function checks if anyone has won
        if self.total == 9:
            self.display.show_endgame("DRAW")

        for slice in self.slices:
            values = set(tile.sym for tile in slice)
            
            if len(values) == 1 and "   " not in values:
                self.highlight_winner(slice)
                print(self)
                self.display.show_endgame("WON")
                self.current_player.update_score()
                
    def get_choice(self):
        "This functions gets the cardinal direction the player wishes to move"
        choice = ""
        while choice not in ("Y", "W", "A", "S", "D"):
                choice = input(f"\t   {self.current_player.name}'s choice : ").upper()  
        return choice
    def get_slices(self):
        """This function returns a list of lists
        The lists contained within are the diagnoals and all rows and columns
        """
        diagnoal_1 = [self[0,0], self[1,1], self[2,2]]
        diagnoal_2 = [self[2,0], self[1,1], self[0,2]]
        slices = [diagnoal_1, diagnoal_2]
        
        for i in range(3):
            slices.append(self[:, i])
            slices.append(self[i, :])

        return slices
    def get_new_pos(self, current, choice):
        """
        This function returns a new position based upon the cardinal choice, 
        it also verifies if it is an actual value on the board"""

        x, y = current

        match choice:
            case "W":
                new = self.check_boundary((x - 1, y  ))
            case "A":
                new = self.check_boundary((x    , y-1))
            case "S":
                new = self.check_boundary((x + 1, y  ))
            case "D":
                new = self.check_boundary((x    , y+1))
            case "Y":
                new = current
        
        return new if new else current
    def get_next_available_position(self):
        "This function finds the first available position in the board that is free"
        for row in self:
            for tile in row:
                if tile.free == True:
                    return tile.pos

    def reset(self):
        #This resets each tile on the board to its default state and changes total to 0 as nothing is now on the board
        for r in self:
            for tile in r:
                tile.reset()    
        self.total = 0