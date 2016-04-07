from profile import Profile


class WalkerProfile(Profile):
    def __init__(self, name, profile_id, hidden, book, page, stats):
        super().__init__(name, profile_id, hidden, book, page)
        self.stats = stats
