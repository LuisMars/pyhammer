from profile import Profile


class RuleProfile(Profile):

    def __init__(self, name, profile_id, hidden, book, page, description):
        super().__init__(name, profile_id, hidden, book, page)
