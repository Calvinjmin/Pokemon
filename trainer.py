class Trainer:
    def __init__(self, name, pokemons, money):
        self.name = name
        self.pokemons = pokemons
        self.money = money

    def __str__(self):
        if self.pokemons is None or len(self.pokemons) == 0:
            return self.name + " with no Pokemon!"
        else:
            return str(self.name) + " has a few pokemon!"