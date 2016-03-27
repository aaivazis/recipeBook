# third party imports
from nautilus import ModelService
import nautilus.models as models


class Recipe(models.CRUDNotificationCreator, models.BaseModel):
    name = models.fields.CharField()
    category = models.fields.CharField()
    cook_time = models.fields.CharField()

class ServiceConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/recipe.db'


service = ModelService(
    configObject = ServiceConfig,
    model = Recipe,
)
