from char import NFT
from attrs import name, head, eyes, nose, mouth, hat, facial_hair, shell

import random

MEGA_DICT = {
    "name": name,
    "head": head, 
    "eyes": eyes,
    "nose": nose,
    "mouth": mouth,
    "hat": hat, 
    "facial_hair": facial_hair
}

def generate_random_number_dict(dict_name):
    random_number_dict = {}
    for key in dict_name:
        random_number_dict[key] = random.randint(1, 10)
    return random_number_dict


def assembler():
    filled = generate_random_number_dict(shell)
    assembled = filled.copy()
    for feature, value in filled.items():
        assembled[feature] = MEGA_DICT[feature][value]
    return assembled
    

def multiplier(int):
    for i in range(int):
        print(assembler())