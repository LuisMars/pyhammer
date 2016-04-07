class Profile:
    def __init__(self, name, profile_id, hidden, book, page):
        self.name = name
        self.profile_id = profile_id
        self.hidden = hidden
        self.book = book
        self.page = page

    def __str__(self):
        return self.name
    pass
