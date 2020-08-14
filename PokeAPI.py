# Uses the PokeAPI to return stats of the pokemon queried.
import json
import random

from urllib.request import *

# The url to query
url = 'https://pokeapi.co/api/v2/pokemon/'

class PokeInfo:

	def __init__(self, num):

		self.json = self.make_request(num)

		self.num = num
		self.name = self.json['name']
		self.level = random.randint(1,100)
		self.type = self.get_types()
		self.ability = self.get_abilities()
		self.moves = self.get_moves()
		self.stats = self.get_stats()

		self.sprite = self.json['sprites']['front_default']

		'''
		self.evolve_lv = 0
		self.evolve_to = 0
		'''

	# Sends the get request to the API
	def make_request(self, num):
		
		# Create the url to search for
		query = url + '/' + num

		# Request info from the API
		req = Request(query)

		# headers - things that are sometimes required for API queries and idk what
		# exactly it's for though hahahaha sorry
		req.add_header('User-Agent', "pi")

		# Read the url response... tbh don't rememeber exactly how this works too
		response = urlopen(req)
		contents = response.read()
		text = contents.decode('utf8')

		# Returns ALL the data of the pokemon queried
		return json.loads(text)

	# Retrieves Pokemon Types
	def get_types(self):

		typelist = self.json['types']

		type0 = typelist[0]['type'].get('name')

		if len(typelist) > 1:
		    type1 = typelist[1]['type'].get("name")
		    return (type0, type1)
		else:
		    return (type0, None)

	# Retrieves Pokemon Abilities
	def get_abilities(self):

		ability_list = []
		hidden_ability = None

		abilities = self.json['abilities']
		a0 = abilities[0]['ability']['name']

		if abilities[0]['is_hidden']:
		    hidden_ability = a0
		else:
		    ability_list.append(a0)

		# Check for secondary abilities and hidden abilities
		indices = len(abilities)

		if indices > 1:
		    a1 = abilities[1]['ability']['name']

		    if abilities[1]['is_hidden']:
		        hidden_ability = a1
		    else:
		        ability_list.append(a1)

		if indices > 2:
		    a2 = abilities[2]['ability']['name']

		    if abilities[2]['is_hidden']:
		        hidden_ability = a2
		    else:
			    ability_list.append(a2)

		# Randomly return an ability
		random.seed(a=None)
		
		if random.randrange(0,50) < 2:
			return hidden_ability
		else:
			if len(ability_list) > 1:
				return ability_list[random.randrange(0,1)]
			else:
				return ability_list[0]

	# Retrieves Pokemon Moves
	# TODO: Figure an algorithm to produce a set of four moves based on level
	def get_moves(self):
		pass

		'''
		moves = self.json['moves']
		moves1 = moves[0]
		moves01 = moves1['move']
		move1 = moves01['name']
		print('Move 1: ' + move1)

		indices = len(moves)

		if indices > 1:
		    moves2 = moves[1]
		    moves02 = moves2['move']
		    move2 = moves02['name']
		    print('Move 2: ' + move2)

		if indices > 2:
		    moves3 = moves[2]
		    moves03 = moves3['move']
		    move3 = moves03['name']
		    print('Move 3: ' + move3)

		if indices > 3:
		    moves4 = moves[3]
		    moves04 = moves4['move']
		    move4 = moves04['name']
		    print('Move 4: ' + move4)
		'''

	# Retrieves Pokemon stats
	def get_stats(self):

		all_stats = {}

		stats = self.json['stats']

		# Atk
		base0 = stats[0]['base_stat']
		name0 = stats[0]['stat']['name']

		all_stats[name0] = {}
		all_stats[name0]['base'] = base0
		all_stats[name0]['stat'] = base0

		# Def
		base1 = stats[1]['base_stat']
		name1 = stats[1]['stat']['name']

		all_stats[name1] = {}
		all_stats[name1]['base'] = base1
		all_stats[name1]['stat'] = base1

		# Sp. Atk
		base2 = stats[2]['base_stat']
		name2 = stats[2]['stat']['name']

		all_stats[name2] = {}
		all_stats[name2]['base'] = base2
		all_stats[name2]['stat'] = base2

		# Sp. Def
		base3 = stats[3]['base_stat']
		name3 = stats[3]['stat']['name']

		all_stats[name3] = {}
		all_stats[name3]['base'] = base3
		all_stats[name3]['stat'] = base3

		# Speed
		base4 = stats[4]['base_stat']
		name4 = stats[4]['stat']['name']

		all_stats[name4] = {}
		all_stats[name4]['base'] = base4
		all_stats[name4]['stat'] = base4

		# Returns all Pokemon stats
		return all_stats

	def info_dump(self):
		print('ID: ' + self.num)
		print('Name: ' + self.name)
		
		if self.type[1] != None:
			print('Type: ' + self.type[0] + ' & ' + self.type[1])
		else:
			print('Type: ' + self.type[0])

		print('Ability: ' + self.ability)

		for key in self.stats:
			print(str(key) + ':')
			print('   Base Stat: ' + str(self.stats[key]['base']))
			print('   Real: ' + str(self.stats[key]['stat']))

if __name__ == '__main__':
	thing = input('Pokemon Name: ')
	test = PokeInfo(thing)
	test.info_dump()
