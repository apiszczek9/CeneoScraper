import requests
from bs4 import BeautifulSoup

respons = requests.get('https://www.ceneo.pl/63419968#tab=reviews')

page_dom = BeautifulSoup(respons.text, "html.parser")

opinions = page_dom.select("div.js_product-review")
#print(type(opinions))
opinion = opinion.pop(0)
#print(type(opinion))

opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post_author-name").text.strip()
recomm = opinion.select_one(
    "span.user-post+author-recommendation").text.strip()
stars = opinion.select_one("span.user-post_score-count").text.strip()
#print(type(author))
print(recomm)

#print(page_dom.prettify())