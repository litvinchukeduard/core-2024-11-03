from app_classes_module import *

from colorama import Fore

def return_hello(name: str) -> str:
    """
    A function that receives a name and returns "Hello, {name}"

    Args:
        - name (str): name os a user
    """
    return f"Hello, {name}!"

starship = StarShip("Starship One", 50, 100)
print(starship)
