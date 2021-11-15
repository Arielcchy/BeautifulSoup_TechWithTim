from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

# print(doc.prettify())

# find things from the html tag
tag = doc.title
# print(tag)
# print(tag.string)

# modify the tag content
# tag.string = "hello"
# print(tag)

# find all by tag name
tagAll = doc.find_all("p")[0]
# print(tagAll)
print(tagAll.find_all("b"))




