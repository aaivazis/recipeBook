# third party imports
from nautilus import ModelService
import nautilus.models as models


class Ingredient(models.CRUDNotificationCreator, models.BaseModel):
    name = models.fields.CharField()

class ServiceConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/recipe.db'


service = ModelService(
    configObject = ServiceConfig,
    model = Ingredient,
)
