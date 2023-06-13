class Scoreboard(dict):

    def get_sorted(self):
        return {k: v for k, v in sorted(self.items(), key=lambda item: item[1], reverse=True)}

        
        