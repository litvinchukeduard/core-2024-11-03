
# from 

from .startship import StarShip, STARSHIP_CODE
from .starship_center import StarShipCenter
from .user import User

with open('app_classes_module/hello.txt') as file:
    print(file.read())

__all__ = ['StarShip', 'StarShipCenter', 'User']
