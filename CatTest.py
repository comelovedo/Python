import json

from cat import Cat


def check_cat(elem, item):
    if elem[item]['code'] == 'cat' in templates:
        return True


with open(r'AnimalDict.json', encoding='utf8') as AnimalD:
    templates = json.load(AnimalD)

for elem in templates['results']:
    for item in elem:
        if item == 'species' and check_cat(elem, item):
            obj_Cat = Cat(elem['name'], elem['gender']['name'], elem['age'])
            print(obj_Cat.name)
