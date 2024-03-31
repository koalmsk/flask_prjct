import flask 
import remote_api
app = flask.Flask(__name__)


@app.route("/")
def test():
    data = remote_api.get_recipe("pasts")
    
    return flask.render_template("single.html", **data[0])



if __name__ == "__main__":
    app.run(port=4000)