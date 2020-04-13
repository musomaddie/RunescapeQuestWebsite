class GridCell:
    """
     Location stores the coordinates. For each even x number the corresponding
       y number is located slightly below (as hexagons)
             ,----,         .----.
            /      \       /      \
           /   00   \_____/   20   \
           \        /     \        /
            \      /       \      /
             )----(   10    )----(
            /      \       /      \
           /   01   \_____/  21    \
           \        /     \        /
            \      /  11   \      /
             `----(         )----'
                   \       /
                    \_____/

    List <int> entry points: the entry points that are being used stored as
        numbers (numbered top to bottom)
             0----,
            /1     \
         2 /        \
           \        /
            \ 3    /
             4----'

    List <int> exit points:  the exit points being used stored as numbers
        (numbered top to bottom)
             .----0
            /      \ 1
           /        \ 2
           \        /
            \      / 3
             `----4
    GridQuest quest: the quest stored inside the cell
    Lines: the number of lines as they pass through the cell (corresponds
        correctly to neighbouring cells). Only three as we will only store
        lines as they pass through the top of the cell (lines passing through
        bottom will be counted by cell below)
            (ordered clockwise from top).
                0
             .----,
            /      \ 1
           /        \
           \        /
            \      / 2
             `----'

    """

    def __init__(self, location):
        # This init will create the blank data -> will be populated later!
        self.location = location
        self.entry_points = [False for i in range(5)]
        self.exit_points = [False for i in range(5)]
        self.lines = [False for i in range(6)]
        self.quest = None

    def add_entry_point(self, point):
        self.entry_points[point] = True

    def add_exit_point(self, point):
        self.exit_points[point] = True

    def add_line(self, edge):
        self.lines[edge] = True

    def add_quest(self, quest):
        self.quest = quest

    def __str__(self):
        return "{}: ({}, {})".format(self.quest, self.location[0], self.location[1])
