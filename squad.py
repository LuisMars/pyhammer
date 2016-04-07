from copy import deepcopy


class Squad:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.troops = []

    def __str__(self):
        res = self.name + ' (' + str(self.get_cost()) + ')\n'
        same_troops = []
        for troop in self.troops:
            if troop not in same_troops:
                n = self.troops.count(troop)
                same_troops.append(troop)

                res += str(n) + 'x ' + str(troop)

        return res

    def add_troop(self, troop):
        if len(self.troops) < self.limit:
            self.troops.append(deepcopy(troop))

    def get_cost(self):
        cost = 0

        for troop in self.troops:
            cost += troop.cost

        return cost

    pass
