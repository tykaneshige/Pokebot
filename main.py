# System packages
import random
import time

# User defined packages
from pokedex import *
from pokemon import *
from trainer import *

class Game:

    def __init__(self):
        self.trainers = {}
        self.available_Pokemon = []

    # Function for spawning pokemon
    def spawn_pokemon(self):

        # Randomly select the next pokemon 
        next_Pokemon = random.randint(1,3)

        # Verify that two of the same pokemon will not spawn at the same time
        first_Pokemon = next_Pokemon
        while next_Pokemon in self.available_Pokemon:
            next_Pokemon += 1

            if next_Pokemon > HIGH_BOUND:
                next_Pokemon = 1

            if next_Pokemon == first_Pokemon:
                return

        # Add the pokemon to the list of available pokemon
        self.available_Pokemon.append(next_Pokemon)

        print('Who\'s that Pokemon?')
        print(Pokedex[next_Pokemon]['Image_url'])

    # See pokemon currently spawned in
    def show_pokemon(self):

        if len(self.available_Pokemon) != 0:
            print('Available Pokemon:')
            print('Who\'s that Pokemon?')

            num = 1
            for pokemon in available_Pokemon:
                print(str(num) + '. ' + Pokedex[pokemon]['Image_url'])
        else:
            print('There are no Pokemon to catch. :(')


    # Main game loop
    def run(self):

        # Functions for checking passed commands
        def is_show(command):
            if command == 'show' or command == 'Show':
                return True
            else:
                return False

        def is_exit(command):
            if command == 'exit' or command == 'Exit' or command == 'quit' or command == 'Quit':
                return True
            else:
                return False

        # Opening prompt from Professor Oak
        '''
        print('Hello there! Welcome to the world of Pokémon!')
        time.sleep(3)
        print('My name is Oak! People call me the Pokémon Prof!')
        time.sleep(3)
        print('This world is inhabited by creatures called Pokémon!')
        time.sleep(3)
        print('For some people, Pokémon are pets. Others use them for fights...')
        time.sleep(3)
        print('Your very own Pokémon adventure is about to unfold!')
        time.sleep(3)
        print('A world of dreams and adventures with Pokémon awaits! Let\'s go!')
        time.sleep(1)

        # Create a new trainer
        name = input('Now tell me, what is your name? ')

        while 1:

            confirm = input('Ah, so your name is ' + str(name) + '? (Y/n) ')

            if confirm == 'Y' or confirm == 'y' or confirm == 'Yes' or confirm == 'yes':
                break;

            name = input('Ah. So what is your name? ')

        new_trainer = Trainer(name)
        self.trainers[name] = new_trainer

        print('Very good ' + str(name) + '!')
        print('It\'s time for you to dive into the world of Pokemon!')
        '''

        # Main loop of the game
        while 1:

            # Spawn pokemon after 10 inputs
            spawn_clock = 0
            while spawn_clock != 10:

                # Recieve and parse input from the user
                command = input()
                command_parse = command.split()

                # Check for a valid command
                if command_parse[0] == '!poke':

                    # Check for the 'available' command
                    if len(command_parse) == 2 and is_show(command_parse[1]):
                        self.show_pokemon()

                    # Check for the 'exit' command
                    elif len(command_parse) == 2 and is_exit(command_parse[1]):
                        return

                # Prevent empty commands from incrementing the counter
                elif command != '':
                    spawn_clock += 1

            self.spawn_pokemon()

game = Game()
game.run()