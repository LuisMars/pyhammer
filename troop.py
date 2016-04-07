from copy import deepcopy


def deepstr(l):
    res = ''
    elements = []

    for element in l:
        if element not in elements:
            elements.append(element)
            n = l.count(element)
            res += str(n) + 'x ' + str(element) + ', '

    return res[:-2]


class Troop:
    def __init__(self, name, cost, stats):
        self.name = name
        self.cost = cost
        self.stats = stats
        self.close_combat_weapons = []
        self.ranged_weapons = []

    def __str__(self):
        res = self.name + " (" + str(self.cost) + ')\n'
        if len(self.close_combat_weapons) != 0:
            res += deepstr(self.close_combat_weapons) + '\n'
        if len(self.ranged_weapons) != 0:
            res += deepstr(self.ranged_weapons) + '\n'
        res += str(self.stats)
        return res

    def __eq__(self, other):
        return self.name == other.name and self.cost == other.cost and self.stats == other.stats \
               and self.close_combat_weapons == other.close_combat_weapons \
               and self.ranged_weapons == other.ranged_weapons

    def add_close_combat_weapon(self, close_combat_weapon):
        self.close_combat_weapons.append(deepcopy(close_combat_weapon))

    def add_ranged_weapon(self, ranged_weapon):
        self.ranged_weapons.append(deepcopy(ranged_weapon))

    pass
