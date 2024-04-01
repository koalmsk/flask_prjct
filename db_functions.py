from data import db_session
from data.users import User
from data.recipes import Recipes
from data.comments import Comments
from utilites import get_hash_password


def create_user(email, hashed_password, name):
    db_sess = db_session.create_session()

    # Описываем созадваемого пользователя
    user = User()
    user.name = name
    user.password = hashed_password
    user.login = email
    user.hashed_password = get_hash_password(user.login, user.password)
    # I dont know how to separate one from enother.
    # Кладем запись в БД
    db_sess.add(user)
    db_sess.commit()
    print('Создан пользователь')


def create_recipes(title, ingredients, servings, instructions):
    db_sess = db_session.create_session()

    # Описываем созадваемого пользователя
    recipe = Recipes()
    recipe.title = title
    recipe.servings = servings
    recipe.instructions = instructions

    # Кладем запись в БД

    db_sess.add(recipe)
    db_sess.commit()

    print('Создан рецепт:', title)


def update_likes(recipe_id):
    db_sess = db_session.create_session()

    recipe = db_sess.query(Recipes).filter(Recipes.id == recipe_id).first()
    recipe.likes += 1
    db_sess.commit()


def get_recipe(limit: int = 1, query=None):
    db_sess = db_session.create_session()

    recipe = db_sess.query(Recipes).limit(limit).all()
    return recipe


def add_comment(recipe_id, user_id, text):
    db_sess = db_session.create_session()

    comment = Comments()
    comment.from_user_id = user_id
    comment.recipe_id = recipe_id
    comment.text = text
    db_sess.add(comment)
    db_sess.commit()


def get_comments(recipe_id):
    db_sess = db_session.create_session()

    comments_by_recipe = db_sess.query(Comments).filter(Comments.recipe_id == recipe_id).all()
    user_info_text = list()
    for comment in comments_by_recipe:
        user = db_sess.query(User).filter(User.id == comment.from_user_id).first()
        user_comment = {
            "text": comment.text,
            "name": user.name,
            "photo": user.photo
        }
        user_info_text.append(user_comment)

    return user_info_text


# добавть поиск по ингридиентам и порциям по умолчанию Naun
# добавить post resipe
# создать табличку для комментов к рецепту
# фк рецепт, фк юзкр, текст коммента
# метод comments(recipe.id) и класс RecipeCommentResourse

if __name__ == "__name__":
    db_session.global_init("db/main.db")
