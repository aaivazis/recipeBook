# third party imports
from nautilus import ModelService
from nautilus.models import BaseModel, fields

class Ingredient(BaseModel):
    name = fields.CharField()

class ServiceConfig:
    database_url = 'sqlite:///ingredients.db'

class IngredientService(ModelService):
    model = Ingredient
    config = ServiceConfig

