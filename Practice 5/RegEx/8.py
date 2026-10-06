import re
text="HelloWorldPython"
pattern=r"(?=[A-Z])"
print(re.split(pattern,text))