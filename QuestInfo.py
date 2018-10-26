class Quest:

    def __init__(self, name):
        self.name = name
        self.free = False
        self.age = None
        self.difficulty = None
        self.length = None
        self.quest_points = 0
        self.pre_quests = []
        self.post_quests = []
        self.children = []
        self.other_requirements = []

        self.agility = 0
        self.attack = 0
        self.constitution = 0
        self.construction = 0
        self.cooking = 0
        self.crafting = 0
        self.defence = 0
        self.divintation = 0
        self.dungeoneering = 0
        self.farming = 0
        self.firemaking = 0
        self.fishing = 0
        self.fletching = 0
        self.herblore = 0
        self.hunter = 0
        self.magic = 0
        self.mining = 0
        self.prayer = 0
        self.ranged = 0
        self.runecrafting = 0
        self.slayer = 0
        self.smithing = 0
        self.strength = 0
        self.summoning = 0
        self.thieving = 0
        self.woodcutting = 0

    def __str__(self):
        return "{}".format(self.name)

    def add_pre_quest(self, q):
        self.pre_quests.append(q)

    def add_post_quest(self, q):
        self.post_quests.append(q)
