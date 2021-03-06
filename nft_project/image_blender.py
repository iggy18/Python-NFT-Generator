from image_functions import cleaned, stack_images
from generator import generate_list
from feedback import DONE



def make_images(number_of_images):
    
    nfts_list = generate_list(number_of_images)
    
    for nft in nfts_list:
        #collect all the images
        back = cleaned(nft.background)
        head = cleaned(nft.head)
        eyes = cleaned(nft.eyes)
        mouth = cleaned(nft.mouth)
        
        #combine all the images
        stg1 = stack_images(back, head)
        stg2 = stack_images(stg1, eyes)
        final = stack_images(stg2, mouth)
        
        #save the image as name and edition
        final.save(f'./nft_project/results/images/{nft.name}_{nft.edition}.png')
        print(f'created image {nft.name}_{nft.edition}.png')
        
    print(DONE)