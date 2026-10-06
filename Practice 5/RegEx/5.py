import re
text="acb appleb axxxb ac"
pattern=r"a.*b"
print(re.findall(pattern,text))