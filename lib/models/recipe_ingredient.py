class RecipeIngredient:
    def __init__(self, recipe_id, ingredient_id, quantity, unit):
        self._recipe_id = recipe_id
        self._ingredient_id = ingredient_id
        self._quantity = quantity
        self._unit = unit

    @property
    def recipe_id(self):
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, value):
        self._recipe_id = value

    @property
    def ingredient_id(self):
        return self._ingredient_id

    @ingredient_id.setter
    def ingredient_id(self, value):
        self._ingredient_id = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    def __str__(self):
        return f"Recipe ID: {self._recipe_id}, Ingredient ID: {self._ingredient_id}, Quantity: {self._quantity} {self._unit}"

    def __repr__(self):
        return f"RecipeIngredient(recipe_id={self._recipe_id}, ingredient_id={self._ingredient_id}, quantity={self._quantity}, unit='{self._unit}')"
