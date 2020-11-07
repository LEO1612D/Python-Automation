import re
result = re.search(r"nik@","nik@unjniknik")
print(result)

startWith = re.search(r"^n","nikunj nick jack")
print("Start With : ",startWith)

endsWith = re.search(r"n$","nikunj nickn jacn")
print("Ends With : ",endsWith)

wildCard = re.search(r"w.t", "wnt wat wat")
print("Wild Card  : ",wildCard)

Ignorecase = re.search(r"w.t", "WNT wat wat",re.IGNORECASE)
print("caseSensitive  : ",Ignorecase)