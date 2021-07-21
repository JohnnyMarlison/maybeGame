from cls_stats import *


class AbstractCard:
    def __init__(self, name, classification, description, self_impact, other_impact, mana_cost):
        self.name = name
        self.classification = classification
        self.description = description
        self.self_impact = self_impact
        self.other_impact = other_impact
        self.mana_cost = mana_cost

    def getCardInfo(self):
        return self.name, self.classification, self.description, self.self_impact, self.other_impact, self.mana_cost

    def printCardInfo(self):
        print("\n",
              "===========================================\n",
              "NAME: {}".format(self.name), "\n",
              "TYPE: {}".format(self.classification), "\n",
              "DESCRIPTION : {}".format(self.description), "\n",
              "Impact for self: {}".format(self.self_impact), "\n",
              "Impact for other: {}".format(self.other_impact), "\n",
              "Mana cost: {}".format(self.mana_cost), "\n",
              "===========================================\n",
        )

    def getCardName(self):
        return self.name

    def getCardKind(self):
        return self.classification

    def getCardDescription(self):
        return self.description

    def getSelfImpact(self):
        return self.self_impact

    def getOtherImpact(self):
        return self.other_impact

    def set(self, stats):
        pass

    def get(self, stats):
        pass

    def cardAction(self):
        pass


class Generator:
    def get_value(self):
        pass


class WalkRick(AbstractCard):
    def process_func(self):
        pass


# Name, direction,
cards = [
    ["Lighting", "ACTION", "Сча как ебанет!", [0, 0, 0], [0, 0, -2], 1],
    ["Lighting", "ACTION", "Сча как ебанет! И по тебе тоже!", [0, 0, -1], [0, 0, -2], 2],
    ["Falling meteor", "ACTION", "Бог злится и бросается камнями...", [0, 0, 0], [0, 0, -4], 2],
    ["Falling meteor", "ACTION", "Усука по мне тоже попал...", [0, 0, -2], [0, 0, -4], 3],
    ["Shadow of Death", "ACTION", "Пиздец как воняет, умойся заебал.", [0, 0, 0], [0, 0, -6], 4],
    ["Orkish berserk", "ACTION", "Ебаный по голове", [0, 0, 0], [0, -5, -5], 2],
    ["FURY, bitch", "ACTION", "Не лезь дебилсукаебаный", [0, 0, 0], [0, -7, -7], 3],
    ["Warrior attack", "ACTION", "Как уеба сука", [0, 0, 0], [0, -9, -9], 4],
    ["Covert attack", "ACTION", "э ты че как крыса дерешься?", [0, 0, 0], [0, -11, -11], 5],
    ["Beast attack", "ACTION", "Я не зоофил, но твою свинячью жопу бы натянул", [0, 0, 0], [0, -13, -13], 6]
]

battle_deck = []
card = []
for i in range(len(cards)):
    for j in range(6):
        card = AbstractCard(cards[i][j], cards[i][j], cards[i][j], cards[i][j], cards[i][j], cards[i][j])


