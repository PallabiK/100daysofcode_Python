from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
index = article_upvotes.index(largest_number)

print(f"Article: {article_texts[index]}\nLink:{article_links[index]}\nUpvotes:{article_upvotes[index]}")

#import lxml

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)

# all_para_tags = soup.find_all(name="p")
#
# for tag in all_para_tags:
#     print(tag.getText())
#
# anchor_tag = soup.find_all(name="a")
# for tag in anchor_tag:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading=soup.select(".heading")
# print(heading)
#
# name=soup.select("#name")
# print(name)


