from app.app_classes_module import *
from functions.saving_functions import save_starship_to_file

from colorama import Fore

def return_hello(name: str) -> str:
    """
    A function that receives a name and returns "Hello, {name}"

    Args:
        - name (str): name os a user
    """
    return f"Hello, {name}!"

# Hello from another branch



def entry_point():
    starship = StarShip("Starship One", 50, 100)
    print(starship)
    print("Hello")
    while True:
        user_input = input("Enter command: ").strip()
        if user_input == 'hello':
            print("Hello")
        elif user_input == 'exit':
            print("Goodbye")
            save_starship_to_file(starship, 'starship.pkl')
            break

if __name__ == '__main__':
    entry_point()