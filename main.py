# Pokemon Import Definitions
from pokemonDatabase import *
from initTrainer import *
import battle


def main():
    """
    Main Method - INIT Pokemon Battle
    """
    globalTrainer = createTrainer()
    battle.fight(globalTrainer.pokemons[0], Charizard)


if __name__ == "__main__":
    main()
