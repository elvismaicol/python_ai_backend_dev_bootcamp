from datetime import date, datetime, timedelta

tipo_carro = "M"  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# O carro chegou: 2024-05-07 21:37:25.142444 e ficará pronto às 2024-03-23 21:37:25.142444

print(date.today() - timedelta(days=1))
# 2024-05-06

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())
# 09:19:20

print(datetime.now().date())
# 2024-05-07