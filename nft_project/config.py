import random

from lists import name as name_list
from get_paths import get_attributes_from_nft_folder, construct_path

ATTRIBUTES = get_attributes_from_nft_folder()

CSV_HEADERS = ["Name", "Background", "Head", "Eyes", "Mouth", "Edition", "Rarity"]

NUMBER_OF_DESIRED_IMAGES = 25

BASE_NAME = "ASMR skull #"

BASE_IMAGE_URL = "www.testing.com/"

def pick_attribute_for(attribute):
    weights_dict = {
        "name" : [10, 20, 10, 1, 14, 15, 10, 5, 30, 10],
        "background" : [20, 35, 5, 50, 10],
        "eyes" : [20, 10, 10, 1, 19, 40],
        "head" : [40, 10, 35, 20, 1],
        "mouth" : [.5, 35, 20, 15, 25]
    }

    choice = None

    if attribute == "name":
        choice = random.choices(name_list, weights=weights_dict[attribute], k=1)[0]
    else:
        choice = random.choices(ATTRIBUTES[attribute], weights=weights_dict[attribute], k=1)[0]

    if attribute != "name":
        return construct_path(attribute, choice)
    else:
        return choice 