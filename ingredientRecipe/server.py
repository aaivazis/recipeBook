# third party imports
from nautilus import ConnectionService
# local imports
from recipe_book import IngredientService, RecipeService

class ServiceConfig:
    database_url = 'sqlite:///ingredientRecipe.db'

class Ingredients(ConnectionService):
    config=ServiceConfig

    from_service = ('Recipe')
    to_service = ('Ingredient')
