class Move:
    def __init__(self, name, type, damage, accuracy):
        self.name = name
        self.type = type
        self.damage = damage
        self.accuracy = accuracy

    def __str__(self):
        return self.name + " (" + self.type + ")"
