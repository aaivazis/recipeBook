#! /usr/bin/env python3

# third party imports
from nautilus import ServiceManager
# local imports
from server import RecipeService

# create a manager wrapping the service
manager = ServiceManager(RecipeService)

if __name__ == '__main__':
    manager.run()
