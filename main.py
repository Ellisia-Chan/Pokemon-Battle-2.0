# Uncomment this import if there is missing modules 

# import packages
# packages.InitializePackages()

import GameManager as GM
import DisplayManager as DP
import time

class Gameplay:
    def __init__(self) -> None:
        # Initialize Managers Class
        self.game_Manager = GM.GameManager()
        self.display_Manager = DP.DisplayManager()
        
        # Start the program
        self.main()
     
    # =============================   
    # Main Game Method    
    # =============================
    def main(self) -> None:
        # ======================================
        # Pokemon Group Selection for player 1 and 2
        # ======================================
        self.PokemonArraySelection()
        
        # =====================================
        # Pokemon Selection for battle
        # =====================================
        self.Battle_Pokemon_Selection()

    def PokemonArraySelection(self):
        # ==============================
        #  Pokemon array selection for
        #  both Player
        # ==============================
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
            
    def Battle_Pokemon_Selection(self) -> None:        
        # =====================================
        # Pokemon Selection for Battle
        # =====================================
        count = 0
        while count != 2:
            try:
                self.display_Manager.DisplayPlayersSelectedPokemons(self.game_Manager.GetPlayer_1_SelectedPokemon(),
                        self.game_Manager.GetPlayer_2_SelectedPokemon(),
                        self.game_Manager.GetPlayer_1_BattlePokemon(),
                        self.game_Manager.GetPlayer_2_BattlePokemon(),
                        count)
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
        else:
            self.display_Manager.DisplayPlayersSelectedPokemons(self.game_Manager.GetPlayer_1_SelectedPokemon(),
                    self.game_Manager.GetPlayer_2_SelectedPokemon(),
                    self.game_Manager.GetPlayer_1_BattlePokemon(),
                    self.game_Manager.GetPlayer_2_BattlePokemon(),
                    count) 
            
        time.sleep(2)
        print("\033c", end="")
            
if __name__ == "__main__":
    Gameplay()