from datetime import date, timedelta
current_date=date.today()
new_data=current_date-timedelta(days=5)
print(new_data)
