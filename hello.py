import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.csgodatabase.com/cases/")
html = BS(r.content, 'html.parser')

el = html.find("h3", text="Prime Drops").find_next_sibling().find_next_sibling(
).find_next_sibling().find_next_sibling().find_next_sibling()
for item in el:
    item = el.find_all(class_="item-box-header")
for each in item:
    print(each.text)
