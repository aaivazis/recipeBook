from graphene import Schema, ObjectType, String, Mutation, Boolean, Field, Int
from nautilus.api import ServiceObjectType, Connection
from nautilus.network import dispatch_action
from nautilus.conventions import get_crud_action
from recipe_book import RecipeService, IngredientService, IngredientRecipeService


class Recipe(ServiceObjectType):
    class Meta:
        service = RecipeService

    ingredients = Connection('Ingredient')


class Ingredient(ServiceObjectType):
    class Meta:
        service = IngredientService


class Query(ObjectType):
    ingredients = Connection(Ingredient)
    recipes = Connection(Recipe)


class AddRecipeMutation(Mutation):
    """
        This mutation fires an event to create a new recipe in the model service.
    """
    class Input:
        """
            This class defines the mutation arguments.
        """
        name = String()
        category = String()
        cook_time = Int()


    success = Boolean(description="Whether or not the dispatch was successful")

    @classmethod
    def mutate(cls, instance, args, info):
        """ perform the mutation """
        # send the new recipe action into the queue
        payload = dict(
            name=args['name'],
            category=args['category'],
            cook_time=args['cookTime'],
        )
        dispatch_action(
            action_type=get_crud_action('create', RecipeService.model),
            payload=payload
        )
        return AddRecipeMutation(success=True)


class AddIngredientMutation(Mutation):
    """
        This mutation fires an event to create a new recipe in the model service.
    """
    class Input:
        """
            This class defines the mutation arguments.
        """
        name = String()


    success = Boolean(description="Whether or not the dispatch was successful")

    @classmethod
    def mutate(cls, instance, args, info):
        """ perform the mutation """
        # send the new ingredient action into the queue
        payload = dict(
            name=args['name'],
        )
        dispatch_action(
            action_type=get_crud_action('create', IngredientService.model),
            payload=payload
        )
        return AddIngredientMutation(success=True)




class ApiMutations(ObjectType):
    """ the list of mutations that the api supports """
    addRecipe = Field(AddRecipeMutation)
    addIngredient = Field(AddIngredientMutation)


schema = Schema()
schema.query = Query
schema.mutation = ApiMutations
