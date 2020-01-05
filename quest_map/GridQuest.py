class GridQuest:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.required_for = []

    def __str__(self):
        return "{} ({})".format(self.name, self.required_for)
