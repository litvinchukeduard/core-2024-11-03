from dataclasses import dataclass
from .user import User

STARSHIP_CODE = 123456789

@dataclass
class StarShip():
    """
    Class for storing information about Starships 
    """
    name: str
    power: int # 0-100
    max_capacity: int

