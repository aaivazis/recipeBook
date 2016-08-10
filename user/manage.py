#! /usr/bin/env python3

# third party imports
from nautilus import ServiceManager
# local imports
from server import UserService

# create a manager wrapping the service
manager = ServiceManager(UserService)

if __name__ == '__main__':
    manager.run()