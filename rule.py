class Rule:
    def __init__(self, rule_id, name, description, hidden, book, page):
        self.rule_id = rule_id
        self.name = name
        self.description = description
        self.hidden = hidden
        self.book = book
        self.page = page

    def __str__(self):
        return self.name