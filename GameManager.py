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
        selected_indexes = set()
        items_to_remove = []
        
        if index == 0:
            print("Select a Maximum of 4 Pokemons\n")
            self.player_1_index = list(map(int, input("Player 1 select sa Pokemon: ").split(" ")))
            
            if len(self.player_1_index) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            elif len(self.player_1_index) > 4:
                print("Selected Pokemon is more than 4. Please Try Again!")
                return True
            else:
                for items in self.player_1_index:
                    if items - 1 >= len(self.pokemon_array):
                        print("Number is Out of Range. Please Try Again!")
                        return True
                    elif items - 1 in selected_indexes:
                        print("Duplicate Selection. Please Try Again!")
                        return True
                    
                    # All conditions are met and append the items in the index and selected pokemon array
                    selected_indexes.add(items - 1)
                    self.player_1_array.append(self.pokemon_array[items - 1])
                    items_to_remove.append(items - 1)
                
                for items in sorted(items_to_remove, reverse=True):
                    self.pokemon_array.pop(items)      
                return False           
        else:
            print(f"Please Select {len(self.player_1_index)} Pokemons")
            self.player_2_index = list(map(int, input("Player 2 selects a Pokemon: ").split(" ")))
            
            if len(self.player_2_index) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            elif len(self.player_2_index) > len(self.player_1_index):
                print(f"Selected Pokemons is more than {len(self.player_1_index)}. Please Try Again!")
                return True
            elif len(self.player_2_index) < len(self.player_1_index):
                print(f"Selected Pokemons is less than {len(self.player_1_index)}. Please Try Again!")
                return True
            else:
                for items in self.player_2_index:
                    if items - 1 >= len(self.pokemon_array):
                        print("Number is Out of Range. Please Try Again!")
                        return True
                                    
                    if items - 1 in selected_indexes:
                        print("Duplicate Selection. Please Try Again!")
                        return True
                    
                    # All conditions are met and append the items in the index and selected pokemon array
                    selected_indexes.add(items - 1)
                    self.player_2_array.append(self.pokemon_array[items - 1])
                    items_to_remove.append(items - 1)
                
                for items in sorted(items_to_remove, reverse=True):
                    self.pokemon_array.pop(items)
                return False
    
    def BattlePokemonSelection(self, index):
        if index == 0:
            player1_selection = int(input("Player 1 Select a Pokemon for Battle: "))
            
            if len(str(player1_selection)) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            
            self.player_1_selected_Pokemon = self.player_1_array[player1_selection - 1]
            return False
        else:
            player2_selection = int(input("Player 2 Select a Pokemon for Battle: "))
            
            if len(str(player2_selection)) == 0:
                print("No Selected Pokemon. Please Try Again!")
                return True
            
            self.player_2_selected_Pokemon = self.player_2_array[player2_selection - 1]
            return False
                              
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
                