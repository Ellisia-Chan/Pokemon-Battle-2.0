import PokemonArray as pa

class GameManager:
    def __init__(self) -> None:
        self.pokemon_array = pa.GetPokemonArray()

        
    def GetPokemonInfo(self):
        return self.pokemon_array