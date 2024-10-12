from prettytable import PrettyTable

class DisplayManager:
    # ==================================
    # Display the title of the program
    # ==================================
    def DisplayProgramInfo(self) -> None:
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"
        print("{:>20}{:>0}".format("", "🔥 Pokemon Battle 🔥"))
        print(f"{YELLOW}INFO:{RESET} Select 3-4 pokemon to be use for battle")
        print(f"💉 {GREEN}Potion{RESET} is used to increase your Power")    
        print(f"💀 {RED}Poison{RESET} is used to decrease opponents Power\n")
        print("⚠ Potion and Poison affects only 1 battle")
        print("⚠ New battle resets power to its base power")
        print("⚠ base power changes depending if winner/loser\n")
        print(f"🎉 {GREEN}Winner:{RESET}")
        print(f"Health {GREEN}increase{RESET} by 5%")
        print(f"Power {GREEN}increase{RESET} by 5%\n")
        print(f"💔 {RED}Loser:{RESET}")
        print(f"Health {RED}decrease{RESET} by 10%")
        print(f"power {GREEN}increase{RESET} by 3%\n")
        print("⚠ Every Battle both Player health is reduced by 2%")
        print("⚠ Due to Fatigue\n")  
        print(f"{YELLOW}⚠ How To End Battle ⚠{RESET}")
        print("- To end battle, all pokemon for both players")
        print("must be used\n")
        
        input("Press Enter To Start")
        print("\033c", end="")
        
        
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
    def DisplayPlayersSelectedPokemons(self, player1, player2, player1_battle_pokemon, player2_battle_pokemon, count, All_pokemon_IsUsed, player1_unused,  player2_unused) -> None:
        table1 = PrettyTable()
        table2 = PrettyTable()
        
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"
        
        table1.title = f"{GREEN}Player 1{RESET}"
        table2.title = f"{RED}Player 2{RESET}"
        table1.field_names = ["Index", "Pokemon", "Health", "Power", "Poison", "Potion", "Used"]
        table2.field_names = ["Index", "Pokemon", "Health", "Power", "Poison", "Potion", "Used"]

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
            
        if All_pokemon_IsUsed == True:
            all_Pokemon_Used = f"{GREEN}YES{RESET}"
        else: all_Pokemon_Used = f"{RED}NO{RESET}"
        
        print("{:>45}{:>0}".format("", "🔥 Battle Pokemon Selection 🔥"))
        print("{:<2}{:<0}".format("", f"{YELLOW}INFO:{RESET} To end battle, All players must use all selected pokemon.\n"))
        print("{:<2}{:<0}".format("", f"All Pokemon Used?: {all_Pokemon_Used}")) 
        print("{:<2}{:<0}".format("", f"Player 1 Unused: {RED}{player1_unused}{RESET}"))
        print("{:<2}{:<0}".format("", f"Player 2 Unused: {RED}{player2_unused}{RESET}"))
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
        GREEN = "\033[32m"
        RED = "\033[31m"
        RESET = "\033[0m"
        COLOR = GREEN if count == 0 else RED
        
        table = PrettyTable()

        table.title = f"{COLOR}Player {count + 1}{RESET}"
        table.field_names = ["Pokemon", "Health", "Power", "Poison", "Potion"]
        
        player_pokemon = player_selected[0] 
        player_health = player_selected[1]
        player_power = player_selected[2]
        player_poisons = player_selected[3]
        player_potions = player_selected[4]
        
        table.add_row([player_pokemon, player_health, player_power, player_poisons, player_potions])
        
        print("{:>13}{:>0}".format("", "🔥 Battle Preparation 🔥"))
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
        player2_powerDecrease: list,
        battleNumber: int) -> None:
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
        
        def __ValidatePowerDetailsFormat(player_power_increase, player_power_decrease, player_previous_power, player_final_power) -> str:
            details_str = ""
            if len(player_power_increase) != 0:
                details_str += f"Power Increase By Potion\n"
                details_str += f"{player_previous_power} + {GREEN}{player_power_increase[1]}{RESET} = {GREEN}{player_power_increase[0]}{RESET}\n"      
            else:
                details_str += f"No Power Increase\n"
                details_str += f" \n"
                
            if len(player_power_decrease) != 0:
                if len(player_power_increase) != 0:
                    player_power = player_power_increase[0]
                else:
                    player_power = player_previous_power
                    
                details_str += f"Power Decreased By Opponents Poison\n"
                details_str += f"{player_power} - {RED}{player_power_decrease[1]}{RESET} = {RED}{player_power_decrease[0]}{RESET}\n"
            else:
                details_str += f"No Power Decreased\n"
                details_str += f" \n"
                           
            details_str += f"{GREEN}Final Power: {player_final_power}{RESET}\n"

            return details_str
        
        previewTable1.title = f"{GREEN}Player 1{RESET}"
        previewTable2.title = f"{RED}Player 2{RESET}"
        
        
        previewTable1.field_names = ["Pokemon", "Health", "Power"]
        previewTable2.field_names = ["Pokemon", "Health", "Power"]
        
        player1_index = player1_pokemon
        player1_pokemonName = player1_index[0]
        player1_health = player1_index[1]
        player1_power = player1_index[2]
        
        player2_index = player2_pokemon
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
        
        print(preview_combined_Table)
        input("Press Enter to Begin Battle")
        print("\033c", end="")
        
        # Main tables to display actual stats after battle
        mainTable1 = PrettyTable()
        mainTable2 = PrettyTable()
        statsDetailsTable1 = PrettyTable()
        statsDetailsTable2 = PrettyTable()
        
        mainTable1.title = f"{GREEN}Player 1{RESET}"
        mainTable2.title = f"{RED}Player 2{RESET}"              
        mainTable1.field_names = ["Pokemon", "Health", "Power"]
        mainTable2.field_names = ["Pokemon", "Health", "Power"]
        
        statsDetailsTable1.field_names = [f"{GREEN}Player 1{RESET}"]
        statsDetailsTable2.field_names = [f"{RED}Player 2{RESET}"]
          
        player1_final_power = __ValidateFinalPowerFormat(player1_power, player1_previousPower)
        player2_final_power = __ValidateFinalPowerFormat(player2_power, player2_previousPower)
        
        player1_power_details = __ValidatePowerDetailsFormat(player1_powerIncrease,
                                                             player1_powerDecrease,
                                                             player1_previousPower,
                                                             player1_power)
        
        player2_power_details = __ValidatePowerDetailsFormat(player2_powerIncrease,
                                                             player2_powerDecrease,
                                                             player2_previousPower,
                                                             player2_power)
        
        mainTable1.add_row([player1_pokemonName, player1_health, player1_final_power])
        mainTable2.add_row([player2_pokemonName, player2_health, player2_final_power])
        statsDetailsTable1.add_row([player1_power_details])
        statsDetailsTable2.add_row([player2_power_details])
        
        mainTable1_str = mainTable1.get_string().splitlines()
        mainTable2_str = mainTable2.get_string().splitlines()
        statsDetailsTable1_str = statsDetailsTable1.get_string().splitlines()
        statsDetailsTable2_str = statsDetailsTable2.get_string().splitlines()
        
        main_combined_Table = ""
        stats_detail_combined_Table = ""
        for row1, row2, in zip(mainTable1_str, mainTable2_str):
            main_combined_Table += f"{row1}  {row2}\n"
        
        for row1, row2, in zip(statsDetailsTable1_str, statsDetailsTable2_str):
            stats_detail_combined_Table += f"{row1}  {row2}\n"
        
        print("{:<30}{:<0}".format("", f"Battle {battleNumber+1}"))     
        print(main_combined_Table)
        print(stats_detail_combined_Table)
    
    def DisplayBattleWinner(self, Winner, power_difference_str,
                            player1_win, player2_win, tie):
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"
        
        print("{:<20}{:<0}".format("", "======== Battle Winner ========"))
        print("{:<28}{:<0}".format("", f"🎉 {Winner} 🎉\n"))
        print("{:<32}{:<0}".format("", f"{power_difference_str}\n"))
        print("{:<13}{:<28}{:<28}{:<0}".format(
            "",
            f"{GREEN}Player 1{RESET} Wins: {player1_win}",
            f"{RED}Player 2{RESET} Wins: {player2_win}",
            f"Ties: {tie}"))
        input("\nPress Enter to Continue")
        print("\033c", end="")
        
    def DisplayBattleStatsAdjustment(self, winner,
                                     player1_pokemon, player1_prev_HP, player1_prev_Pwr,
                                     player2_pokemon, player2_prev_HP, player2_prev_Pwr
                                     ):
        GREEN = "\033[32m"
        RED = "\033[31m"
        YELLOW = "\033[33m"
        RESET = "\033[0m"
        
        def __Create_HP_PWR_STR_Format():
            # Player 1 Table
            if player1_prev_HP < player1_pokemon[1]:
                p1_HP_str = f"{player1_prev_HP} -> {GREEN}{player1_pokemon[1]}{RESET}"
            else:
                p1_HP_str = f"{player1_prev_HP} -> {RED}{player1_pokemon[1]}{RESET}"
                
            if player1_prev_Pwr < player1_pokemon[2]:
                p1_Pwr_str = f"{player1_prev_Pwr} -> {GREEN}{player1_pokemon[2]}{RESET}"
            else:
                p1_Pwr_str = f"{player1_prev_Pwr} -> {RED}{player1_pokemon[2]}{RESET}"
                
            # player 2 Table
            if player2_prev_HP < player2_pokemon[1]:
                p2_HP_str = f"{player2_prev_HP} -> {GREEN}{player2_pokemon[1]}{RESET}"
            else:
                p2_HP_str = f"{player2_prev_HP} -> {RED}{player2_pokemon[1]}{RESET}"
                
            if player2_prev_Pwr < player2_pokemon[2]:
                p2_Pwr_str = f"{player2_prev_Pwr} -> {GREEN}{player2_pokemon[2]}{RESET}"
            else:
                p2_Pwr_str = f"{player2_prev_Pwr} -> {RED}{player2_pokemon[2]}{RESET}"
            
            return p1_HP_str, p2_HP_str, p1_Pwr_str, p2_Pwr_str
        
        winner_perc_table = PrettyTable()
        loser_perc_table = PrettyTable()
        winner_table = PrettyTable()
        loser_table = PrettyTable()
        
        winner_table.field_names = ["Pokemon", "Health", "Power"]
        loser_table.field_names = ["Pokemon", "Health", "Power"]
        
        if winner == f"{GREEN}Player 1{RESET}":
            winner_table.title = f"Winner: {GREEN}Player 1{RESET}"
            loser_table.title = f"Loser: {RED}Player 2{RESET}"
            winner_perc_table.field_names = [f"Winner: {GREEN}Player 1{RESET}"]
            loser_perc_table.field_names = [f"Loser: {RED}Player 2{RESET}"]
            
            p1_Hp, p2_Hp, p1_Pwr, p2_Pwr = __Create_HP_PWR_STR_Format()
            
            winner_table.add_row([player1_pokemon[0], p1_Hp, p1_Pwr])
            loser_table.add_row([player2_pokemon[0], p2_Hp, p2_Pwr])
            
            winner_perc_table.add_row(["Health +5% - Power +5%"])
            loser_perc_table.add_row(["Health -10% - Power +3%"])
        elif winner == f"{RED}Player 2{RESET}":
            winner_table.title = f"Winner: {RED}Player 2{RESET}"
            loser_table.title = f"Loser: {GREEN}Player 1{RESET}"
            winner_perc_table.field_names = [f"Winner: {RED}Player 2{RESET}"]
            loser_perc_table.field_names = [f"Loser: {GREEN}Player 1{RESET}"]
            
            p1_Hp, p2_Hp, p1_Pwr, p2_Pwr = __Create_HP_PWR_STR_Format()
            
            winner_table.add_row([player2_pokemon[0], p2_Hp, p2_Pwr])
            loser_table.add_row([player1_pokemon[0], p1_Hp, p1_Pwr])
            
            winner_perc_table.add_row(["Health +5% - Power +5%"])
            loser_perc_table.add_row(["Health -10% - Power +3%"])
            
        winner_perc_table_str = winner_perc_table.get_string().splitlines()
        loser_perc_table_str = loser_perc_table.get_string().splitlines()
        winner_table_str = winner_table.get_string().splitlines()
        loser_table_str = loser_table.get_string().splitlines()
        
        
        main_combine_Table = ""
        perc_combine_Table = ""
        for row1, row2 in zip(winner_table_str, loser_table_str):
            main_combine_Table += f"{row1}  {row2}\n"
            
        for row1, row2 in zip(winner_perc_table_str, loser_perc_table_str):
            perc_combine_Table += f"{row1}  {row2}\n"
        
        print("{:<30}{:<0}".format("", "Stats Adjustment\n"))
        print(perc_combine_Table)
        print(main_combine_Table)
        
        input("Press Enter to Continue")
        print("\033c", end="")
 
    def DisplayFatigueAdjustment(self):  
        print("{:<33}{:<0}".format("", "Pokemon Fatigue Effects\n"))
        input()
        
        