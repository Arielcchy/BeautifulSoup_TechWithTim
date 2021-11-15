from os import link
from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={search_term}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# query multiple pages
page_text = doc.find(class_="list-tool-pagination-text").strong
lastPage = int(str(page_text).split(">")[-2].split("<")[0])

items_found = {} # store item, link, price in this dictionary
# find products by looping through all the pages
for page in range(1,lastPage+1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    # create my own filter, just make sure it only grab items I want
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell") # narrow the search zone to div class
    items = div.find_all(text=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != 'a':
            continue
        itemLink = parent['href']  
        # print(itemLink)
        # looking for price
        next_parent = item.find_parent(class_="item-container") #find all the parents with specific attribute
        price = next_parent.find(class_="price-current")

        try: 
            price_int = price.strong.string
            price_decimal = price.sup.string
            price_full = price_int+price_decimal
            items_found[item] = {"price": float(price_full.replace(",","")), "link": itemLink}
        except:
            pass

# sort list and put it back to the dictionary
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price']) # sort by the key: price
# .items() gives us the tuple with the keys and values

for s_item in sorted_items:
    print(s_item[0])
    print(f"${s_item[1]['price']}")
    print(s_item[1]['link'])
    print('-------------------------------')
