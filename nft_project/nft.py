class NFT:
    
    def __init__(self, name, background, head, eyes, mouth):
        self.name = name
        self.background = background
        self.head = head
        self.eyes = eyes
        self.mouth = mouth
        self.rarity = None
        self.edition = None
        
    def __repr__(self):
        return f'name: {self.name} background: {self.background} head: {self.head} eyes: {self.eyes} mouth: {self.mouth}'