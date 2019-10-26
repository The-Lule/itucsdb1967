from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "Oh hi! Just trying to change some source files. Hope this works."


if __name__ == "__main__":
    app.run()
