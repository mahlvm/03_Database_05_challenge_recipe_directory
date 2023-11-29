from lib.recipes import Recipes

class RecipesRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        list_recipes = []
        for row in rows:
            item = Recipes(row["id"], row["name"], row["cooking_time"], row["rating"])
            list_recipes.append(item)
        return list_recipes

    def find(self, recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_id])
        row = rows[0]
        return Recipes(row["id"], row["name"], row["cooking_time"], row["rating"])
