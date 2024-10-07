import PokemonArray as pa

class GameManager:
    def __init__(self) -> None:
        # ==============================================
        # Pokemon Array
        # Contains the list of the available pokemons
        # ==============================================
        self.pokemon_array = list(pa.GetPokemonArray())
        
        # ==============================================
        # Player Pokemon Selection Array
        # Contains the selected pokemons and Index 
        # of both players
        # ==============================================
        self.player_1_array = []
        self.player_2_array = []
        self.player_1_index = []
        self.player_2_index = []
        self.player_1_selected_Pokemon = None
        self.player_2_selected_Pokemon = None
     
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
            print("Select a Maximum of 4 Pokemons\n")
            self.player_1_index = list(map(int, input("Player 1 select sa Pokemon: ").split(" ")))

            if validate_selection(self.player_1_index, 4):
                return True
            if process_selection(self.player_1_index, self.player_1_array):
                return True
        else:
            print(f"Please Select {len(self.player_1_index)} Pokemons")
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

    
    def BattlePokemonSelection(self, index) -> bool:
        if index == 0:
            player1_selection = int(input("Player 1 Select a Pokemon for Battle: "))
            
            if len(str(player1_selection)) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            elif player1_selection > len(self.player_1_array):
                print(f"Selected Index is greater than {len(self.player_1_array)}")
                return True
            elif player1_selection <= 0:
                print(f"Selected Index is less than {len(self.player_1_array)}")
                return True
            else:
                self.player_1_selected_Pokemon = self.player_1_array[player1_selection - 1]
                return False
        else:
            player2_selection = int(input("Player 2 Select a Pokemon for Battle: "))
            
            if len(str(player2_selection)) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            elif player2_selection > len(self.player_2_array):
                print(f"Selected Index is greater than {len(self.player_2_array)}")
                return True
            elif player2_selection <= 0:
                print(f"Selected Index is less than {len(self.player_2_array)}")
                return True
            else:
                self.player_2_selected_Pokemon = self.player_2_array[player2_selection - 1]
                return False
        
    def RandomPowerIncrease(self):
        pass
                              
    # ==================================
    # Methods for Returning Values
    # ==================================
    def GetPokemonInfo(self):
        return self.pokemon_array
    
    def GetPlayer_1_SelectedPokemon(self):
        return self.player_1_array
    
    def GetPlayer_2_SelectedPokemon(self):
        return self.player_2_array
    
    def GetPlayer_1_BattlePokemon(self):
        return self.player_1_selected_Pokemon
    
    def GetPlayer_2_BattlePokemon(self):
        return self.player_2_selected_Pokemon
                