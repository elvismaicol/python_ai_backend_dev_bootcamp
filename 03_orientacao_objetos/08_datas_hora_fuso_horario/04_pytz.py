from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
# 2024-05-08 02:53:53.512406+02:00

print(data2)
# 2024-05-07 21:53:53.514411-03:00

# pip install pytz