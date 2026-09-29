from datetime import datetime
now=datetime.now()
microseconds=now.replace(microsecond=0)
print(microseconds)