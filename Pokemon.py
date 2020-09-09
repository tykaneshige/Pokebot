from PokeAPI import *

class Pokemon:

    # <poke_obj> is a PokeAPI object
    def __init__(self,poke_obj):

        self.num = poke_obj.num
        self.name = poke_obj.name

        self.level = poke_obj.level
        self.type = poke_obj.type
        self.item = poke_obj.item
        self.ability = poke_obj.ability
        self.moves = poke_obj.moves
        self.stats = poke_obj.stats

        self.evolve = (0,0)
        self.all_moves = poke_obj.all_moves

        self.nickname = ''

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
