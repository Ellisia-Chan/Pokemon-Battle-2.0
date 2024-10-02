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
        self.player_1 = []
        self.player_2 = []
        self.player_1_index = []
        self.player_2_index = []
     
    # ==============================================
    # Pokemon Selection Method
    # Handles the selection and removing pokemons
    # in the pokemon selection table
    # ==============================================       
    def PokemonSelection(self, index) -> bool:
        selected_indexes = set()
        items_to_remove = []
        
        if index == 0:
            print("Select a Maximum of 4 Pokemons\n")
            self.player_1_index = list(map(int, input("Player 1 select sa Pokemon: ").split(" ")))
            
            if self.player_1_index is None or len(self.player_1_index) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            
            if len(self.player_1_index) > 4:
                print("Selected Pokemon is more than 4. Please Try Again!")
                return True
            
            for items in self.player_1_index:
                if items - 1 >= len(self.pokemon_array):
                    print("Number is Out of Range. Please Try Again!")
                    return True

                if items - 1 in selected_indexes:
                    print("Duplicate Selection. Please Try Again!")
                    return True
                
                # All conditions are met and append the items in the index and selected pokemon array
                selected_indexes.add(items - 1)
                self.player_1.append(self.pokemon_array[items - 1])
                items_to_remove.append(items - 1)
            
            for items in sorted(items_to_remove, reverse=True):
                self.pokemon_array.pop(items)
                    
        else:
            print(f"Please Select {len(self.player_1_index)} Pokemons")
            self.player_2_index = list(map(int, input("Player 2 selects a Pokemon: ").split(" ")))
            
            if self.player_2_index is None or len(self.player_2_index) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True

            if len(self.player_2_index) > len(self.player_1_index):
                print(f"Selected Pokemons is more than {len(self.player_1_index)}. Please Try Again!")
                return True
            
            if len(self.player_2_index) < len(self.player_1_index):
                print(f"Selected Pokemons is less than {len(self.player_1_index)}. Please Try Again!")
                return True
            
            for items in self.player_2_index:
                if items - 1 >= len(self.pokemon_array):
                    print("Number is Out of Range or Duplicate. Please Try Again!")
                    return True
                                   
                if items - 1 in selected_indexes:
                    print("Duplicate Selection. Please Try Again!")
                    return True
                
                # All conditions are met and append the items in the index and selected pokemon array
                selected_indexes.add(items - 1)
                self.player_2.append(self.pokemon_array[items - 1])
                items_to_remove.append(items - 1)
            
            for items in sorted(items_to_remove, reverse=True):
                self.pokemon_array.pop(items)
    
    def PokemonBattleSelection(self):
        pass           
                              
    # ==================================
    # Methods for Returning Values
    # ==================================
    def GetPokemonInfo(self):
        return self.pokemon_array
    
    def GetPlayer_1_SelectedPokemon(self):
        return self.player_1
    
    def GetPlayer_2_SelectedPokemon(self):
        return self.player_2
                