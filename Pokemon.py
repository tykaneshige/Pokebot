from pokeAPI import *

class Pokemon:

    def __init__(self, num):

        self.num = num
        self.name = 0

        self.level = 0
        self.type = 0
        self.item = 0
        self.ability = 0
        self.moves = {}

        self.evolve = (0,0)

        self.nickname = 0

    # Increases level by 1
    # Checks for new moves
    # Checks for evolution
    def level_up(self):
        pass

    # Evolves the pokemon to the next evolution
    # Trainer will be given the option to cancel evolution
    def evolve_pokemon(self):
        pass

    # Returns information on a given pokemon
    def pokedex_entry(self):
        pass
