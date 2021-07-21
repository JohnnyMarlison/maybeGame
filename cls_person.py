from cls_stats import *


class AbstractPerson:
    def __init__(self, name, stats, e_point):
        self.name = name
        self.stats = stats
        self.e_point = e_point
        self.table_cards = None
        self.epoint_place = False
        # self.role = role

    def printInfo(self):
        print("\n",
              "===========================================\n",
              "PLAYER NAME: {}".format(self.name), "\n",
              "STATS: Attack - {}, Defense - {}, Health - {}".format(self.stats[0], self.stats[1], self.stats[2]), "\n",
              "E-POINT: {}".format(self.e_point), "\n",
              "==========================================="
              )

    def set(self):
        pass

    def get(self):
        pass


# Name, Stats, E-Point, cards
players = [
    ["Алкограммистер", [3, 6, 20], 0],
    ["Крысиный король", [3, 5, 22], 0]
]
