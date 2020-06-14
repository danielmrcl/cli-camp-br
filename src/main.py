# NOTE: funcao principal
import functions

def main():
    functions.clear_screen()

    rank = functions.open_rank()

    print(functions.get_info())
    opc_usr = int(input("[0 a 5] >>> "))

    if opc_usr == 1:
        # NOTE: listar os times em ordem alfabetica
        print("\n--- Ordem alfabetica:")

        sorted_rank = sorted(rank)

        functions.rank(0, len(rank), sorted_rank)

        print("---\n")
    elif opc_usr == 2:
        # NOTE: todas as 20 colocacoes
        print("\n--- 20 primeiros colocados:")

        functions.rank(0, 20, rank)

        print("---\n")
    elif opc_usr == 3:
        # NOTE: pesquisar por nome
        print("\n--- Pesquisar por nome:")

        print("- Digite o nome (ou parte dele) do time a ser pesquisado [sem acentuaçao]:")
        search = str(input("- >>> ")).upper().strip()

        teams_found = []

        for team in rank:
            if search in team:
                teams_found.append(team)

        if len(teams_found) > 0:
            for team in teams_found:
                index = rank.index(team)
                print(f"- {index+1:>2}°\t{rank[index]}")
        else:
            print(  "Este time não consta entre os 20 classificados..."
                    "Verifique se o nome foi digitado corretamente."    )

        print("---\n")
    elif opc_usr == 4:
        # NOTE: apenas as 4 ultimas colocacoes
        print("\n--- 4 ultimas colocacoes:")

        lenght = len(rank)

        functions.rank(lenght-4, lenght, rank)

        print("---\n")
    elif opc_usr == 5:
        # NOTE: apenas as 5 primeiras colocacoes
        print("\n--- 5 primeiras colocacoes:")

        functions.rank(0, 5, rank)

        print("---\n")
    elif opc_usr == 0:
        print("Saindo imediatamente...")
        exit()
    else:
        print("ERRO: opcao invalida, tente novamente")

    input("Para continuar digite ENTER: ")
    main()

main()
