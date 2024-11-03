import pickle

def save_starship_to_file(star_ship, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(star_ship, file)
