# Usando função com arqumentos

def salvar_moto(marca, modelo, ano, placa):
    # salva moto no banco de dados...
    print(f"Moto inserida com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_moto("Honda", "CB-500", 2024, "ABC-1D34")
salvar_moto(marca="Honda", modelo="CB-500", ano=2024, placa="ABC-1D34")
salvar_moto(**{"marca": "Honda", "modelo": "CB-500", "ano": 2024, "placa": "ABC-1D34"})