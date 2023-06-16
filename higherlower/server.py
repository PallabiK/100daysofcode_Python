from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def guess():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media1.giphy.com/media/JdFEeta1hLNnO/200w.webp?cid=ecf05e47ue4kg31gm5b3onb45nx13p8s7yf' \
           '4o42vjtd127aa&ep=v1_gifs_search&rid=200w.webp&ct=g" width=500>'


random_number = random.randint(0, 10)


@app.route('/<int:number>')
def game(number):
    if number < random_number:
        return f'<h1 style="color: red">{number} is too low. Try again.</h1>' \
               f'<img src="https://media1.giphy.com/media/HSvpy6Jk396SI/200.webp?cid=ecf05e47g675rfmui0lh1na3ywff41' \
               f'cwig1be9jmfh7f6v2u&ep=v1_gifs_search&rid=200.webp&ct=g" width=500>'
    elif number > random_number:
        return f'<h1 style="color: purple">{number} is too high. Try again</h1>' \
               f'<img src="https://media4.giphy.com/media/I02FPwgjBgMZa/giphy.webp?cid=ecf05e47fzleubf4rwwn64y33v9b' \
               f'15sa0ig2l7dzmlh09hi2&ep=v1_gifs_search&rid=giphy.webp&ct=g" width=500>'
    elif number == random_number:
        return f'<h1 style="color: green">You guessed it correctly!\nThe number is {random_number}.</h1>' \
               f'<img src="https://media4.giphy.com/media/o75ajIFH0QnQC3nCeD/200.webp?cid=ecf05e4734dgsazjl7vkf' \
               f'drabl50bplusri54gi7vslk4r1a&ep=v1_gifs_search&rid=200.webp&ct=g" width=500>'


if __name__ == "__main__":
    app.run(debug=True)
