
class Session:
    user_id = None
    username = None

    @classmethod
    def set(cls, user_id, username):
        cls.user_id = user_id
        cls.username = username

