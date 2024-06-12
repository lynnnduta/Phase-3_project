from database import CURSOR

class User:
    @staticmethod
    def create(username, email):
        CURSOR.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
        return CURSOR.lastrowid

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM users")
        return CURSOR.fetchall()

    @staticmethod
    def delete(user_id):
        CURSOR.execute("DELETE FROM users WHERE id = ?", (user_id,))