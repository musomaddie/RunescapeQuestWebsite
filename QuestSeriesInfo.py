class QuestSeries:

    def __init__(self, name):
        self.name = name
        self.quests = []
        self.related_quests = []

    def add_quest(self, quest, n):
        self.quests.append((quest, n))

    def add_related_quest(self, quest):
        self.related_quests.append(quest)
