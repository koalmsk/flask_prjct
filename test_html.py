import flask
from flask import redirect, render_template
import random

import remote_api
from data import db_session
from db_functions import create_user
from login import LoginForm
from making_form import CreterionForm
from registration import RegisterForm
from utilites import check_password

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# @app.route("/")
# def test():
#     data = remote_api.get_recipe("pasts")

#     return flask.render_template("single.html", **data[0])

@app.route('/')
@app.route('/index')
def main():
    spisok = remote_api.get_meals()
    print(spisok)
    spisok2 = [i['foto'] for i in spisok]
    spisok3 = [i['title'] for i in spisok]
    spisok4 = [i['id'] for i in spisok]
    return flask.render_template('index.html', firstimg=spisok2[0], secondimg=spisok2[1], thirdimg=spisok2[2],
                                 fourthimg=spisok2[3], fifthimg=spisok2[4], title1=spisok3[0], title2=spisok3[1],
                                 title3=spisok3[2], title4=spisok3[3], title5=spisok3[4], id1=spisok4[0],
                                 id2=spisok4[1], id3=spisok4[2], id4=spisok4[3], id5=spisok4[4])


@app.route("/recipe/<id>")
def test(id):
    data = remote_api.get_recept(id)
    return flask.render_template("single.html", title=data[4], instructions=data[1], steps=data[0], image=data[2])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        if check_password(form.username.data, form.password.data):
            return redirect("/")
        return 'not now, not yet'
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form1 = RegisterForm()
    print(form1.password.data)
    if form1.validate_on_submit():
        if form1.password.data != form1.password_again.data:
            return 'LOL'
        create_user(form1.email.data, form1.password.data, form1.name.data)
        return redirect('/login')
    return render_template('registration.html', title='Registration', form=form1)
    # data = remote_api.get_recipe("pasts")

    return flask.render_template("contact.html")

@app.route('/food_filter', methods=['GET', 'POST'])
def food_filter():
    form3 = CreterionForm()
    if form3.validate():
        listik = remote_api.get_filtered_food(form3.min_carbs.data, form3.max_carbs.data, form3.min_protein.data, form3.max_protein.data, form3.min_calories.data, form3.max_calories.data, form3.min_fat.data, form3.max_fat.data)
        dlina = len(listik)
        number = random.choice(range(dlina))
        if dlina == 0:
            return render_template('foodcretecion.html', title='Food filter', form=form3)
        else:
            data1 = remote_api.get_recept(number)
            if dlina > 5:
                return flask.render_template("single.html", title=data1[4], instructions=data1[1], steps=data1[0],
                                             image=data1[2], spisok1=listik[:5])
            else:
                return flask.render_template("single.html", title=data1[4], instructions=data1[1], steps=data1[0], image=data1[2], spisok1=listik)
    return render_template('foodcretecion.html', title='Food filter', form=form3)


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.run(port=4000)
