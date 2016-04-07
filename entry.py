class Entry:
    def __init__(self, entry_id, name, category_id, entry_type, points, min_points, max_points, min_in_force, max_in_force,
                 min_in_rooster, max_in_rooster, min_selections, max_selections, collective, hidden,
                 entries, entry_groups, rules, profiles, links, book, page):
        self.entry_id = entry_id
        self.name = name
        self.category_id = category_id
        self.entry_type = entry_type
        self.points = points
        self.min_points = min_points
        self.max_points = max_points
        self.min_in_force = min_in_force
        self.max_in_force = max_in_force
        self.min_in_rooster = min_in_rooster
        self.max_in_rooster = max_in_rooster
        self.min_selections = min_selections
        self.max_selections = max_selections
        self.collective = collective
        self.hidden = hidden
        self.entries = entries
        self.entry_groups = entry_groups
        self.rules = rules
        self.profiles = profiles
        self.links = links
        self.book = book
        self.page = page

