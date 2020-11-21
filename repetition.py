import re

# * means any number of times AS MANY AS POSSIBLE
print(re.search(r"py.*n","pyasbdakn"))

#in programming this is called greedy approach
print(re.search(r"py.*n","python programming"))

print(re.search(r"py[a-z]*n","python programming"))

# + 
print(re.findall(r"n+m+","nikunnmmnj monalisannnmmm"))

# ? for 0 or more accurance

print(re.findall(r"n?iku","nikummm"))

#present at least twice
print(re.findall(r"a.*a","bansns"))

#atleast a present twice capital or small [aA].*[aA]