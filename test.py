from flask import Flask
from data import db_session
from db_functions import create_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    create_user('superLogin', '123', name='Иван')
    app.run()




if __name__ == '__main__':
    main()
