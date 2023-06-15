from player import Player
from board import Board
import random

class Ai(Player):

    def get_move(self) -> None:
        "This function gets the best posible move and comits it to the board"
        
        #Init current player on board
        self.board.current_player = self  
        
        win, block = self.get_win_or_block_move()
                      
        if win:                             # - If we have found a winning position        
            self.board.commit_move(win)
            return
        elif block:                         # - Is there a position we can block  
            self.board.commit_move(block)
            return
        else:                               # - If not find the next best position    
            position = self.get_best_available_position()
            self.board.commit_move(position)

    def get_win_or_block_move(self) -> str:
        """
        This function searches if there are any valid:
            - Winning moves
            - Blocking moves
        """
        win, block = "", ""

        #Must search the whole board to see if there are any winning or blocking positions
        for slices in self.board.slices:
 
            values = [tile.sym for tile in slices]
            positions = [tile.pos for tile in slices]

            self_count = values.count(self.sym)
            enemy_count = values.count(self.opposite)

            #Ensure winning always takes precedence over blocking
            if (self_count == 2 and enemy_count == 0): 
                return positions[values.index('   ')], ""
                   
            elif (self_count == 0 and enemy_count == 2):
                block = positions[values.index('   ')]
        return win, block

    def get_best_available_position(self) -> tuple:
        """
        If this function is called it means that there are no winning or blocking move
        We now want to find the best posible position available for the Ai"""
        
        random.shuffle(Board.corner)
        random.shuffle(Board.side)

        for pos in (Board.corner + Board.center + Board.side):
            if self.board[pos].free:
                return pos

    def get_name(self) -> str:
        return "Ai"