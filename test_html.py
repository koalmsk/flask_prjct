import flask 
import remote_api

app = flask.Flask(__name__)


@app.route("/recipe/<id>")
def test(id):
    data = remote_api.get_recipe(id)
    
    return flask.render_template("single.html", **data[0])


@app.route("/contact")
def contact():
    # data = remote_api.get_recipe("pasts")

    return flask.render_template("contact.html")


@app.route("/found_dish")
def found_dish():
    # data = remote_api.get_recipe("pasts")

    return flask.render_template("found_dish.html")


if __name__ == "__main__":
    app.run(port=4000)