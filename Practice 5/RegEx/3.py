import re
text = "hello_world pp2_practice kbtu_official Hello_world"
pattern = r"[a-z]+_[a-z]+"
print(re.findall(pattern, text))  