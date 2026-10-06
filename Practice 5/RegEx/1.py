import re

text="ab acb abbbb ac ac abc" 
pattern=r"ab*"
print(re.findall(pattern,text))