# Import Definitions
import sys
import time
from random import randint
from typeEffective import *


def delay_print(string):
    """"
    Function that delays system printing
    """
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.025)


def fight(pokemon1, pokemon2):
    """
    Function that conducts a turn-based battle between two pokemon
    Pokemon1 - User Pokemon
    Pokemon2 - Opposing Pokemon
    """

    # Initial Prints for Pokemon Battle
    print("----- Pokemon Battle -----")
    print(pokemon1.name + " vs. " + pokemon2.name)
    print(f"You chose {pokemon1.name}")

    # Turn-Based Pokemon Fight
    while pokemon1.health > 0 and pokemon2.health > 0:
        delay_print("\nCurrent Battle Status")
        delay_print(
            f"\n{pokemon1.name} lvl. {pokemon1.level}\t{pokemon1.health} hp")
        delay_print(
            f"\n{pokemon2.name} lvl. {pokemon2.level}\t{pokemon2.health} hp")

        # Pokemon 1's Turn
        print("\n\n---Move Set---")
        for i, move in enumerate(pokemon1.move_set):
            print(f"{i + 1}. ", move)

        while True:
            try:
                moveInput = input("Pick a move (number): ")
                if moveInput == "quit" or moveInput == "q()":
                    return
                moveIndex = int(moveInput)
                if moveIndex < 0 or moveIndex > 4:
                    print("Invalid Move. Try Again.")
                else:
                    break
            except:
                print("Invalid Input, Try Again.")

        # Calculate Damage to Pokemon 2
        randomHitCalc = randint(0, 100)
        if randomHitCalc <= pokemon1.move_set[moveIndex - 1].accuracy:
            # Super Effective
            if pokemon2.type in effectiveness[pokemon1.move_set[moveIndex -
                                                                1].type]:
                delay_print(
                    f"\n{pokemon1.name} used {pokemon1.move_set[moveIndex - 1]}. It's super effective!"
                )
                delay_print(
                    f"\n{pokemon1.name} dealt {int(2 * pokemon1.move_set[moveIndex - 1].damage)} to {pokemon2.name}"
                )
                pokemon2.health -= int(2 *
                                       pokemon1.move_set[moveIndex - 1].damage)
            # Not Very Effective
            elif pokemon2.type in not_effective[pokemon1.move_set[moveIndex -
                                                                  1].type]:
                delay_print(
                    f"\n{pokemon1.name} used {pokemon1.move_set[moveIndex - 1]}. Not very effective..."
                )
                delay_print(
                    f"\n{pokemon1.name} dealt {int(0.5 * pokemon1.move_set[moveIndex - 1].damage)} to {pokemon2.name}"
                )
                pokemon2.health -= int(0.5 *
                                       pokemon1.move_set[moveIndex - 1].damage)
            # No Effect
            elif pokemon2.type in effectiveness[pokemon1.move_set[moveIndex -
                                                                  1].type]:
                delay_print(
                    f"\n{pokemon1.name} used {pokemon1.move_set[moveIndex - 1]}. No effect."
                )
                delay_print(f"\n{pokemon1.name} dealt 0 to {pokemon2.name}")
            else:
                delay_print(
                    f"\n{pokemon1.name} used {pokemon1.move_set[moveIndex - 1]}"
                )
                delay_print(
                    f"\n{pokemon1.name} dealt {pokemon1.move_set[moveIndex - 1].damage} to {pokemon2.name}"
                )
                pokemon2.health -= int(pokemon1.move_set[moveIndex - 1].damage)
        else:
            delay_print(f"\n{pokemon1.name}'s attack missed")

        if pokemon2.health <= 0:
            print(f"\n\n{pokemon2.name} fainted.")
            print(f"{pokemon1.name} won the fight.")
            return

        # --- Pokemon 2's Turn ---
        randomMoveIndex = randint(0, 3)
        randomHitCalc = randint(0, 100)
        if randomHitCalc <= pokemon2.move_set[randomMoveIndex].accuracy:
            # Pokemon 2's Attack Hit
            # Super Effective
            if pokemon1.type in effectiveness[pokemon2.move_set[randomMoveIndex
                                                                - 1].type]:
                delay_print(
                    f"\n{pokemon2.name} used {pokemon2.move_set[randomMoveIndex - 1]}. It's super effective!"
                )
                delay_print(
                    f"\n{pokemon2.name} dealt {int(2 * pokemon2.move_set[randomMoveIndex - 1].damage)} to {pokemon1.name}"
                )
                pokemon2.health -= int(2 *
                                       pokemon1.move_set[moveIndex - 1].damage)
            # Not Very Effective
            elif pokemon1.type in not_effective[pokemon2.move_set[
                    randomMoveIndex - 1].type]:
                delay_print(
                    f"\n{pokemon2.name} used {pokemon2.move_set[randomMoveIndex - 1]}. Not very effective..."
                )
                delay_print(
                    f"\n{pokemon2.name} dealt {int(0.5 * pokemon2.move_set[randomMoveIndex - 1].damage)} to {pokemon1.name}"
                )
                pokemon2.health -= int(0.5 *
                                       pokemon1.move_set[moveIndex - 1].damage)
            # No Effect
            elif pokemon1.type in effectiveness[pokemon2.move_set[
                    randomMoveIndex - 1].type]:
                delay_print(
                    f"\n{pokemon2.name} used {pokemon2.move_set[randomMoveIndex - 1]}. No Effect."
                )
                delay_print(f"\n{pokemon2.name} dealt 0 to {pokemon1.name}")
            else:
                delay_print(
                    f"\n{pokemon2.name} used {pokemon2.move_set[randomMoveIndex]}"
                )

                # Calculate Damage to Pokemon 1
                delay_print(
                    f"\n{pokemon2.name} dealt {pokemon2.move_set[randomMoveIndex].damage} to {pokemon1.name}\n"
                )
                pokemon1.health -= int(
                    pokemon2.move_set[randomMoveIndex].damage)
        else:
            delay_print(f"\n{pokemon2.name}'s attack missed")

        if pokemon1.health <= 0:
            print(f"\n\n{pokemon1.name} fainted.")
            print(f"{pokemon2.name} won the fight.")
            return
