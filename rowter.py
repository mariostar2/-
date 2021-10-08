from flask import Flask
from flask.templating import render_template
import movie_api as mop
import weader_api as wap

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html", movies=mop.MovieApi(),temp = wap.getTempature)
if __name__ == "__main__":
    app.run(debug=True)