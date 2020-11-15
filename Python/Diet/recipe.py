import requests
import json


apiKey = 'a0ab8407037c4a36a9f1e77fa128f2be'
url = 'https://api.spoonacular.com'

def get_recipe(ingredients=None):
    '''
    ingredients: csv string of ingredients
    '''
    params = {
        'ingredients': ingredients,
        'apiKey': apiKey
    }
    data = requests.get(url+'/recipes/findByIngredients', params=params)
    # data = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2')

    for item in data.json():
        print(item['title'])


if __name__=='__main__':
    get_receipe('spinach,chicken,feta')