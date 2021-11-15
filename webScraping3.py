from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trows = tbody.contents # a list of all tags inside tbody
# print(trows)

# tree sibling
# print(trows[0].next_sibling)
# print(trows[1].previous_sibling)
# print(trows[0].next_siblings) # generator object-> an iteration object
# print(list(trows[0].next_siblings))

# tree parents and descendents
# print(trows[0].parent)
# print(list(trows[0].descendants))
# print(list(trows[0].contents))
# print(list(trows[0].children))

# getting crypto prices
# 1st step:
prices = {}
# for trow in trows:
#     for td in trow.contents[2:4]:
#         print(td)
#         print()
# 2nd step: narrow down to find coin names
# for trow in trows:
#     name, price = trow.contents[2:4]
#     print(name.p) # look for a p tag in name
#     print()
# 3rd step: bottom coins do not store names in p tag, sort it out
# for trow in trows[:10]: # get top 10
#     name, price = trow.contents[2:4]
#     fixed_name = name.p.string
#     print()
# 4th step: looking for the price
# for trow in trows[:10]: # get top 10
#     name, price = trow.contents[2:4]
#     fixed_name = name.p.string
#     print(price)
# 5th step: observe from the result from step 4, price is inside of <a>
# for trow in trows[:10]: # get top 10
#     name, price = trow.contents[2:4]
#     fixed_name = name.p.string
#     print(price.a.string)
# 6th step: store price in the dictionary
for trow in trows[:10]: # get top 10
    name, price = trow.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)



