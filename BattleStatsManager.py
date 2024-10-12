from prettytable import PrettyTable

class BattleStatsManager:
    def __init__(self):
        self.player1_wins = 0
        self.player2_wins = 0
        self.ties = 0
        
        self.GREEN = "\033[32m"
        self.RED = "\033[31m"
        self.YELLOW = "\033[33m"
        self.RESET = "\033[0m"
        
        self.stats_table = PrettyTable()
        
        self.stats_table.title = f"{self.YELLOW}Battle Statistic{self.RESET}"
        self.stats_table.field_names = [
            "Battle", f"{self.GREEN}Player 1 Pokemon", f"Player 1 Health", f"Player 1 Power{self.RESET}",
            f"{self.RED}Player 2 Pokemon", f"Player 2 Health", f"Player 2 Power{self.RESET}", "Winner"]
               
    def SetValueToStatsTable(self, battle_num, player1, player2, winner):
        print(winner)
        if winner == f"{self.GREEN}Player 1{self.RESET}":
            win_str = f"{self.GREEN}Player 1{self.RESET}"
        elif winner == f"{self.RED}Player 2{self.RESET}":
           win_str = f"{self.RED}Player 2{self.RESET}"
        else:
            win_str = "Tie"
            
        self.stats_table.add_row([battle_num + 1, player1[0], player1[1], player1[2],
                                  player2[0], player2[1], player2[2], win_str])
        
    def ShowStatsTable(self):
        if self.player1_wins > self.player2_wins:
            overall_winner = f"{self.GREEN}Player 1{self.RESET}"
        elif self.player2_wins > self.player1_wins:
            overall_winner = f"{self.RED}Player 2{self.RESET}"
        else:
            overall_winner = f"{self.YELLOW}No Overall Winner{self.RESET}"
            
        print("{:<54}{:<0}".format("", "🔥 Pokemon Battle 🔥\n"))
        print("{:<42}{:<0}".format("", "🔥 ============ Overall Winner ============ 🔥"))
        print("{:<60}{:<0}".format("", f"{overall_winner}\n"))
        print("{:<40}{:<30}{:<30}{:<0}".format(
            "",
            f"{self.GREEN}Player 1{self.RESET} Wins: {self.player1_wins}",
            f"{self.RED}Player 2{self.RESET} Wins: {self.player2_wins}",
            f"Ties: {self.ties}\n"))
        print(self.stats_table)  
    @property
    def GetPlayer1_win_count(self) -> int:
        return self.player1_wins
    
    @GetPlayer1_win_count.setter
    def GetPlayer1_win_count(self, value):
        if value < 0:
            raise ValueError("Value must not be negative")
        self.player1_wins += value
        
    @property
    def GetPlayer2_win_count(self) -> int:
        return self.player2_wins
    
    @GetPlayer2_win_count.setter
    def GetPlayer2_win_count(self, value):
        if value < 0:
            raise ValueError("Value must not be negative")
        self.player2_wins += value
        
    @property
    def GetTie_count(self) -> int:
        return self.ties
    
    @GetTie_count.setter
    def GetTie_count(self, value):
        if value < 0:
            raise ValueError("Value must not be negative")
        self.ties += value
    