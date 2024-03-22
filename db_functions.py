from data import db_session
from data.users import User
from data.recipes import Recipes
from utilites import get_hash_password

def create_user(login, password, **params):
    # Описываем созадваемого пользователя
    user = User()
    user.name = params['name']
    user.password = password
    user.login = login
    user.hashed_password=get_hash_password(user.login, user.password)

    # Кладем запись в БД
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    print('Создан пользователь')


def create_recipes(title, ingredients, servings, instructions):
    # Описываем созадваемого пользователя
    recipe = Recipes()
    recipe.title = title
    recipe.servings = servings
    recipe.instructions = instructions

    # Кладем запись в БД
    db_sess = db_session.create_session()
    db_sess.add(recipe)
    db_sess.commit()

    print('Создан рецепт:', title)


def get_recipe():
    db_sess = db_session.create_session()
    recipe = db_sess.query(Recipes).first()
    return recipe

# добавть поиск по ингридиентам и порциям по умолчанию Naun
