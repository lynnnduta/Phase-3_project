from models.recipe import Recipe
from models.ingredient import Ingredient
from models.recipe_ingredient import RecipeIngredient
from models.user import User
from database.seed import create_tables
from database.models import get_db_connection

class RecipeManagerCLI:
    def display_menu(self):
        print("Recipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Add Ingredient")
        print("4. View Ingredients")
        print("5. Add User")
        print("6. View Users")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_recipe()
            elif choice == '2':
                self.view_recipes()
            elif choice == '3':
                self.add_ingredient()
            elif choice == '4':
                self.view_ingredients()
            elif choice == '5':
                self.add_user()
            elif choice == '6':
                self.view_users()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_recipe(self):
        name = input("Enter recipe name: ")
        instructions = input("Enter recipe instructions: ")
        recipe = Recipe(name, instructions)
        print("Recipe added successfully.")

    def view_recipes(self):
        print("Recipes:")
        # Fetch and display all recipes from the database

    def add_ingredient(self):
        name = input("Enter ingredient name: ")
        ingredient = Ingredient(name)
        print("Ingredient added successfully.")

    def view_ingredients(self):
        print("Ingredients:")
        # Fetch and display all ingredients from the database

    def add_user(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        user = User(username, email)
        print("User added successfully.")

    def view_users(self):
        print("Users:")
        # Fetch and display all users from the database

if __name__ == "__main__":
    app = RecipeManagerCLI()
    app.run()