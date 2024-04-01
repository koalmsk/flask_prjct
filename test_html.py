import flask
from flask import redirect, render_template

import remote_api
from data import db_session
from db_functions import create_user
from login import LoginForm
from registration import RegisterForm
from utilites import check_password

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# @app.route("/")
# def test():
#     data = remote_api.get_recipe("pasts")
    
#     return flask.render_template("single.html", **data[0])

@app.route("/")
def test():
    data = remote_api.get_meals(limit=1)
    print(data)
    return flask.render_template("single.html", title=data[0]['title'], instruction=data[0]['id'])

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



if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.run(port=4000)