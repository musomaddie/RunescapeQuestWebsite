class GridQuest:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.required_for = []

    def __str__(self):
        return "{} ({})".format(self.name, self.required_for)

    def left_difference_to(self, other):
        return other.position[0] - self.position[0]

    def above(self, other):
        return self.position[1] > other.position[1]

    def below(self, other):
        return self.position[1] < other.position[1]

    def height_difference(self, other):
        return max(self.position[1] - other.position[1],
                   other.position[1] - self.position[1])
