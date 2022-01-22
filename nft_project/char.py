class NFT:
    
    def __init__(self, name, head, eyes, mouth, nose, hat, facial_hair):
        self.name = name
        self.head = head
        self.eyes = eyes
        self.mouth = mouth
        self.nose = nose
        self.hat = hat
        self.facial_hair = facial_hair
        
    def __repr__(self):
        return f"{self.name} has a {self.head} head, {self.eyes} eyes, {self.mouth} mouth, {self.nose} nose, {self.hat} hat, and {self.facial_hair} facial hair."
    