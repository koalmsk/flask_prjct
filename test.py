from flask import Flask
from data import db_session
from db_functions import create_user
from utilites import check_password

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/main.db")
    app.run()




if __name__ == '__main__':
    main()
