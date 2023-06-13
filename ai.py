from player import Player
import random

class Ai(Player):



    def make_move(self): 
        self.board.current_player = self  
        
        #beginner level
        #pos = (random.randint(0, 2), random.randint(0, 2))

        #while board[pos].free == False:
        #    pos = (random.randint(0, 2), random.randint(0, 2))
        
        #please note that the Ai should always set its position to the center IF it is playing second

        #Hard level
        win = []       
        block = []

        for slices in self.board.slices:
 
            values = [tile.sym for tile in slices]
            positions = [tile.pos for tile in slices]

            #Try to make a winning move
            #Block a players winning move
            #Go to try instead sides, corners or center
            #Respectively
            self_count = values.count(self.sym)
            enemy_count = values.count(self.opposite)

            
            #Ensure winning always takes precedence over blocking
            if (self_count == 2 and enemy_count == 0): 
                win.append(positions[values.index('   ')])
                
            elif (self_count == 0 and enemy_count == 2):
                block.append(positions[values.index('   ')])
                
            else:
                corner = [(0, 0), (0, 2), (2, 0), (2, 2)]
                center = [(1, 1)]
                side = [(0, 1), (1, 0), (2, 1), (1, 2)]

                random.shuffle(corner)
                random.shuffle(side)

                for pos in (corner + center + side):
                    if self.board[pos].free:
                        pos = pos
                        break
    
        if win:
            pos = win[0]
        elif block: 
            pos = block[0]
        
        self.board.make_move(pos)


    def get_name(self):
        return "Ai"