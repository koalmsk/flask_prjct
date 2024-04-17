import requests
import random


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


def get_recept(id):
    param = id
    recipe_info = f'https://api.spoonacular.com/recipes/{param}/information?includeNutrition=false&apiKey=8a7f512606ab41ee8f03c29701dfc065'
    response3 = requests.get(recipe_info)
    if response3:
        json_response3 = response3.json()
        sumarise_info = json_response3['summary']
        image = json_response3['image']
        instructions = json_response3['instructions']
        title = json_response3['title']
        steps = []
        county = 1
        if json_response3['analyzedInstructions']:
            for i in json_response3["analyzedInstructions"][0]['steps']:
                textinfo = i['step']
                steps.append({'number': county,
                              'content': textinfo})
                county += 1
            return [steps, instructions, image, sumarise_info, title]
        else:
            return [[{"number": "no number", 'content': 'No content'}], instructions, image, sumarise_info, title]
        # print(steps)
        # print(instructions)
        # print(image)
        # print(sumarise_info)
def get_filtered_food(min_carbs, max_carbs, min_protein, max_protein, min_calories, max_calories, min_fat, max_fat):
    recipe_chr = f'https://api.spoonacular.com/recipes/findByNutrients?minCarbs={min_carbs}&maxCarbs={max_carbs}&minProtein={min_protein}&maxProtein={max_protein}&minCalories={min_calories}&maxCalories={max_calories}&minFat={min_fat}&maxFat={max_fat}&apiKey=8a7f512606ab41ee8f03c29701dfc065'
    response4 = requests.get(recipe_chr)
    if response4:
        print('aboba')
        json_response4 = response4.json()
        dlina = len(json_response4)
        if dlina == 0:
            return 0
        i = random.choice(range(dlina))
        print(json_response4)
        number = json_response4[i]['id']
        return number

# print(get_nutritients('cheese'))
# print(get_meals())
# print(get_recept(653785))
print(get_meals)
