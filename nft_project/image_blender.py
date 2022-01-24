from email.mime import image
from typing import final
from PIL import Image

from generator import generate_list


def make_images(number_of_images):
    
    nfts_list = generate_list(number_of_images)
    edition = 1
    
    for nft in nfts_list:
        # collect all the images
        back = Image.open(nft.background)
        if back.mode != 'RGBA':
            back = back.convert('RGBA')
        head = Image.open(nft.head)
        eyes = Image.open(nft.eyes)
        mouth = Image.open(nft.mouth)
        
        #combine all the images
        stg1 = Image.alpha_composite(back, head)
        stg2 = Image.alpha_composite(stg1, eyes)
        final = Image.alpha_composite(stg2, mouth)
        
        #save the image as name and edition
        final.save(f'./nft_project/results/{nft.name}{edition}.png')
        
        edition += 1