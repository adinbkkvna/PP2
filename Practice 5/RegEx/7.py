import re
def snake(text):
    return re.sub(r"_([a-z])",lambda m: m.group(1).upper(),text)
print(snake("kazakh_british_technical_university"))