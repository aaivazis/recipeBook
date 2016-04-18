# third party imports
from nautilus import ConnectionService

# import the services to connect
from recipeBook import IngredientService, RecipeService

class ServiceConfig:
    database_url = 'sqlite:///ingredientRecipe.db'

class IngredientRecipeService(ConnectionService):
    services=[IngredientService, RecipeService]
    configObject=ServiceConfig
