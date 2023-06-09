import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies]
# movies_new_list = movies_list[::-1]
movies_list.reverse()

with open("movies.txt", mode="w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")


