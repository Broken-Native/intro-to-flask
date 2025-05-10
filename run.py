from flask_app import create_app
from config import development_config


app = create_app("config.development_config")
# app = create_app("hilary")

@app.route("/")
def hello_world():
    return "<p>Hello i'm learning flask</p>"


@app.route("/about")
def about():
    return "I am a  "


if __name__ == '__main__':
    app.run()