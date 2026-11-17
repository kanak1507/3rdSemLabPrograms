from datetime import date, datetime
today = date.today()
print("Today's date:", today)
now = datetime.now()
print("Now (date and time):", now)
print("Current time:", now.strftime("%H:%M:%S"))
print("Day of the week:", now.strftime("%A"))
print("Month and Year:",today.strftime("%d %B %Y"))