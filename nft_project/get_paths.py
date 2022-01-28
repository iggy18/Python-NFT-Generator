import os

NFT_FOLDER = "nft_project/nft"

def get_attributes_from_nft_folder():
    nft_attributes = os.listdir(NFT_FOLDER)
    attribute_dict = dict.fromkeys(nft_attributes, "None")
    
    for attribute in nft_attributes:
        attribute_dict[attribute] = os.listdir(f'{NFT_FOLDER}/{attribute}/')

    return attribute_dict

def construct_path(attribute, image_name):
    return f'{NFT_FOLDER}/{attribute}/{image_name}'