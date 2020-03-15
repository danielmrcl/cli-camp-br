# desafio 073 - curso em vídeo - mundo 3 [13/03/2020] - 1.0
# tupla com o nome dos times em ordem de classificaçao
camp_bras_class = ( "FLAMENGO", "SANTOS", "PALMEIRAS", "GREMIO", "ATHLETICO-PR",
                    "SAO PAULO", "INTERNACIONAL", "CORINTHIANS", "FORTALEZA",
                    "GOIAS", "BAHIA", "VASCO DA GAMA", "ATHLETICO-MG", "FLUMINENSE",
                    "BOTAFOGO", "CEARA SC", "CRUZEIRO", "CSA", "CHAPECOENSE", "AVAI" )
def colocacao(inicio, fim): # função que retorna a colocação
    for c in range(inicio, fim):
        print(f"{c+1}º\t{camp_bras_class[c]}")
# inicio
print("""
Campeonato Brasileiro de Futebol [15:46 13/03/2020]
Escolha uma das opções abaixo:
[1] listar os times em ordem alfabética
[2] todas as 20 colocações
[3] saber a posição de um time específico
[4] apenas os 4 últimos colocados
[5] apenas as 5 primeiras colocações
[0] SAIR
""")
opc_usr = int(input("[0 a 5] >>> "))
if opc_usr == 1: # listar os times em ordem alfabética
    for c in range(0, 20):
        print(f"{c+1}\t{sorted(camp_bras_class)[c]}")
elif opc_usr == 2: # todas as 20 colocações
    colocacao(0, 20)
elif opc_usr == 3: # saber a posição de um time específico
    opc_usr_time = str(input("Digite o nome do time a ser pesquisado [sem acentuaçao]: ")).upper().strip()
    if opc_usr_time in camp_bras_class:
        print(f"{(camp_bras_class.index(opc_usr_time))+1}°\t{opc_usr_time}")
    else:
        print(  "Este time não consta entre os 20 classificados...",
                "Verifique se o nome foi digitado corretamente."    )
elif opc_usr == 4: # apenas os 4 últimas colocações
    colocacao(16, 20)
elif opc_usr == 5 : # apenas as 5 primeiras colocações
    colocacao(0, 5)
elif opc_usr == 0: # SAIR
    print("Saindo imediatamente...")
    exit()
else: # opcao invalida
    print("ERRO: Opção inválida, tente novamente")
