from datetime import date, datetime
today = date.today()
print("Today's date:", today)
now = datetime.now()
print("Now (date and time):", now)
print("Current time:", now.strftime("%H:%M %p"))
print("Day of the week:", now.strftime("%A"))
print("Today in DD/MM/YYYY:",today.strftime("%d %B %Y"))