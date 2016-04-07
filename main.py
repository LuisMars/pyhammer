import base64
import json

import zlib

import dice
from gear import CloseCombatWeapon, RangedWeapon
from infantry_profile import InfantryProfile
from link import Link
from rule import Rule
from rule_profile import RuleProfile
from stats import Stats
from troop import Troop
from squad import Squad
from vehicle_profile import VehicleProfile
from walker_profile import WalkerProfile
from weapon_profile import WeaponProfile


def main():
    base_stats = Stats(5, 4, 4, 4, 2, 4, 2, 10, 2, 5)

    troop = Troop('Grey Knight', 20, base_stats)

    sword = CloseCombatWeapon('Sword', 2, 0, 1, 3)

    troop.add_close_combat_weapon(sword)

    bolter = RangedWeapon('Bolter', 24, 'Assault', 1, 4, 4)
    troop.add_close_combat_weapon(bolter)

    squad = Squad('Strike Squad', 10)

    squad.add_troop(Troop('Captain', 30, Stats(5, 4, 5, 4, 2, 4, 2, 10, 2, 5)))

    for i in range(squad.limit - 1):
        squad.add_troop(troop)

    squads = [squad]
    print(squad)
    print(json.dumps({'Grey Knight': base_stats}, default=lambda o: o.__dict__, indent=4))

    # print(base64.b64encode(zlib.compress(bytes(json.dumps(squads, default=lambda o: o.__dict__), 'utf-8'), 9)))
    pass


def test_input():
    data_file = open('gk.json', encoding='utf-8')
    text = data_file.read().replace('\n', '')
    data = json.loads(text)
    for key in data.keys():
        catalogue = data[key]

    indent = 4
    content = {}

    for key in catalogue.keys():
        if catalogue[key].__class__ == dict:
            content[key] = catalogue[key]
    indent += 4

    shared_entries = {}
    shared_rules = {}
    data_entries = {}
    data_links = {}
    shared_entry_groups = {}
    shared_profiles = {}

    for key in content.keys():
        # print(' ' * indent, key)
        if key == 'sharedEntries':
            shared_entries = content[key]['entry']
        elif key == 'sharedRules':
            shared_rules = content[key]['rule']
        elif key == 'entries':
            data_entries = content[key]['entry']
        elif key == 'links':
            data_links = content[key]['link']
        elif key == 'sharedEntryGroups':
            shared_entry_groups = content[key]['entryGroup']
        elif key == 'sharedProfiles':
            shared_profiles = content[key]['profile']
    """
    for profile in shared_entries:
        print(' ' * (indent + 4), profile)
    for profile in shared_rules:
        print(' ' * (indent + 4), profile)
    for profile in entries:
        print(' ' * (indent + 4), profile)
    for profile in links:
        print(' ' * (indent + 4), profile)
    for profile in shared_entry_groups:
        print(' ' * (indent + 4), profile)
    """
    profiles = {}
    for profile in shared_profiles:
        extract_profile(profile, profiles)

    rules = {}
    for rule in shared_rules:
        extract_rule(rule, rules)

    links = {}

    for link in data_links:
        extract_link(link, links)

    entries = {}

    # for entry in data_entries:
    # TODO entries and gluing all together

    # print(json.dumps({'links': links}, default=lambda o: o.__dict__, indent=4))


def extract_link(link, links):
    l = Link(link.get('-id'), link.get('-linkType'), link.get('-targetId'), link.get('-categoryId'))
    links[l.link_id] = l


def extract_rule(rule, rules):
    r = Rule(rule.get('-id'), rule.get('-name'), rule.get('description'), rule.get('-hidden'), rule.get('-book'),
             rule.get('-page'))
    rules[r.rule_id] = r


def extract_profile(profile, profiles):
    characteristics = profile.get('characteristics').get('characteristic')
    if characteristics.__class__ == dict:
        characteristics = [characteristics]
    # Infantry
    if profile['-profileTypeId'] == '2d6001b0-980e-46d2-bcc2-a9fc60109afd':
        stats = {}
        for characteristic in characteristics:
            stats[characteristic['-name']] = characteristic['-value']

        p = InfantryProfile(profile['-name'], profile['-id'], profile['-hidden'], profile.get('-book'),
                            profile.get('-page'), stats)
        profiles[p.profile_id] = p
    # Rules
    elif profile['-profileTypeId'] == '72c5eafc-75bf-4ed9-b425-78009f1efe82':
        p = RuleProfile(profile['-name'], profile['-id'], profile['-hidden'], profile.get('-book'),
                        profile.get('-page'), profile['characteristics']['characteristic'].get('-value'))
        profiles[p.profile_id] = p
    # Vehicles
    elif profile['-profileTypeId'] == '725a358c-765b-498c-8de5-399fc0c0725f':
        stats = {}
        for characteristic in characteristics:
            stats[characteristic['-name']] = characteristic['-value']

        p = VehicleProfile(profile['-name'], profile['-id'], profile['-hidden'], profile.get('-book'),
                           profile.get('-page'), stats)
        profiles[p.profile_id] = p
    # Weapons
    elif profile['-profileTypeId'] == 'd5f97c0b-9fc9-478d-aa34-a7c414d3ea48':
        stats = {}
        for characteristic in characteristics:
            stats[characteristic['-name']] = characteristic['-value']

        p = WeaponProfile(profile['-name'], profile['-id'], profile['-hidden'], profile.get('-book'),
                          profile.get('-page'), stats)
        profiles[p.profile_id] = p
    # Walker
    elif profile['-profileTypeId'] == '3dadd2ff-33f1-41dd-85c7-bee5a7dfa413':
        stats = {}
        for characteristic in characteristics:
            stats[characteristic['-name']] = characteristic['-value']

        p = WalkerProfile(profile['-name'], profile['-id'], profile['-hidden'], profile.get('-book'),
                          profile.get('-page'), stats)
        profiles[p.profile_id] = p


if __name__ == '__main__':
    test_input()
