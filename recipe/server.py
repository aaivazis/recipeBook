# third party imports
from nautilus import ModelService
from nautilus.models import BaseModel, fields

class Recipe(BaseModel):
    name = fields.CharField()
    category = fields.CharField()
    cook_time = fields.IntegerField()

class ServiceConfig:
    database_url = 'sqlite:///recipe.db'

class RecipeService(ModelService):
    model = Recipe
    config = ServiceConfig
