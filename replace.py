import re

# result = re.sub(r"^([\w \.-]*), ([\w \.-]*)$",r"\2 \1","Nikunj, Prajapati")
# print(result)


# def transform_record(record):
#   new_record = re.sub(r"([,\]+)",r"\1 \+1- \2",record)
#   return new_record

# print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# # Sabrina Green,+1-802-867-5309,System Administrator

# print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# # Eli Jones,+1-684-3481127,IT specialist

# print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# # Melody Daniels,+1-846-687-7436,Programmer

# print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# # Charlie Rivera,+1-698-746-3357,Web Developer



print(re.sub(r"(,\d)",r",+1-","Charlie Rivera,698-746-3357,Web Developer")) 


print(re.findall(r"[ ](\d{3,})[-]","My number is 212-345-9999."))


#  re.sub(r"(,\d)",r",+1-\1",record)

#   r"[\w]+[aeiouAEIOU]{3,}[\w]+"

#    re.sub(r"[#]+",r"//",line_of_code)