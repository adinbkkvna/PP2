import re
text = "helloWorldPython"
pattern = r"(?<!^)(?=[A-Z])"
new_text = re.sub(pattern, "_", text).lower()
print(new_text)