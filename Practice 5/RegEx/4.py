import re
text="Adina Kbtu Programing Principles"
pattern=r"[A-Z][a-z]+"
print(re.findall(pattern,text))