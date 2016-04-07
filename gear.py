class CloseCombatWeapon:
    def __init__(self, name, s, i, a, ap):
        self.name = name
        self.s = s
        self.i = i
        self.a = a
        self.ap = ap

    def __eq__(self, other):
        return self.name == other.name and self.s == other.s and self.i == self.i and self.a == other.a

    def __str__(self):
        return self.name


class RangedWeapon:
    def __init__(self, name, distance, weapon_type, shots, s, ap):
        self.name = name
        self.shots = shots
        self.weapon_type = weapon_type
        self.distance = distance
        self.ap = ap
        self.s = s

    def __eq__(self, other):
        return self.name == other.name and self.shots == other.shots and self.weapon_type == other.weapon_type \
               and self.distance == other.distance and self.ap == other.ap and self.s == other.s

    def __str__(self):
        return self.name
