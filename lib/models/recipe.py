class Recipe:
    def __init__(self, id, name, instructions):
        self._id = id
        self._name = name
        self._instructions = instructions

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

    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, value):
        self._instructions = value

    def __str__(self):
        return f"Recipe ID: {self._id}, Name: {self._name}, Instructions: {self._instructions}"

    def __repr__(self):
        return f"Recipe(id={self._id}, name='{self._name}', instructions='{self._instructions}')"
