import PokemonArray as pa
import random
import time

class GameManager:
    def __init__(self) -> None:
        # ==============================================
        # Pokemon Array
        # Contains the list of the available pokemons
        # ==============================================
        pokemonArray = pa.PokemonArray()
        self.pokemon_array = list(pokemonArray.GetPokemonArray)
        
        # ==============================================
        # Player Pokemon Selection Array
        # Contains the selected pokemons and Index 
        # of both players
        # ==============================================
        self.player_1_array = []
        self.player_2_array = []
        self.player_1_index = []
        self.player_2_index = []
        self.player_1_selected_Pokemon = []
        self.player_2_selected_Pokemon = []
        
        # Contains: 
        # Index 0 = Power Increase/Decrease
        # Index 1 = Percentage of Increase/Decrease
        self.player_1_selected_Pokemon_Power_Increase = []
        self.player_1_selected_Pokemon_Power_Decrease = []
        self.player_2_selected_Pokemon_Power_Increase = []
        self.player_2_selected_Pokemon_Power_Decrease = []
        
        # ==================================
        # Battle Number counter and Winner
        # ==================================
        self.battle_number = 0
        self.Battle_Winner = ""
        
        # =======================================
        # Stats holder for previous values for
        # health and power after poison and potion
        # are applied
        # =======================================
        self.player_1_previous_health = None
        self.player_2_previous_health = None
        self.player_1_previous_power = None
        self.player_2_previous_power = None
     
    # ==============================================
    # Pokemon Selection Method
    # Handles the selection and removing pokemons
    # in the pokemon selection table
    # ==============================================       
    def PokemonArraySelection(self, index) -> bool:
        selected_indexes = []
        items_to_remove = []

        def validate_selection(selected, max_limit):
            if len(selected) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            if len(selected) > max_limit:
                print(f"Selected Pokemons is more than {max_limit}. Please Try Again!")
                return True
            return False

        def process_selection(selected, player_array):
            for item in selected:
                idx = item - 1
                if idx >= len(self.pokemon_array):
                    print("Number is Out of Range. Please Try Again!")
                    return True
                if idx in selected_indexes:
                    print("Duplicate Selection. Please Try Again!")
                    player_array.clear()
                    return True
                selected_indexes.append(idx)
                player_array.append(self.pokemon_array[idx])
                items_to_remove.append(idx)
            return False

        if index == 0:
            print("Select a Maximum of 4 Pokemons\nINFO: Select 3-4 Pokemons to use for battle (Ex. Input: 1 2 3 4)\n")
            self.player_1_index = list(map(int, input("Player 1 select sa Pokemon: ").split(" ")))

            if validate_selection(self.player_1_index, 4):
                return True
            if process_selection(self.player_1_index, self.player_1_array):
                return True
        else:
            print(f"Please Select {len(self.player_1_index)} Pokemons\nINFO: Select 3-4 Pokemons to use for battle (Ex. Input: 1 2 3 4)\n")
            self.player_2_index = list(map(int, input("Player 2 selects a Pokemon: ").split(" ")))

            if validate_selection(self.player_2_index, len(self.player_1_index)):
                return True
            if len(self.player_2_index) < len(self.player_1_index):
                print(f"Selected Pokemons is less than {len(self.player_1_index)}. Please Try Again!")
                return True
            if process_selection(self.player_2_index, self.player_2_array):
                return True

        for item in sorted(items_to_remove, reverse=True):
            self.pokemon_array.pop(item)       
        return False

    # ===========================================
    # Selection of pokemon that will be use for
    # Battle
    # ==========================================
    def BattlePokemonSelection(self, index) -> bool:
        print("Select 1 pokemon to use for battle\n")        
        player_selection = int(input(f"Player {index + 1} Select a Pokemon for Battle: "))
        
        player_array = self.player_1_array if index == 0 else self.player_2_array
        selected_pokemon_attr = 'player_1_selected_Pokemon' if index == 0 else 'player_2_selected_Pokemon'

        if player_selection <= 0:
            print(f"Selected Index is less than or equal to zero. Please try again.")
            return True
        elif player_selection > len(player_array):
            print(f"Selected Index is greater than {len(player_array)}. Please try again.")
            return True
        else:
            setattr(self, selected_pokemon_attr, player_array[player_selection - 1])
            selected_pokemon = getattr(self, selected_pokemon_attr)
            selected_pokemon[5] = True
            
            return False
    
    def BattlePreparation(self, index) -> bool:
        player_selected = self.player_1_selected_Pokemon if index == 0 else self.player_2_selected_Pokemon
        
        player_actions = {"use_potion": False, "use_poison": False}
        
         # Helper methods for potion and poison effects
        def __UsePotion(player) -> int:
            percentage = random.choice([0.50, 0.30, 0.10])
            
            if percentage == 0.50: percentage_str = "50%" 
            elif percentage == 0.30: percentage_str = "30%"
            elif percentage == 0.10: percentage_str = "10%" 
            
            power_increase = int(player[2] * percentage)
            player[2] += power_increase
            player[4] -= 1  # Decrease potion count
            
            return player[2], percentage_str

        def __UsePoison(opponent, player) -> int:
            percentage = random.choice([0.50, 0.30, 0.10])
            
            if percentage == 0.50: percentage_str = "50%" 
            elif percentage == 0.30: percentage_str = "30%"
            elif percentage == 0.10: percentage_str = "10%"
            
            power_decrease = int(opponent[2] * percentage)
            opponent_newPower = max((opponent[2] - power_decrease), 1)  # Minimum power of 1
            player[3] -= 1  # Decrease poison count
               
            return opponent_newPower, percentage_str
        
        if player_selected[3] == 0 and player_selected[4] == 0:
            print("No available Poison and Potions")
            input("Press enter to continue\n")
            
            if index == 0:
                self.player_1_actions = player_actions
                self.player_1_previous_power = self.player_1_selected_Pokemon[2]           
            else:
                self.player_2_actions = player_actions
                self.player_2_previous_power = self.player_2_selected_Pokemon[2]
            return
        
        # Poison action prompt refactored
        if player_selected[3] > 0:
            print("INFO: Poison Reduce Opponents Power by Random Percentage (10%, 30%, 50%)\n")
            use_poison = input("Use poison on the opponent? [Y/N]: ").strip().lower()
            if use_poison == "y":
                player_actions["use_poison"] = True
                print("Poison will be applied to the opponent\n")
                time.sleep(1)
            elif use_poison == "n":
                print("No Poison used\n")
                time.sleep(1)
            else:
                print("Invalid input. Please try again.")
                return True
        else:
            print("No available Poison")
            input("Press enter to continue\n")
        
        # Potion action prompt refactored
        if player_selected[4] > 0:
            print("INFO: Potion Increase Your Pokemon Power by Random Percentage (10%, 30%, 50%)\n")
            use_potion = input("Use Potion to increase power? [Y/N]: ").strip().lower()
            if use_potion == "y":
                player_actions["use_potion"] = True
                print("Potion will be applied\n")
                time.sleep(1)
            elif use_potion == "n":
                print("No Potion used\n")
                time.sleep(1)
            else:
                print("Invalid input. Please try again.")
                return True
        else:
            print("No available Potion")
            input("Press enter to continue\n")
            
        if index == 0:
            self.player_1_actions = player_actions
        else:
            self.player_2_actions = player_actions
            
        if hasattr(self, "player_1_actions") and hasattr(self, "player_2_actions"):
            self.player_1_previous_power = self.player_1_selected_Pokemon[2]
            self.player_2_previous_power = self.player_2_selected_Pokemon[2]
            
            power_Decrease_player1 = 0
            power_Decrease_player2 = 0
            
            # Player 1|2 Potions Actions
            if self.player_1_actions["use_potion"]:
                power_Increase, perct = __UsePotion(self.player_1_selected_Pokemon)
                self.player_1_selected_Pokemon_Power_Increase.append(power_Increase)
                self.player_1_selected_Pokemon_Power_Increase.append(perct)
                
            if self.player_2_actions["use_potion"]:
                power_Increase, perct = __UsePotion(self.player_2_selected_Pokemon)
                self.player_2_selected_Pokemon_Power_Increase.append(power_Increase)
                self.player_2_selected_Pokemon_Power_Increase.append(perct) 
   
            # Player 1|2 Poison Action
            if self.player_1_actions["use_poison"]:
                power_Decrease_player2, perct = __UsePoison(self.player_2_selected_Pokemon, self.player_1_selected_Pokemon)
                self.player_2_selected_Pokemon_Power_Decrease.append(power_Decrease_player2)
                self.player_2_selected_Pokemon_Power_Decrease.append(perct)
                
            if self.player_2_actions["use_poison"]:
                power_Decrease_player1, perct = __UsePoison(self.player_1_selected_Pokemon, self.player_2_selected_Pokemon)
                self.player_1_selected_Pokemon_Power_Decrease.append(power_Decrease_player1)
                self.player_1_selected_Pokemon_Power_Decrease.append(perct)

            if power_Decrease_player1 != 0:
                self.player_1_selected_Pokemon[2] = power_Decrease_player1   
            if power_Decrease_player2 != 0:
                self.player_2_selected_Pokemon[2] = power_Decrease_player2
                
            # Clear actions after applying to both players
            del self.player_1_actions
            del self.player_2_actions
            
        return False
    
    def BattleWinner(self):
        GREEN = "\033[32m"
        RED = "\033[31m"
        RESET = "\033[0m"
        if self.player_1_selected_Pokemon[2] > self.player_2_selected_Pokemon[2]:
            self.Battle_Winner = "Player 1"
            self.power_difference_str = f"{GREEN}{self.player_1_selected_Pokemon[2]}{RESET} > {RED}{self.player_2_selected_Pokemon[2]}{RESET}"
            
            self.player_1_selected_Pokemon[1] += int(self.player_1_selected_Pokemon[1] * 0.10)
            self.player_1_selected_Pokemon[2] = self.player_1_previous_power + int(self.player_1_previous_power * 0.05)
            
            self.player_2_selected_Pokemon[1] += int(self.player_2_selected_Pokemon[1] * 0.05)
            self.player_2_selected_Pokemon[2] = self.player_2_previous_power + int(self.player_2_previous_power * 0.03)
                       
        elif self.player_1_selected_Pokemon[2] < self.player_2_selected_Pokemon[2]:
            self.Battle_Winner = "Player 2"
            self.power_difference_str = f"{RED}{self.player_1_selected_Pokemon[2]}{RESET} < {GREEN}{self.player_2_selected_Pokemon[2]}{RESET}"
            
            self.player_2_selected_Pokemon[1] += int(self.player_2_selected_Pokemon[1] * 0.10)
            self.player_2_selected_Pokemon[2] = self.player_2_previous_power + int(self.player_2_previous_power * 0.05)
            
            self.player_1_selected_Pokemon[1] += int(self.player_1_selected_Pokemon[1] * 0.05)
            self.player_1_selected_Pokemon[2] = self.player_1_selected_Pokemon[2] + int(self.player_1_previous_power * 0.03)            
        else:
            self.Battle_Winner = "Tie"
            self.power_difference_str = f"{self.player_1_selected_Pokemon[2]} == {self.player_2_selected_Pokemon[2]}"
            
            self.player_1_selected_Pokemon[2] = self.player_1_previous_power
            self.player_2_selected_Pokemon[2] = self.player_2_previous_power
    
    def FatigueEffects(self):
        pass
    
    # =======================================
    # Method for setting Values
    # =======================================
    def SetSelectedPokemonsToNull(self):
        self.player_1_selected_Pokemon = []
        self.player_2_selected_Pokemon = []
    
    def SetChangedPokemonPowerToNull(self):
        self.player_1_selected_Pokemon_Power_Increase = []
        self.player_1_selected_Pokemon_Power_Decrease = []
        self.player_2_selected_Pokemon_Power_Increase = []
        self.player_2_selected_Pokemon_Power_Decrease = []

    # ==================================
    # Methods for Returning Values
    # ==================================
    @property
    def GetPokemonInfo(self) -> list:
        return self.pokemon_array
    
    # return Selected Pokemon Array
    @property
    def GetPlayer_1_SelectedPokemon(self) -> list:
        return self.player_1_array
    
    @property
    def GetPlayer_2_SelectedPokemon(self) -> list:
        return self.player_2_array
    
    # return selected battle pokemon
    @property
    def GetPlayer_1_BattlePokemon(self) -> list:
        return self.player_1_selected_Pokemon
    
    @property
    def GetPlayer_2_BattlePokemon(self) -> list:
        return self.player_2_selected_Pokemon
    
    # return previous health of pokemons after a battle
    # which is affected by fatigue and increase by 
    # 10 and 5 points
    @property
    def GetPlayer_1_previousHealth(self) -> int:
        return self.player_1_previous_health

    @property
    def GetPlayer_2_previousHealth(self) -> int:
        return self.player_2_previous_health
    
    # return previous power after poison and poitons
    # are applied
    @property
    def GetPlayer_1_PreviousPower(self) -> int:
        return self.player_1_previous_power
    
    @property
    def GetPlayer_2_PreviousPower(self) -> int:
        return self.player_2_previous_power
    
    # Return power increase
    @property
    def GetPlayer_1_Selected_Pokemon_Power_Increase(self) -> list:
        return self.player_1_selected_Pokemon_Power_Increase
    
    @property
    def GetPlayer_2_Selected_Pokemon_Power_Increase(self) -> list:
        return self.player_2_selected_Pokemon_Power_Increase
    
    # Return power Decrease
    @property
    def GetPlayer_1_Selected_Pokemon_Power_decrease(self) -> list:
        return self.player_1_selected_Pokemon_Power_Decrease
    
    @property
    def GetPlayer_2_Selected_Pokemon_Power_decrease(self) -> list:
        return self.player_2_selected_Pokemon_Power_Decrease
    
    # Return Battle Number
    @property
    def GetBattle_Number(self) -> int:
        return self.battle_number
    
    # Increase Battle Number
    @GetBattle_Number.setter
    def SetBattle_Number(self, value) -> None:
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.battle_number += value
    
    @property
    def Get_Battle_Winner(self) -> str:
        return self.Battle_Winner
    
    @property
    def Get_Power_Difference_str(self) -> str:
        return self.power_difference_str