import re

def rearrange_name(name):

    result = re.search(r"^([\w .]*), ([\w .]*)$",name)
     #Edge Case
    if result == None:
        return name 

    return f"{result[2]} {result[1]}"