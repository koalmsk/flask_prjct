from flask import Flask, jsonify
from flask_restful import abort, Api, Resource

from data import db_session
from data.recipes import Recipes
from db_functions import get_recipe

db_session.global_init("db/main.db")

app = Flask(__name__)
api = Api(app)


def abort_if_recipes_not_found():
    session = db_session.create_session()
    recipes = session.query(Recipes).first()
    if not recipes:
        abort(404, message=f"Recipes not found")


class RecipesResource(Resource):
    def get(self):
        # abort_if_recipes_not_found()
        recipes = get_recipe()
        return jsonify({'recipes': recipes.to_dict(
            only=('title', 'servings', 'instructions'))})


# для списка объектов
api.add_resource(RecipesResource, '/api/recipes')
app.run()