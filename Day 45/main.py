from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

span_tag = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for tag in span_tag:
    tagg = tag.find(name="a")
    tag_link = tagg.get("href")
    tag_text = tagg.getText()
    article_links.append(tag_link)
    article_texts.append(tag_text)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_votes = max(article_upvotes)
max_index = article_upvotes.index(max_votes)
print(article_texts[13])









# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name='a')
#
# for tag in all_anchor_tags:
#     print(tag.getText())