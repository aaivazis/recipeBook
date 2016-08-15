# external imports
import nautilus

# create a nautilus service with just the schema
class RecipeBookAPI(nautilus.APIGateway):

    @nautilus.auth_criteria('recipe')
    async def auth_recipe(self, model, user_id):
        # only recipes with id 2 are visible
        return await model._has_id(2)
