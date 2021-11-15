from bs4 import BeautifulSoup

# read a file: "r"
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

tag = doc.find("option") # only fetch the first one
# access to all attributes
# print(tag.attrs)

# # call attributes like in dictionary
# tag["selected"] = "hello"
# # add attributes in the tag
# tag["colour"] = "blue"
# print(tag)

# # find multiple tags
# tags = doc.find_all(["p", "div", "li"])
# print(tags)

# multiple conditions
# tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate") # fetch all of it, so it turns to a list
# how to access the content through an attribute print(tags["value"])
# find_all give a list, so need to indicate index first and access to attribtes
# tag + attribute conditions
# print(tags)
# t = doc.find_all(["option"]) 
# print(tags) # find_all is a list, don't have .string method
# print(t)

# find class name
# tags = doc.find_all(class_="btn-item")
# print(tags)

# find regular expression
import re
# tags = doc.find_all(text=re.compile("\$.*")) # dollar sign is a reserved symbol, so add "\"
# for tag in tags:
#     print(tag.strip()) # strip: remove all the spaces

# limit the result amount
# tags = doc.find_all(text=re.compile("\$.*"), limit=1) # dollar sign is a reserved symbol, so add "\"
# for tag in tags:
#     print(tag.strip()) # strip: remove all the spaces

# save modified model: "w"
tags = doc.find_all("input", type="text")
for tag in tags:
    tag["placeholder"] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))


