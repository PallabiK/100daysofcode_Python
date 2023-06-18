from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io/?name={name}")
    data_age = age_response.json()["age"]
    data_gender = gender_response.json()["gender"]
    return render_template("guess.html", name=name, age=data_age, gender=data_gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

