class Quest:

    def __init__(self, name, is_free, age, difficulty, length, skills):
        self.name = name
        self.is_free = is_free
        self.age = age
        self.difficulty = difficulty
        self.length = length
        self.pre_quests = []

        self.agility = 0
        if "Agility" in skills:
            self.agility = skills["Agility"]
        self.attack = 0
        if "Attack" in skills:
            self.attack = skills["Attack"]
        self.constitution = 0
        if "Constitution" in skills:
            self.constitution = skills["Constitution"]
        self.construction = 0
        if "Construction" in skills:
            self.construction = skills["Construction"]
        self.cooking = 0
        if "Cooking" in skills:
            self.cooking = skills["Cooking"]
        self.crafting = 0
        if "Crafting" in skills:
            self.crafting = skills["Crafting"]
        self.defence = 0
        if "Defence" in skills:
            self.defence = skills["Defence"]
        self.divination = 0
        if "Divination" in skills:
            self.divination = skills["Divination"]
        self.dungeoneering = 0
        if "Dungeoneering" in skills:
            self.dungeoneering = skills["Dungeoneering"]
        self.farming = 0
        if "Farming" in skills:
            self.farming = skills["Farming"]
        self.firemaking = 0
        if "Firemaking" in skills:
            self.firemaking = skills["Firemaking"]
        self.fishing = 0
        if "Fishing" in skills:
            self.fishing = skills["Fishing"]
        self.fletching = 0
        if "Fletching" in skills:
            self.fletching = skills["Fletching"]
        self.herblore = 0
        if "Herblore" in skills:
            self.herblore = skills["Herblore"]
        self.hunter = 0
        if "Hunter" in skills:
            self.hunter = skills["Hunter"]
        self.magic = 0
        if "Magic" in skills:
            self.magic = skills["Magic"]
        self.mining = 0
        if "Mining" in skills:
            self.mining = skills["Mining"]
        self.prayer = 0
        if "Prayer" in skills:
            self.prayer = skills["Prayer"]
        self.ranged = 0
        if "Ranged" in skills:
            self.ranged = skills["Ranged"]
        self.runecrafting = 0
        if "Runecrafting" in skills:
            self.runecrafting = skills["Runecrafting"]
        self.slayer = 0
        if "Slayer" in skills:
            self.slayer = skills["Slayer"]
        self.smithing = 0
        if "Smithing" in skills:
            self.smithing = skills["Smithing"]
        self.strength = 0
        if "Strength" in skills:
            self.strength = skills["Strength"]
        self.summoning = 0
        if "Summoning" in skills:
            self.summoning = skills["Summoning"]
        self.thieving = 0
        if "Thieving" in skills:
            self.thieving = skills["Thieving"]
        self.woodcutting = 0
        if "Woodcutting" in skills:
            self.woodcutting = skills["Woodcutting"]

    def __str__(self):
        return "{}".format(self.name)

    def add_pre_quest(self, q):
        self.pre_quests.append(q)

    def add_post_quest(self, q):
        self.post_quests.append(q)
