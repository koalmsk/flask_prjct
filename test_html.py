import flask 

app = flask.Flask(__name__)


@app.route("/")
def test():
    return flask.render_template("single.html")



if __name__ == "__main__":
    app.run(port=4000)