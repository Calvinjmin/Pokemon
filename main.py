# Import Definitions
import battle
from moves import Move
from pokemon import Pokemon


def main():
    """
    Main Method - INIT Pokemon Battle
    """

    # Creating Moves
    Flamethrower = Move("Flamethrower", "Fire", 100)
    Flame_Blast = Move("Flame Blast", "Fire", 150)
    Dragon_Claw = Move("Dragon Claw", "Dragon", 80)
    Dragon_Pulse = Move("Dragon Pulse", "Dragon", 150)
    Fly = Move("Fly", "Flying", 80)
    Hyper_Beam = Move("Hyper Beam", "Normal", 150)

    Charizard_Moveset = [Flamethrower, Flame_Blast, Fly, Hyper_Beam]
    Dragonite_Moveset = [Dragon_Claw, Dragon_Pulse, Fly, Hyper_Beam]

    # Creating Pokemon
    Charizard = Pokemon("Charizard", "Fire", Charizard_Moveset, 500, 50)
    Dragonite = Pokemon("Dragonite", "Dragon", Dragonite_Moveset, 400, 50)
    battle.fight(Charizard, Dragonite)


if __name__ == "__main__":
    main()
