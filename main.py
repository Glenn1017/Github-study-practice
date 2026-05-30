from datetime import date
from bday_messages import rdm
today = date.today()
nb = date(2026,10,17)
days_away = (nb - today).days
if today  == nb:
    print(rdm)
else:
    print(f'My next birthday is {days_away} days away!')
