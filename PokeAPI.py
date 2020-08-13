# Uses the PokeAPI to return stats of the pokemon queried.
import json
from urllib.request import *

class Pokemon:

	def __init__(self, name, num, type1, ability, move1, baseHP, baseAtk, baseDef, baseSPatk, baseSPdef, baseSpeed, sprite):
		self.p_name = name
		self.id = num
		self.type1 = type1
		self.ability = ability
		self.move1 = move1
		self.baseHP = baseHP
		self.baseAtk = baseAtk
		self.baseDef = baseDef
		self.baseSPatk = baseSPatk
		self.baseSPdef = baseSPdef
		self.baseSpeed = baseSpeed
		self.sprite = sprite

        # Optional Arguments
		#self.type2
		#self.evolve_lv = 
        #self.evolve_to = 
		#self.level = level
        #self.nickname = nickname

	def getName(self):
		return self.p_name

	def getID(self):
		return self.id

	def getAbility(self):
		return self.ability

	def getType(self):
		return self.type1

	def getMove1(self):
		return self.move1

	def getBaseHP(self):
		return self.baseHP

	def getBaseAtk(self):
		return self.baseAtk
	
	def getBaseDef(self):
		return self.baseDef
	
	def getBaseSPatk(self):
		return self.baseSPatk

	def getSPdef(self):
		return self.baseSPdef
	
	def getSpeed(self):
		return self.baseSpeed
	
	def getSprite(self):
		return self.sprite


# The url to query
url = 'https://pokeapi.co/api/v2/pokemon/'

# query stores the user's input which should be a pokemon name
query = input('Pokemon Name:')

# changes the input to lowercase letters
query = query.lower()

# add a '/' to the end of the query to complete the url
query = query + '/'

# debug check the url
print(url + query)

# create the url to search for
url = url + query

# request info from the API
req = Request(url)

# headers - things that are sometimes required for API queries and idk what
# exactly it's for though hahahaha sorry
req.add_header('User-Agent', "pi")

# read the url response... tbh don't rememeber exactly how this works too
response = urlopen(req)
contents = response.read()
text = contents.decode('utf8')

# data is ALL the data of the pokemon queried
data = json.loads(text)

# stores Pokemon name
name = data['name']
print('Pokemon: ' + name)

idNum = data['id']
print('ID: ' + str(idNum))

#store Pokemon type
typelist = data['types']
typedict0 = typelist[0]
typedict01 = typedict0["type"]
type0 = typedict01.get("name")

indices = len(typelist)

if indices > 1:
    typedict1 = typelist[1]
    typedict11 = typedict1["type"]
    type1 = typedict11.get("name")
    print('Type: ' + type0 + ", " + type1)
else:
    print('Type: ' + type0)

 
#stores Pokemon abilities
abilities = data['abilities']
abilities0 = abilities[0]
hidden0 =  abilities0["is_hidden"]
abilities01 = abilities0["ability"]
ability0 = abilities01["name"]

if hidden0 == True:
        print('Hidden Ability: ' + ability0)
else:
    print('Ability 1: ' + ability0)

indices = len(abilities)
 
if indices > 1:
    abilities1 = abilities[1]
    hidden1 =  abilities1["is_hidden"]
    abilities11 = abilities1["ability"]
    ability1 = abilities11["name"]

    if hidden1 == True:
        print('Hidden Ability: ' + ability1)
    else:
        print('Ability 2: ' + ability1)

if indices > 2:
    abilities2 = abilities[2]
    hidden2 =  abilities2["is_hidden"]
    abilities21 = abilities2["ability"]
    ability2 = abilities21["name"]

    if hidden2 == True:
        print('Hidden Ability: ' + ability2)
    else:
        print('Ability 3: ' + ability2)


#stores Pokemon moves
moves = data['moves']
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


#Pokemon stats
stats = data['stats']

stats0 = stats[0]
basestat0 = stats0['base_stat']
stat0 = stats0['stat']
name0 = stat0['name']
print (name0 + ":", basestat0)

stats1 = stats[1]
basestat1 = stats1['base_stat']
stat1 = stats1['stat']
name1 = stat1['name']
print (name1 + ":", basestat1)

stats2 = stats[2]
basestat2 = stats2['base_stat']
stat2 = stats2['stat']
name2 = stat2['name']
print (name2 + ":", basestat2 )

stats3 = stats[3]
basestat3 = stats3['base_stat']
stat3 = stats3['stat']
name3 = stat3['name']
print (name3 + ":", basestat3 )

stats4 = stats[4]
basestat4 = stats4['base_stat']
stat4 = stats4['stat']
name4 = stat4['name']
print (name4 + ":", basestat4 )

stats5 = stats[5]
basestat5 = stats5['base_stat']
stat5 = stats5['stat']
name5 = stat5['name']
print (name5 + ":", basestat5 )


#Pokemon image
sprites = data['sprites']
sprites1 = sprites['front_default']
print(sprites1)

Poke = Pokemon(name, idNum, type0, ability0, move1, basestat0, basestat1, basestat2, basestat3, basestat4, basestat5, sprites1)
