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
        # Pokemon Battle Loop
        # =====================================
        all_pokemons_isUsed = False
        while not all_pokemons_isUsed:
            # Selection of pokemon that will be
            # use for battle
            self.Battle_Pokemon_Selection()
            self.BattlePreparation()
            self.MainBattle()

    def PokemonArraySelection(self) -> None:
        # ==============================
        #  Pokemon array selection for
        #  both Player
        # ==============================
        
        # Display Title and Program Information
        self.display_Manager.DisplayProgramInfo()
        
        count = 0
        while count != 2:
            try: 
                print("{:>20}{:>0}".format("", "🔥 Pokemon Battle 🔥"))     
                self.display_Manager.DisplayPokemonSelection(self.game_Manager.GetPokemonInfo)  
                
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
        self.game_Manager.SetSelectedPokemonsToNull()
        self.game_Manager.SetChangedPokemonPowerToNull() 
        
        count = 0
        while count != 2:
            try:
                self.display_Manager.DisplayPlayersSelectedPokemons(
                        self.game_Manager.GetPlayer_1_SelectedPokemon,
                        self.game_Manager.GetPlayer_2_SelectedPokemon,
                        self.game_Manager.GetPlayer_1_BattlePokemon,
                        self.game_Manager.GetPlayer_2_BattlePokemon,
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
            self.display_Manager.DisplayPlayersSelectedPokemons(
                    self.game_Manager.GetPlayer_1_SelectedPokemon,
                    self.game_Manager.GetPlayer_2_SelectedPokemon,
                    self.game_Manager.GetPlayer_1_BattlePokemon,
                    self.game_Manager.GetPlayer_2_BattlePokemon,
                    count)
            print("{:<45}{:<0}".format("", "Preparing Pokemons"))
            time.sleep(2)   
            print("\033c", end="")
            
    def BattlePreparation(self) -> None:
        # ==================================
        # Battle Preparation where the players
        # can decide whether they can use
        # poison or postion
        # ==================================
        count = 0
        while count != 2:
            try:
                if count == 0:
                    self.display_Manager.DisplayBattlePreparation(
                        self.game_Manager.GetPlayer_1_BattlePokemon,
                        count)
                elif count == 1:
                    self.display_Manager.DisplayBattlePreparation(
                        self.game_Manager.GetPlayer_2_BattlePokemon,
                        count)
                    
                selection_Errors = self.game_Manager.BattlePreparation(count)
                
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
            print("{:<15}{:>0}".format(
                "",
                "Entering Battle Stage"
            ))
            time.sleep(1)
            
    def MainBattle(self):
        self.display_Manager.DisplayMainBattleStats(
            self.game_Manager.GetPlayer_1_SelectedPokemon,
            self.game_Manager.GetPlayer_2_SelectedPokemon,
            self.game_Manager.GetPlayer_1_PreviousPower,
            self.game_Manager.GetPlayer_2_PreviousPower,
            self.game_Manager.GetPlayer_1_Selected_Pokemon_Power_Increase,
            self.game_Manager.GetPlayer_2_Selected_Pokemon_Power_Increase,
            self.game_Manager.GetPlayer_1_Selected_Pokemon_Power_decrease,
            self.game_Manager.GetPlayer_2_Selected_Pokemon_Power_decrease,
            self.game_Manager.GetBattle_Number
        )
        self.game_Manager.SetBattle_Number = 1
        
        self.game_Manager.BattleWinner()  
        self.display_Manager.DisplayBattleWinner(
            self.game_Manager.Get_Battle_Winner
        )
                      
if __name__ == "__main__":
    Gameplay()