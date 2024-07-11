from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
# 2023-07-10
print(date.today())
# 2024-05-07

data_hora = datetime(2023, 7, 10)
print(data_hora)
# 2023-07-10 00:00:00

print(datetime.today())
# 2024-05-07 21:25:55.791869

hora = time(10, 20, 0)
print(hora)
# 10:20:00