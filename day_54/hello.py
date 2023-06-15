from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/okay")
def okay_world():
    return "Alrighty!"


if __name__ == "__main__":
    app.run()
