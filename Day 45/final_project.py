import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# response = requests.get(URL)
html_doc = """
<article class="article-movie-title">
  <h3 class="title">1. The Godfather</h3>
</article>
<article class="article-movie-title">
  <h3 class="title">2. Raiders of the Lost Ark</h3>
</article>
"""
soup = BeautifulSoup(html_doc, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

movies = []
for title in movie_titles:
    movie_title = title.getText()
    movies.append(movie_title)
movies.reverse()
print(movies)