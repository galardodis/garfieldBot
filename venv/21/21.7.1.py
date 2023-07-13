import json
from Cat import Cat

with open('pets.json', 'r', encoding='utf8') as f:
    pets = json.load(f)

cats = []

for i in pets:
    if i['species']['name'] == 'кошка':
        print(i)
        cats.append(Cat(i['name'], i['gender']['name'], i['age']))
