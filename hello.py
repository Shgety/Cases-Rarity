import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.csgodatabase.com/cases/")
html = BS(r.content, 'html.parser')

el = html.find("h3", text="Prime Drops").find_next_sibling().find_next_sibling(
).find_next_sibling().find_next_sibling().find_next_sibling()
for item in el:
    item = el.find_all(class_="item-box-header")
prime_drops = []
for each in item:
    prime_drops.append(each.text)
el = html.find("h3", text="Rare Cases").find_next_sibling(
).find_next_sibling().find_next_sibling().find_next_sibling()
for item in el:
    item = el.find_all(class_="item-box-header")
rare_drops = []
for each in item:
    rare_drops.append(each.text)
el = html.find("h3", text="Discontinued Cases").find_next_sibling(
).find_next_sibling().find_next_sibling().find_next_sibling()
for item in el:
    item = el.find_all(class_="item-box-header")
discountinued_drops = []
for each in item:
    discountinued_drops.append(each.text)

d = {
    "prime_drops": prime_drops,
    "rare_drops": rare_drops,
    "discontinued_drops": discountinued_drops
}
print(d)