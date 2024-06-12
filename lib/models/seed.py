from models.user import User
from models.recipe import Recipe
from models.recipe_ingredient import RecipeIngredient

User.create_table()
Recipe.create_table()
RecipeIngredient.create_table()

User.create("Alice", "alice@example.com")
User.create("Bob", "bob@example.com")

Recipe.create("Pancakes", "Mix flour, milk, eggs, and butter. Cook on a hot griddle.", 1)
Recipe.create("Scrambled Eggs", "Beat eggs, cook in a pan with butter.", 2)

RecipeIngredient.create(1, "Flour")
RecipeIngredient.create(1, "Milk")
RecipeIngredient.create(1, "Eggs")
RecipeIngredient.create(1, "Butter")
RecipeIngredient.create(2, "Eggs")
RecipeIngredient.create(2, "Butter")