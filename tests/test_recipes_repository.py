from lib.recipes_repository import RecipesRepository
from lib.recipes import Recipes

def test_all(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipesRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipes(1, "Toast", 5, 2),
        Recipes(2, "Ragou", 60, 4), 
        Recipes(3, "Pasta", 20, 3),
        Recipes(4, "Rice", 35, 5)
    ]

def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipesRepository(db_connection)
    recipe = repository.find(3)
    assert recipe == Recipes(3, "Pasta", 20, 3)