from django.shortcuts import render
import requests
from googletrans import Translator
from django.core.paginator import Paginator

# Create your views here.

def characters(request, page=1): # request é padrão django / são os dados carregados
    # print(api.characterTranslatered)
    characters = charactersJSON()
    characterTranslatered = translateAtributes('name', 'affiliation', characters)

    paginator = Paginator(characterTranslatered, per_page=5)
    page_object = paginator.get_page(page)

    context = {'page_object': page_object}

    return render(request, 'index.html', context) # dados, página


def charactersJSON():
    r = requests.get('https://last-airbender-api.fly.dev/api/v1/characters')
    character = r.json()
    return character


def translateAtributes(atribute1, atribute2, dict):
    for person in dict:
        person[f'{translater(atribute1)}'] = translater(person[atribute1])
        if atribute2 in person:
            person[f'{translater(atribute2)}'] = translater(person[atribute2])
        # print(json.dumps(person, ensure_ascii=False, indent=4))
        # print('proximo')
    return dict


def translater(word, dest='pt', src='en'):
    translator = Translator()
    return translator.translate(word, dest=dest, src='en').text