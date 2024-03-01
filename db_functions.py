from data import db_session
from data.users import User
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