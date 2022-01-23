import random
from timer import speed

from attrs import MEGA_DICT, shell


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
    

@speed
def multiplier(int):
    for i in range(int):
        x = assembler()
