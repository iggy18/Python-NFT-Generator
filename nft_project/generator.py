import random

from nft import NFT
from lists import name, head, eyes, mouth, background

def generate_list(edition):
    ntf_list = []
    
    for i in range(1, edition+1):
        nft = NFT(
            name=random.choice(name),
            background=random.choice(background), 
            head=random.choice(head),
            eyes=random.choice(eyes),
            mouth=random.choice(mouth),
        )
        ntf_list.append(nft)
        
    return ntf_list
        
