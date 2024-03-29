import requests


def get_nutritients(query):
    param = query
    spoonacular_request = f"https://api.spoonacular.com/recipes/complexSearch?query={param}&apiKey=8a7f512606ab41ee8f03c29701dfc065"
    # Выполняем запрос.
    response = requests.get(spoonacular_request)
    if response:
        json_response = response.json()
        id = json_response["results"][0]["id"]
        # print(json_response)
        second_request = f"https://api.spoonacular.com/recipes/{id}/nutritionWidget.json?&apiKey=8a7f512606ab41ee8f03c29701dfc065"
        response1 = requests.get(second_request)
        if response1:
            json_response1 = response1.json()
            calories = int(json_response1['calories'])
            carbs = int(json_response1['carbs'][:-1])
            fat = int(json_response1['fat'][:-1])
            protein = int(json_response1['protein'][:-1])
            return ({'calories': calories, 'carbs': carbs, 'fat': fat, 'protein': protein})
        # f'calories:{calories}, carbs:{carbs}, fat:{fat}, protein:{protein}'
        # for i in json_response:
        #     ids = []
        #     fats = 0
        #     carbs = 0
        #     protein = 0
        #     id = int(i['id'])
        #     fats += int(i['fat'][:-1])
        #     carbs += int(i['carbs'][:-1])
        #     protein += int(i['protein'][:-1])
        #     title = i['title']
        #     image_link = i['image']
        #     map_file = "map.png"
        #     with open(map_file, "wb") as file:
        #         file.write(response.content)
        #     print(response)
        #     print(f'title:{title}, id:{id}, fats:{fats}, carbs:{carbs}, protein:{protein}')
    else:
        return ("Ошибка выполнения запроса:")
        # print(spoonacular_request)
        # print("Http статус:", response.status_code, "(", response.reason, ")")


def get_meals(limit=5):
    random_food = 'https://api.spoonacular.com/recipes/random'
    parameters = {'number': limit, 'apiKey': '8a7f512606ab41ee8f03c29701dfc065'}
    response_F = requests.get(random_food, params=parameters)
    if response_F:
        json_responseF = response_F.json()
        spisok = json_responseF['recipes']
        spisok1 = []
        for item in spisok:
            slovar = {}
            slovar['id'] = item['id']
            slovar['foto'] = item['image']
            slovar['title'] = item['title']
                # ingridients [{name,quantity}]
                # text
            spisok1.append(slovar)
        return spisok1


print(get_nutritients('cheese'))
print(get_meals())
