from lib.recipes import Recipes

def test_recipes():
    recipes = Recipes(1, "Recipe1", 10, 1)
    assert recipes.id == 1
    assert recipes.name == "Recipe1"
    assert recipes.cooking_time == 10
    assert recipes.rating == 1


