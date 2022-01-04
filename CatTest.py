import json

from cat import Cat

with open(r'AnimalDict.json', encoding='utf8') as AnimalD:
    templates = json.load(AnimalD)


def check_cat():
    if "Cat" in templates.elem():
        return True
    else:
        print("There are no one cats here.")


for elem in templates['results']:
    if elem.get('species') == 'cat':
        if elem == 'species' and check_cat:
            obj_Cat = Cat(elem['name'], elem['gender']['name'], elem['age'])
            print(obj_Cat.name)


