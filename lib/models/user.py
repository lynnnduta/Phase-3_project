class User:
    def __init__(self, id, username, email):
        self._id = id
        self._username = username
        self._email = email

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def __str__(self):
        return f"User ID: {self._id}, Username: {self._username}, Email: {self._email}"

    def __repr__(self):
        return f"User(id={self._id}, username='{self._username}', email='{self._email}')"
