class Ingredient:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"Ingredient ID: {self._id}, Name: {self._name}"

    def __repr__(self):
        return f"Ingredient(id={self._id}, name='{self._name}')"