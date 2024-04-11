import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "c": [".c"],
    "c++": [".c++"],
    "css": [".css"],
    "csv": [".csv"],
    "dart": [".dart"],
    "doc": [".doc"],
    "exe": [".exe"],
    "git": [".git"],
    "html": [".html"],
    "ino": [".ino"],
    "imagens": [".png," "jpg"],
    "java": [".java"],
    "javascript": [".js"],
    "mp3": [".mp3"],
    "pdf": [".pdf"],
    "php": [".php"],
    "planilhas": [".xlsx"],
    "python": [".python"],
    "rar": [".rar"],
    "ruby": [".ruby"],
    "zip": [".zip"]
}

for arquivo in lista_arquivos:
    nome, extensão = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensão in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")