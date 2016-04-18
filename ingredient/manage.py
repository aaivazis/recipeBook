#! /usr/bin/env python3

# third party imports
from nautilus import ServiceManager
# local imports
from server import IngredientService

# create a manager wrapping the service
manager = ServiceManager(IngredientService)

if __name__ == '__main__':
    manager.run()
