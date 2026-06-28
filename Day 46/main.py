import requests
from bs4 import BeautifulSoup
import os
import dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

dotenv.load_dotenv()

base_URL = "https://appbrewery.github.io/bakeboard-hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
user_choice = input("What year would you like to travel back to? Type the date in this format YYYY-MM-DD:")
URL = f"{base_URL}{user_choice}"
response = requests.get(URL, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

top_songs = soup.find_all(name="h3", class_="chart-entry__title")
top_songs_list = []
for song in top_songs:
    top_songs_list.append(song.text)

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user = sp.current_user()
account_id = user["id"]
q = f"track:{top_songs_list[0]} year:{user_choice[:4]}"
track_query = sp.search(q=q, limit=1, offset=0, type='track', market=None)
track_uri = track_query['tracks']['items'][0]['uri']

all_track_uri = []

for song in top_songs_list:
    try:
        q = f"track:{song} year:{user_choice[:4]}"
        track_query = sp.search(q=q, limit=1, offset=0, type='track', market=None)
        track_uri = track_query['tracks']['items'][0]['uri']
        all_track_uri.append(track_uri)
    except IndexError:
        pass
name = f"{user_choice} Billboard 100"
create_playlist = sp.user_playlist_create(user=account_id,name=name,public=False,collaborative=False,description="angela yu")
playlist_id = create_playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, tracks=all_track_uri)