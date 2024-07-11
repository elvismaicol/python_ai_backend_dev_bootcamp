from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
# 2024-05-08 02:59:43.621004+02:00

print(data_sao_paulo)
# 2024-05-07 21:59:43.621004-03:00