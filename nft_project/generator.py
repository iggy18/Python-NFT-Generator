from enum import unique
import random

from nft import NFT
from config import pick_attribute_for

def all_nfts_are_unique(nft_list):
    seen = []
    return not any(nft in seen or seen.append(nft) for nft in nft_list)

def generate_list(edition):
    unique_nfts = []
    
    def generate_unique_nft():
            nft = NFT(
                name=pick_attribute_for('name'),
                background=pick_attribute_for('background'), 
                head=pick_attribute_for('head'),
                eyes=pick_attribute_for('eyes'),
                mouth=pick_attribute_for('mouth')
            )

            if nft in unique_nfts:
                print("duplicate nft found! re-generating...")
                return generate_unique_nft()

            return nft
        
    for i in range(1, edition+1):
        unique_nfts.append(generate_unique_nft())
    
    if all_nfts_are_unique(unique_nfts):
        print("############ all_nfts_are_unique ########################")

    for nft in unique_nfts:
        nft.add_edition()
        
    return unique_nfts
        
