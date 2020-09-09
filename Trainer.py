from Pokemon import *

class Trainer:

    def __init__(self,name):

        self.name = name

        self.team = []
        self.pokemon = {}
        self.pokemon_order = []
        self.next_key = 0

        self.items = {}

    # Pokemon-related Functions

    # Adds the Pokemon to the trainer's collection 
    def catch_pokemon(self,pokemon):
        
        # Create a new Pokemon object
        new_pokemon = Pokemon(pokemon)

        # Add Pokemon to collection
        self.pokemon[self.next_key] = new_pokemon
        self.pokemon_order.append(self.next_key)
        self.next_key += 1

    def release_pokemon(self):
        pass

    # Lists all Pokemon owned by the trainer
    def list_pokemon(self):
        full_list = '(Name,Nickname,Level)\n'
        for key in self.pokemon_order:
            if not self.pokemon[key].nickname:
                format_string = '{},None,{}\n'.format(self.pokemon[key].name.capitalize(),self.pokemon[key].level)
            else:
                format_string = '{},{},{}\n'.format(self.pokemon[key].name.capitalize(),self.pokemon[key].nickname,self.pokemon[key].level)
            full_list += format_string
        return full_list

    # Auxiliary Functions

    # 1: Sort by number
    # 2: Sort by name (alphabetical)
    def sort_pokemon(self, method):
        pass