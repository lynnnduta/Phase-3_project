from database import CURSOR

class Recipe:
    @staticmethod
    def create(name, instructions, user_id):
        CURSOR.execute("INSERT INTO recipes (name, instructions, user_id) VALUES (?, ?, ?)", (name, instructions, user_id))
        return CURSOR.lastrowid

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM recipes")
        return CURSOR.fetchall()

    @staticmethod
    def delete(recipe_id):
        CURSOR.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))