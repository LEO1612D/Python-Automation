import re

# result = re.search(r"^(\w*), (\w*)$","Nikunj, Prajapati")
# print(result)
# print(result.groups())



# for i in result.groups():
#     print(i)

# print("{} {}".format(result[1],result[2]))

def arrangeName(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)",name)
    if result is None:
        return name
     
    return "{} {}".format(result[2],result[1])



print(arrangeName("Nikunj, Prajapati R."))

# REPEATATION GROUPS

result = re.search(r"[a-zA-Z]{5}","a scary ghost appeard")
print(result)

resultAll = re.findall(r"[a-zA-Z]{5}","a scary ghost appeard")
print(resultAll)

resultAllExact = re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeard")
print(resultAllExact)


# {min,max}  , {min,} in this case maximum is any limit
resultInSpecificLength = re.findall(r"\w{5,10}","i really like python programming and reactjs")
print(resultInSpecificLength)





