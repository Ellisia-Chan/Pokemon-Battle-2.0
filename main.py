import packages
packages.InitializePackages()

import GameManager as GM
import DisplayManager as DP
import time

class Gameplay:
    def __init__(self) -> None:
        # Initialize Managers Class
        self.game_Manager = GM.GameManager()
        self.display_Manager = DP.Display()
        
        # Start the program
        self.main()
     
    # =============================   
    # Main Game Method    
    # =============================
    def main(self):
        # ======================================
        # Pokemon Group Selection for player 1 and 2
        # ======================================
        count = 0
        while count != 2:
            try:      
                # Display Title and Program Information
                self.display_Manager.DisplayProgramInfo()
                self.display_Manager.DisplayPokemonSelection(self.game_Manager.GetPokemonInfo())  
                
                selection_Errors = self.game_Manager.PokemonArraySelection(count)
                
                # Check IndexError for user input selections
                if selection_Errors: 
                    time.sleep(1)
                    print("\033c", end="")
                    continue
                count += 1
                
                # Clear the Console for better UX
                print("\033c", end="")
            except ValueError:
                print("Invald Input. Please Try Again!")
                time.sleep(1)
                print("\033c", end="")
                continue
        
        self.Battle_Pokemon_Selection()
        
    def Battle_Pokemon_Selection(self):        
        # =====================================
        # Pokemon Selection for Battle
        # =====================================
        count = 0
        while count != 2:
            try:
                self.display_Manager.DisplayPlayersSelectedPokemons(self.game_Manager.GetPlayer_1_SelectedPokemon(),
                                                                self.game_Manager.GetPlayer_2_SelectedPokemon(),
                                                                self.game_Manager.GetPlayer_1_BattlePokemon(),
                                                                self.game_Manager.GetPlayer_2_BattlePokemon())
                selection_Errors = self.game_Manager.BattlePokemonSelection(count)
                
                # Check IndexError for user input selections
                if selection_Errors: 
                    time.sleep(1)
                    print("\033c", end="")
                    continue
                count += 1
                
                # Clear the Console for better UX
                print("\033c", end="")
                
            except ValueError:
                print("Invald Input. Please Try Again!")
                time.sleep(1)
                print("\033c", end="")
                continue
        
        self.display_Manager.DisplayPlayersSelectedPokemons(self.game_Manager.GetPlayer_1_SelectedPokemon(),
                                                                self.game_Manager.GetPlayer_2_SelectedPokemon(),
                                                                self.game_Manager.GetPlayer_1_BattlePokemon(),
                                                                self.game_Manager.GetPlayer_2_BattlePokemon())       
if __name__ == "__main__":
    Gameplay()