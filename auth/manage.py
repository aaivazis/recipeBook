#! /usr/bin/env python3

# third party imports
from nautilus import ServiceManager
# local imports
from server import AuthService

# create a manager wrapping the service
manager = ServiceManager(AuthService)

if __name__ == '__main__':
    manager.run()