from prettytable import PrettyTable

class BattleStatsManager:
    def __init__(self):
        self.player1_wins = 0
        self.player2_wins = 0
        self.ties = 0
        
        self.stats_table1 = PrettyTable()
        self.stats_table2 = PrettyTable()
           
    @property
    def GetPlayer1_win_count(self) -> int:
        return self.player1_wins
    
    @GetPlayer1_win_count.setter
    def SetPlayer1_win_count(self, value):
        if value < 0:
            raise ValueError("Value must not be negative")
        self.player1_wins += value
        
    @property
    def GetPlayer2_win_count(self) -> int:
        return self.player2_wins
    
    @GetPlayer2_win_count.setter
    def SetPlayer2_win_count(self, value):
        if value < 0:
            raise ValueError("Value must not be negative")
        self.player2_wins += value