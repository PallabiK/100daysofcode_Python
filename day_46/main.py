from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SP_CLIENT_ID = "YOURS"
SP_CLIENT_SECRET = "YOURS"

#input from user
date_from_user = input("What date do you want to go back to? Type in YYYY-MM-DD format:")

#webscarpping from BILLBOARD
URL = f"https://www.billboard.com/charts/hot-100/{date_from_user}/"
response = requests.get(URL)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)

#spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=" ",
        client_id=SP_CLIENT_ID,
        client_secret=SP_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = "YOURS"

song_uris =[]
year = date_from_user.split("-")[0]
month = date_from_user.split("-")[1]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{year}-{month} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



