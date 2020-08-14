class Trainer:

    def __init__(self, id, name):

        self.id = id
        self.name = name

        self.team = []
        self.pokemon = {}
        self.pokemon_order = []

        self.items = {}

    # Trainer-related functions

    def change_name(self, name):
        pass

    # Pokemon-related functions

    def catch_pokemon(self):
        pass

    def release_pokemon(self):
        pass

    def list_pokemon(self):
        pass

    # Auxiliary Functions

    # 1: Sort by number
    # 2: Sort by name (alphabetical)
    def sort_pokemon(self, method):

        