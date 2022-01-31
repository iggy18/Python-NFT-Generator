from collections import Counter

from nft import NFT
from config import pick_attribute_for
from writers import make_json, init_CSV, write_to_CSV, individual_json, json_metadata
from feedback import ALL_GOOD, DUPE


def all_nfts_are_unique(nft_list):
    seen = []
    return not any(nft in seen or seen.append(nft) for nft in nft_list)

def tally_traits(unique_nfts):
    trait_count = []
    for nft in unique_nfts:
        nft.add_edition()
        
        for trait in nft.report():
            trait_count.append(trait)
    
    rarity_dict = Counter(trait_count)    
    make_json(rarity_dict)
    
    return rarity_dict


def generate_list(edition):
    unique_nfts = []
    
    init_CSV()
    
    def generate_unique_nft():
        
            nft = NFT(
                name=pick_attribute_for('name'),
                background=pick_attribute_for('background'), 
                head=pick_attribute_for('head'),
                eyes=pick_attribute_for('eyes'),
                mouth=pick_attribute_for('mouth')
            )

            if nft in unique_nfts:
                print(DUPE)
                return generate_unique_nft()
            else:    
                return nft
        
    for i in range(1, edition+1):
        unique_nfts.append(generate_unique_nft())
    
    if all_nfts_are_unique(unique_nfts):
        print(ALL_GOOD)
    
    rarity_dict = tally_traits(unique_nfts)
    
    meta_data = []
    
    for nft in unique_nfts:
        nft.add_rarity_score(rarity_dict)
        
        csv_values = nft.report()
        csv_values.append(nft.edition)
        csv_values.append(nft.rarity)
        
        write_to_CSV(csv_values)
        
        meta_chunk = nft.to_dict()
        individual_json(meta_chunk)
        meta_data.append(meta_chunk)
    
    json_metadata(meta_data)
    
    return unique_nfts
        
