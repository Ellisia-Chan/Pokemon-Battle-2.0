from prettytable import PrettyTable

class DisplayManager:
    # ==================================
    # Display the title of the program
    # ==================================
    def DisplayProgramInfo(self) -> None:
        print("{:>20}{:>0}".format("", "🔥 Pokemon Battle 🔥"))
        #print("".format("", "Select a list of pokemons"))
    
    # ====================================
    # Display a table of all the available
    # Pokemons for the player to select
    # ====================================   
    def DisplayPokemonSelection(self, pokemon_List) -> None:
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
    
    # ===========================================
    # Display a table of all the selected pokemons
    # of both players
    # ===========================================
    def DisplayPlayersSelectedPokemons(self, player1, player2, player1_battle_pokemon, player2_battle_pokemon, count) -> None:
        table1 = PrettyTable()
        table2 = PrettyTable()
        
        table1.field_names = ["Index", "Pokemon", "Health", "Power", "Poison", "Potion", "Used"]
        table2.field_names = ["Index", "Pokemon", "Health", "Power", "Poison", "Potion", "Used"]

        GREEN = "\033[32m"
        RED = "\033[31m"
        RESET = "\033[0m"
        for i in range(len(player1)):
            # Player 1 
            player1_index = player1[i]
            player1_pokemon = player1_index[0]
            player1_health = player1_index[1]
            player1_power = player1_index[2]
            player1_poisons = player1_index[3]
            player1_potions = player1_index[4]
            
            player1_isUsed = f"{GREEN}Yes{RESET}" if player1_index[5] == True else f"{RED}No{RESET}"
            
            if count == 0:
                table1.add_row([i+1,
                                player1_pokemon,
                                player1_health,
                                player1_power,
                                player1_poisons,
                                player1_potions,
                                player1_isUsed])
            else:
                table1.add_row([i+1, player1_pokemon, "?", "?", "?", "?", "?"])

            # Player 2
            player2_index = player2[i]
            player2_pokemon = player2_index[0]
            player2_health = player2_index[1]
            player2_power = player2_index[2]
            player2_poisons = player2_index[3]
            player2_potions = player2_index[4]
            
            player2_isUsed = f"{GREEN}Yes{RESET}" if player2_index[5] == True else f"{RED}No{RESET}"

            if count == 1:
                table2.add_row([i+1,
                                player2_pokemon,
                                player2_health,
                                player2_power,
                                player2_poisons,
                                player2_potions,
                                player2_isUsed])
            else:
                table2.add_row([i+1, player2_pokemon, "?", "?", "?", "?", "?"])

        table1_str = table1.get_string().splitlines()
        table2_str = table2.get_string().splitlines()
        
        combined_Table = ""
        for row1, row2 in zip(table1_str, table2_str):
            combined_Table += f"{row1}  {row2}\n"
        
        print("{:>45}{:>0}".format("", "🔥 Battle Pokemon Selection 🔥")) 
        print("{:<23}{:<65}{:<0}".format(
            "",
            "Player 1",
            "Player 2"   
        ))
        print(combined_Table)
    
        if len(player1_battle_pokemon) == 0:
            player1_battle_pokemon = ""
        else:
            player1_battle_pokemon = f"🔥 {player1_battle_pokemon[0]} 🔥"
            
        if len(player2_battle_pokemon) == 0:
            player2_battle_pokemon = ""
        else:    
            player2_battle_pokemon = f"🔥 {player2_battle_pokemon[0]} 🔥"
            
        print("{:<10}{:<60}{:<0}".format(
            "",
            f"Player 1 Pokemon: {player1_battle_pokemon}",
            f"Player 2 Pokemon: {player2_battle_pokemon}\n"
        ))
        
    # =======================================
    # Display Player stats where they can use
    # poison and potions
    # ====================================== 
    def DisplayBattlePreparation(self, player_selected, count) -> None:
        table = PrettyTable()

        table.field_names = ["Pokemon", "Health", "Power", "Poison", "Potion"]
        
        player_pokemon = player_selected[0] 
        player_health = player_selected[1]
        player_power = player_selected[2]
        player_poisons = player_selected[3]
        player_potions = player_selected[4]
        
        table.add_row([player_pokemon, player_health, player_power, player_poisons, player_potions])
        
        print("{:>15}{:>0}".format("", "Battle Preparation"))
        print("{:>20}{:>0}".format("", f"Player {count + 1}"))
        print(table)
        print()
    
    # ===========================================
    # Display The final stats of both pokemon
    # this includes the poison and potion effects
    # ===========================================
    def DisplayMainBattleStats(self,
        player1_pokemon,
        player2_pokemon,
        player1_previousPower,
        player2_previousPower,
        player1_powerIncrease: list,
        player2_powerIncrease: list,
        player1_powerDecrease: list,
        player2_powerDecrease: list) -> None:
        previewTable1 = PrettyTable()
        previewTable2 = PrettyTable()
        
        # Color for string formatting
        GREEN = "\033[32m"
        RED = "\033[31m"
        RESET = "\033[0m"
        
        def __ValidateFinalPowerFormat(player_finalPower, player_previousPower) -> str:
            if player_finalPower > player_previousPower :
                player_final_power = f"{player_previousPower} -> {GREEN}{player_finalPower}{RESET}"
            elif player_finalPower < player_previousPower:
                player_final_power = f"{player_previousPower} -> {RED}{player_finalPower}{RESET}"
            else:
                player_final_power = f"{player_previousPower} -> {player_finalPower}"
            return player_final_power
        
        def __ValidatePowerDetailsFormat(player_power_increase, player_power_decrease, player_previous_power, player_final_power):
            pass 
        
        mainTable1 = PrettyTable()
        mainTable2 = PrettyTable()
        
        previewTable1.field_names = ["Pokemon", "Health", "Power"]
        previewTable2.field_names = ["Pokemon", "Health", "Power"]
        mainTable1.field_names = ["Pokemon", "Health", "Power"]
        mainTable2.field_names = ["Pokemon", "Health", "Power"]
        
        player1_index = player1_pokemon[0]
        player1_pokemonName = player1_index[0]
        player1_health = player1_index[1]
        player1_power = player1_index[2]
        
        player2_index = player2_pokemon[0]
        player2_pokemonName = player2_index[0]
        player2_health = player2_index[1]
        player2_power = player2_index[2]
        
        previewTable1.add_row([player1_pokemonName, "?", "?"])
        previewTable2.add_row([player2_pokemonName, "?", "?"])
        
        previewTable1_str = previewTable1.get_string().splitlines()
        previewTable2_str = previewTable2.get_string().splitlines()
        
        preview_combined_Table = ""
        for row1, row2 in zip(previewTable1_str, previewTable2_str):
            preview_combined_Table += f"{row1}  {row2}\n"
        
        print("{:<20}{:<20}{:<0}".format(
            "",
            "Player 1",
            "Player 2"
        ))
        print(preview_combined_Table)
        input("Press Enter to Begin Battle")
        
        # Main tables to display actual stats after battle
        mainTable1 = PrettyTable()
        mainTable2 = PrettyTable()
        statsDetailsTable1 = PrettyTable()
        statsDetailsTable2 = PrettyTable()        
        
        mainTable1.field_names = ["Pokemon", "Health", "Power"]
        mainTable2.field_names = ["Pokemon", "Health", "Power"]
          
        player1_final_power = __ValidateFinalPowerFormat(player1_power, player1_previousPower)
        player2_final_power = __ValidateFinalPowerFormat(player2_power, player2_previousPower)
        player1_power_details = __ValidatePowerDetailsFormat(player1_powerIncrease, player1_powerDecrease, player1_previousPower, player1_final_power)
        player2_power_details = __ValidatePowerDetailsFormat(player2_powerIncrease, player2_powerDecrease, player2_previousPower, player2_final_power)
        
        mainTable1.add_row([player1_pokemonName, player1_health, player1_final_power])
        mainTable2.add_row([player2_pokemonName, player2_health, player2_final_power])
        
        mainTable1_str = mainTable1.get_string().splitlines()
        mainTable2_str = mainTable2.get_string().splitlines()
        
        main_combined_Table = ""
        for row1, row2, in zip(mainTable1_str, mainTable2_str):
            main_combined_Table += f"{row1}  {row2}\n"
        
        print(main_combined_Table)
        print(player1_powerIncrease)
        print(player1_powerDecrease)
        print()
        print(player2_powerIncrease)
        print(player2_powerDecrease)
        
        input()           