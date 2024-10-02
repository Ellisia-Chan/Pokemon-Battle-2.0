from prettytable import PrettyTable

class Display:
    def DisplayProgramInfo(self):
        print("{:>20}{:>0}".format("", "Pokemon Battle"))
        
    def DisplayPokemonSelection(self, pokemon_List):
        table = PrettyTable()

        table.field_names = ["Index", "Pokemon", "Health", "Power", "Poison", "Potion"]

        for i in range(len(pokemon_List)):
            pokemon_list_index = pokemon_List[i]
            pokemon = pokemon_list_index[0]
            health = pokemon_list_index[1]
            power = pokemon_list_index[2]
            poisons = pokemon_list_index[3]
            potions = pokemon_list_index[4]
            table.add_row([i+1, pokemon, health, power, poisons, potions])
        print(table)
        print()
    
    def DisplayPlayersSelectedPokemons(self, player1, player2):
        table1 = PrettyTable()
        table2 = PrettyTable()
        
        table1.field_names = ["Pokemon", "Health", "Power", "Poison", "Potion"]
        table2.field_names = ["Pokemon", "Health", "Power", "Poison", "Potion"]
        
        for i in range(len(player1)):
            # Player 1 
            player1_index = player1[i]
            player1_pokemon = player1_index[0]
            player1_health = player1_index[1]
            player1_power = player1_index[2]
            player1_poisons = player1_index[3]
            player1_potions = player1_index[4]
            table1.add_row([player1_pokemon, player1_health, player1_power, player1_poisons, player1_potions])
        
            # Player 2
            player2_index = player2[i]
            player2_pokemon = player2_index[0]
            player2_health = player2_index[1]
            player2_power = player2_index[2]
            player2_poisons = player2_index[3]
            player2_potions = player2_index[4]
            table2.add_row([player2_pokemon, player2_health, player2_power, player2_poisons, player2_potions])
            
        table1_str = table1.get_string().splitlines()
        table2_str = table2.get_string().splitlines()
        
        combined_Table = ""
        for row1, row2 in zip(table1_str, table2_str):
            combined_Table += f"{row1}  {row2}\n"
            
        print(combined_Table)
        print()
            
            