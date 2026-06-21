import datetime, bday_messages as bd
today = datetime.date.today()
next_birthday = datetime.date(2027,3,23)

days_away = next_birthday - today
if today == next_birthday:
    print(bd.random_message)
else:
    print('My next birthday is {days_away} days away!')