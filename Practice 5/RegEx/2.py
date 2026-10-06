import re
text="ab abb abbbb abbbbb" 
pattern=r"ab{2,3}"
print(re.findall(pattern,text))