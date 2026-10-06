import re
text="Kazakh, British, Technical, University."
pattern=r"[ ,.]"
new_text=re.sub(pattern, ":",text)
print(new_text)