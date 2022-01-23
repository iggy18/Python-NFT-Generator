import random
from timer import speed
from attrsList import name, head, eyes, mouth, nose, hat, facial_hair
from char import NFT
from generator import multiplier



@speed
def generate(max):
    for i in range(1, max):
        unit = NFT(
            name=random.choice(name), 
            head=random.choice(head),
            eyes=random.choice(eyes),
            mouth=random.choice(mouth),
            nose=random.choice(nose),
            hat=random.choice(hat),
            facial_hair=random.choice(facial_hair)
        )

        
x = generate(10000)

x = multiplier(10000)
