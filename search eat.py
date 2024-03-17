import json
import requests
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    name_of_eat = input("Введите название блюда:")
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(name_of_eat)
    response = requests.get(api_url, headers={'X-Api-Key': '68VExiXeWSEK7IDBVrtJfw==W8g20fDjCJkSbCkr'})

    if response.status_code == requests.codes.ok:
        data = response.json()  # Преобразуем текст ответа в формат JSON

        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file, indent=4, ensure_ascii=False)  # Записываем JSON данные в файл с отступами

        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
            dish_name = data[0]["title"]
            ingredients = data[0]["ingredients"].split(";")
            instructions = data[0]["instructions"].split(";")

            return render_template('found_dish.html', dish_name=dish_name, ingredients=ingredients, instructions=instructions)

    return "Произошла ошибка"

if __name__ == '__main__':
    app.run(debug=True)
