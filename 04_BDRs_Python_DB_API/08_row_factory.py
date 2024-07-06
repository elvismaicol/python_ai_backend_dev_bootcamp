import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def atualizar_registros(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def deletar_registros(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def lista_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

clientes = lista_clientes(cursor)

for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])

print(f'Seja bem vindo ao sistema {cliente["nome"]}')