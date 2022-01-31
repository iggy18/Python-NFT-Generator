from config import BASE_IMAGE_URL, NUMBER_OF_DESIRED_IMAGES
from itertools import count

class NFT:
    
    new_edition = count()
    
    def __init__(self, name, background, head, eyes, mouth):
        self.name = name
        self.background = background
        self.head = head
        self.eyes = eyes
        self.mouth = mouth
        self.rarity = 0
        self.edition = 1
        
    def __eq__(self, other):
        return self.background == other.background and self.eyes == other.eyes and self.head == other.head and self.mouth == other.mouth
            
        
    def __repr__(self):
        return f'name: {self.name} background: {self.background} head: {self.head} eyes: {self.eyes} mouth: {self.mouth} edition: {self.edition}'
    
    def add_edition(self):
        self.edition = next(self.new_edition)
        
    def trait_value(self, input):
        specific = input.split('/')[-1]
        return specific
    
    def trait_type(self, input):
        specific = input.split('/')[-2]
        return specific
        
    def report(self): 
        Attribute_report = [ 
            self.name,
            self.trait_value(self.background).split('.')[0], 
            self.trait_value(self.head).split('.')[0], 
            self.trait_value(self.eyes).split('.')[0], 
            self.trait_value(self.mouth).split('.')[0]
        ]
        
        return Attribute_report
    
    def add_rarity_score(self, rarity_dict):
        total = 0
        keys = [
            self.name,
            self.trait_value(self.background),
            self.trait_value(self.head),
            self.trait_value(self.eyes),
            self.trait_value(self.mouth),
        ]
        
        for key in keys:
            total += rarity_dict[key]
        
        self.rarity = total/NUMBER_OF_DESIRED_IMAGES * 100
        
    def to_dict(self):
        nft = {
            "name": self.name + "_" + str(self.edition),
            "image": BASE_IMAGE_URL + self.name + "_" + str(self.edition),
            "description" : "the result of an ASMR NFT maker tutorial... of all things.",
            "edition": str(self.edition),
            "attributes": [
                { "trait_type": self.trait_type(self.background)   , "value" : self.trait_value(self.background).split('.')[0] },
                { "trait_type": self.trait_type(self.head)         , "value" : self.trait_value(self.head).split('.')[0] },
                { "trait_type": self.trait_type(self.eyes)         , "value" : self.trait_value(self.eyes).split('.')[0] },
                { "trait_type": self.trait_type(self.mouth)        , "value" : self.trait_value(self.mouth).split('.')[0] },
                { "display_type": "number", "trait_type": "rarity" , "value" : str(self.rarity) },
            ]
        }
        
        return nft