import os

NFT_FOLDER = "nft_project/nft"

def get_top_folders():
    return os.listdir(NFT_FOLDER)

def get_attributes_from_nft_folder():
    nft_attributes = get_top_folders()
    attribute_dict = dict.fromkeys(nft_attributes, "None")
    
    for attribute in nft_attributes:
        attribute_dict[attribute] = os.listdir(f'{NFT_FOLDER}/{attribute}/')

    return attribute_dict

def construct_path(attribute, image_name):
    return f'{NFT_FOLDER}/{attribute}/{image_name}'

def ensure_output_folders_exist():
    '''if these folders do not exsist create them'''
    if not os.path.exists('nft_project/results'):
        os.mkdir('nft_project/results')
        os.mkdir('nft_project/results/json')
        os.mkdir('nft_project/results/images')
        os.mkdir('nft_project/results/csv')

    if not os.path.exists('nft_project/results/json'):
        os.mkdir('nft_project/results/json')

    if not os.path.exists('nft_project/results/images'):
        os.mkdir('nft_project/results/images')

    if not os.path.exists('nft_project/results/csv'):
        os.mkdir('nft_project/results/csv')
        