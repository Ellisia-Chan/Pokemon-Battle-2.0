import packages
packages.InitializePackages()

import GameManager as GM
import Display as DP


class Gameplay(GM.GameManager, DP.Display):
    def __init__(self) -> None:

        super().__init__()
        self.DisplayPokemonSelection(self.GetPokemonInfo())
        


if __name__ == "__main__":  
    Gameplay()