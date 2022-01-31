import csv
import json
from config import CSV_HEADERS

def make_json(data):
    with open('rarity.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def init_CSV():
    with open(r'nft_project/results/csv/nft.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADERS)

def write_to_CSV(data):
    with open(r'nft_project/results/csv/nft.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
def individual_json(data):
    #data needs to come in as a dictionary for this to work
    with open(f'nft_project/results/json/{data["name"]}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def json_metadata(data):
    with open(f'nft_project/results/json/_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)