from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__, static_folder="client/static", template_folder="client/templates")
ui = FlaskUI(app=app, server="flask")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    ui.run()
