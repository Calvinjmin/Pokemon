from trainer import Trainer
from pokedex import pokedex
from functions import delay_print

trainer = Trainer


def createTrainer():
    delay_print("Hello, welcome to the world of Pokemon!\n")
    delay_print("Please tell me your name: ")
    name = input("")

    global trainer
    trainer = Trainer(name, [], 0)

    delay_print("Please choose a pokemon!\n")
    index = 1
    for pokemon in pokedex:
        print(str(index) + ":", pokemon)
        index += 1
    pokemonIndexInput = int(
        input("Enter a number from 1-" + str(len(pokedex)) + ": "))
    if pokemonIndexInput < 1 or pokemonIndexInput > len(pokedex):
        print("Invalid Pokemon!")
    else:
        firstPokemon = pokedex[pokemonIndexInput - 1]
        trainer.pokemons.append(firstPokemon)

    return trainer