class Move:
    def __init__(self, name, type, damage) -> None:
        self.name = name
        self.type = type
        self.damage = damage

    def __str__(self):
        return self.name + " (" + self.type + ")"
