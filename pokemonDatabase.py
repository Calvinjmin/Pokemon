from moveDatabase import *
from pokemon import Pokemon

# Movesets
Charizard_Moveset = [Flamethrower, Flame_Blast, Fly, Hyper_Beam]
Dragonite_Moveset = [Dragon_Claw, Dragon_Pulse, Fly, Hyper_Beam]

# Creating Pokemon
Charizard = Pokemon("Charizard", "Fire", Charizard_Moveset, 500, 50)
Dragonite = Pokemon("Dragonite", "Dragon", Dragonite_Moveset, 400, 50)
