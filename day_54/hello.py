from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Here goes paragraph!</p>' \
           '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Olive_baboon_Ngorongoro.jpg/' \
           '220px-Olive_baboon_Ngorongoro.jpg">' \
           '<img src="https://media2.giphy.com/media/dQuXnEyFlMsrk0v0fG/200w.webp?cid=ecf05e47q3wlxzxtn4epd1cf0wmb' \
           'tia59hljcugfncm3b6oi&ep=v1_gifs_search&rid=200w.webp&ct=g">'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
