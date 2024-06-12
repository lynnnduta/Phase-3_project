from database import CURSOR

class Ingredient:
    @staticmethod
    def create(name):
        CURSOR.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
        return CURSOR.lastrowid

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM ingredients")
        return CURSOR.fetchall()

    @staticmethod
    def delete(ingredient_id):
        CURSOR.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))