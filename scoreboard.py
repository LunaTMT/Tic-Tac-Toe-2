class Scoreboard(dict):

    def get_sorted(self) -> dict:
        #Return the scoreboard sorted by the score. Top player is the one with the highest score
        return {k: v for k, v in sorted(self.items(), key=lambda item: item[1], reverse=True)}

        
        