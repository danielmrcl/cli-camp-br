# NOTE: arquivo de funcoes
import os, sys

# NOTE: criar uma funcao para pegar o arquivo da internet e trata-lo

# buscar a classificacao dos times:
def open_rank():
    archive = open("rank.txt")
    info = archive.read()
    archive.close()

    info = info.upper()
    info = info.split('\n')

    for c in info:
        if c == '':
            del info[info.index(c)]

    return info

# informacao incial:
def get_info():
    info = (
        "Campeonato Brasileiro de Futebol [15:49 14/06/2020]\n"
        "Escolha uma das opções abaixo:\n"
        "[1] listar os times em ordem alfabética\n"
        "[2] todas as 20 colocações\n"
        "[3] pesquisar por nome\n"
        "[4] apenas os 4 últimos colocados\n"
        "[5] apenas as 5 primeiras colocações\n"
        "[0] SAIR\n"
    )

    return info

# limpar a tela
def clear_screen():
    # Windows:
    if sys.platform == 'win32':
        return os.system("cls")
    # Linux:
    elif sys.platform == 'linux':
        return os.system("clear")
    # MacOS:
    elif sys.platform == 'darwin':
        return os.system("clear")

# listar o rank:
def rank(start, end, rank):

    for c in range(start, end):
        print(f"- {c+1:>2}\t{rank[c]}")

    return
