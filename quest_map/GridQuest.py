class GridQuest:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.required_for = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return "{} ({})".format(self.name, self.required_for)

    def for_db(self):
        return self.name

    def horizontal_difference(self, other):
        return other.position[0] - self.position[0]

    def vertical_difference(self, other):
        return other.position[1] - self.position[1]
