import json
import requests


def get_recipe(title):
    api_url = f'https://api.api-ninjas.com/v1/recipe?query={title}'
    response = requests.get(api_url, headers={'X-Api-Key': '68VExiXeWSEK7IDBVrtJfw==W8g20fDjCJkSbCkr'})

    if response.status_code == requests.codes.ok:
        data = response.json()  # Преобразуем текст ответа в формат JSON
        return data


    return "Произошла ошибка"


