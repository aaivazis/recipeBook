# third party imports
import nautilus
from nautilus.models import BaseModel, fields

class User(BaseModel):
    email = fields.CharField()

class ServiceConfig:
    database_url = 'sqlite:///user.db'

class UserService(nautilus.ModelService):
    model = User
    config = ServiceConfig