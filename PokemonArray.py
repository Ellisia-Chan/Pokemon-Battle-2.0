pokemon_Array = [
    # [Name, Health, Power, Poisons, Potions]
    ["Pikachu", 100, 55, 0, 5],
    ["Charmander", 120, 60, 1, 3],
    ["Bulbasaur", 90, 50, 2, 4],
    ["Squirtle", 110, 65, 0, 2],
    ["Jigglypuff", 80, 45, 1, 6],
    ["Eevee", 95, 70, 0, 8],
    ["Snorlax", 150, 100, 3, 1],
    ["Gengar", 85, 75, 2, 5],
    ["Machamp", 130, 80, 0, 2],
    ["Mewtwo", 140, 90, 1, 7]
]

def GetPokemonArray() -> list:
    # ============================================
    # Returns the pokemon_Array.
    #
    # Return:
    #     list: A 2D list where each sublist contains the following:
    #     [Name (str), Health (int), Power (int), Poisons (int), Potions (int)].
    # ============================================
    return pokemon_Array