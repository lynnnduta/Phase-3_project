from database import CURSOR

class RecipeIngredient:
    @staticmethod
    def create(recipe_id, ingredient_id):
        CURSOR.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (?, ?)", (recipe_id, ingredient_id))
        return CURSOR.lastrowid

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM recipe_ingredients")
        return CURSOR.fetchall()

    @staticmethod
    def delete(recipe_ingredient_id):
        CURSOR.execute("DELETE FROM recipe_ingredients WHERE id = ?", (recipe_ingredient_id,))