# Pokemon Import Definitions
# import battle
from pokemonDatabase import *
import battle

# GUI Imports
from customWindow import *


def main():
    """
    Main Method - INIT Pokemon Battle
    """

    battle.fight(Lapras, Charizard)

    # GUI Code - Implement in the future
    # myWindow = CustomWindow()
    # myWindow.start()


if __name__ == "__main__":
    main()
