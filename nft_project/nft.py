from itertools import count

class NFT:
    
    new_edition = count()
    
    def __init__(self, name, background, head, eyes, mouth):
        self.name = name
        self.background = background
        self.head = head
        self.eyes = eyes
        self.mouth = mouth
        self.rarity = None
        self.edition = 1
        
    def __eq__(self, other):
        return self.background == other.background and self.eyes == other.eyes and self.head == other.head and self.mouth == other.mouth
            
        
    def __repr__(self):
        return f'name: {self.name} background: {self.background} head: {self.head} eyes: {self.eyes} mouth: {self.mouth} edition: {self.edition}'
    
    def add_edition(self):
        self.edition = next(self.new_edition)