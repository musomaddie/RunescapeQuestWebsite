class QuestSeries:

    def __init__(self, name):
        self.name = name
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)
