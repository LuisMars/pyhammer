def hit_roll(attacker, defender):
    if attacker > defender:
        return 4 / 6
    elif defender > attacker * 2:
        return 2 / 6
    else:
        return 3 / 6


def shoot_roll(bs):
    if bs > 5:
        return 5 / 6 + (1 / 6) * (bs - 5) / 6
    else:
        return bs / 6


def reroll(p):
    return p + ((1 - p) * p)


def reroll_one_of_n(p, n):
    return p + pow(p, n) * (1 - p)


def wound_roll(attacker, defender):
    if attacker == defender:
        return 3 / 6
    elif attacker == defender + 1:
        return 4 / 6
    elif attacker == defender - 1:
        return 2 / 6
    elif attacker > defender + 1:
        return 5 / 6
    elif attacker + 3 >= defender:
        return 1 / 6
    else:
        return 0


def pass_test(n):
    if n <= 1:
        return 0
    r = - 0.0031495 * pow(n, 4) - 0.004211 * pow(n, 3) + 0.903352 * pow(n, 2) - 2.364843 * n + 2
    return round(r) / 36


def save(ap, sv, ss):
    if ap <= sv:
        return armor_save(ap, sv)
    else:
        return special_save(ss)


def armor_save(ap, sv):
    if sv == 7 or ap <= sv:
        return 1
    else:
        return (sv - 1) / 6


def special_save(ss):
    return (ss - 1) / 6


def force(wounds, sv, w):
    if wounds != 0:
        return ((wounds - (1 / 6)) * sv) + ((1 - sv) * (w / 6))
    else:
        return wounds * sv


def rending(wounds, sv):
    return force(wounds, sv, 1)


def retreat_cc(wound_difference, l):
    if wound_difference > -0.5:
        return 1 - pass_test(l - wound_difference.ceil())
    else:
        return 0


def sweeping_advance(attacker, defender):
    return min(max(1 - ((6 - ((attacker + 3) - defender)) / 6)), 1)

