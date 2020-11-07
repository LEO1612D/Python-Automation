import re

charcase = re.search(r"[pP]ython","Python")
print(charcase)


charcase = re.search(r"[a-z]bye","zbye")
print(charcase)

#finds any matching '-' defines ranging
charcase = re.search(r"[a-zA-Z0-9]bye","Abye")
print(charcase)

#finds character which isn't in the list
charcase = re.search(r"[^a-zA-z]","Abye jsadk aksj")
print(charcase)

#or
like = re.search(r"cat|dog", "i like cat")
print(like)

#findall
like = re.findall(r"cat|dog", "i like cat i like dog")
print(like)


