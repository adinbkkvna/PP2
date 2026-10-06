import re
text = "HelloWorldPython"
pattern = r"(?<!^)(?=[A-Z])"
new_text = re.sub(pattern, " ", text)
print(new_text)  
