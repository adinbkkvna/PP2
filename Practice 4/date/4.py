from datetime import datetime

dt1 = datetime(2026, 9, 29, 10, 9, 1)
dt2 = datetime(2026, 9, 29, 15, 30, 45)

difference = dt2 - dt1
total= difference.total_seconds()
print(total)