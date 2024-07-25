from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(static_folder="client/static", template_folder="client/templates")
ui = FlaskUI(app)

@app.route("/")
def home():
    render_template("index.html")

if __name__ == "__main__":
    ui.run()
