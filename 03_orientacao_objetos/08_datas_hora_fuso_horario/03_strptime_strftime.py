from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))
# 07/05/2024 

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
# Tue 2023-10-20 10:20:00

print(type(data_convertida))
# <class 'datetime.datetime'> 
