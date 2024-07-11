
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
#print(ROOT_PATH.parent)

#os.mkdir(ROOT_PATH / 'novo-diretorio')

#arquivo = open(ROOT_PATH / "novo.txt", "w")
#arquivo.close()

#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "nome_alterado.txt")

#os.remove(ROOT_PATH / "nome_alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
