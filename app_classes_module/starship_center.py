
# from app_classes_module.startship import StarShip
from .startship import StarShip

class StarShipCenter:
    def __init__(self, star_ships: list[StarShip]):
        self.star_ships = star_ships
