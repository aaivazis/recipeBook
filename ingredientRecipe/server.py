# third party imports
from nautilus import ConnectionService
# local imports
from recipeBook import IngredientService, RecipeService

class ServiceConfig:
    database_url = 'sqlite:///ingredientRecipe.db'

class IngredientRecipeService(ConnectionService):
    services=[IngredientService, RecipeService]
    config=ServiceConfig
